from django.contrib.auth.models import User
from rest_framework import filters
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters.rest_framework import DjangoFilterBackend
from hibus_proj.hibus.models import Line, Bus, Order
from hibus_proj.hibus.serializers import UserSerializer, LineSerializer, BusSerializer, OrderSerializer
import uuid

# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'lines': reverse('line-list', request=request, format=format),
        'buses': reverse('bus-list', request=request, format=format),
        'orders': reverse('order-list', request=request, format=format),
    })


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LineList(generics.ListCreateAPIView):
    queryset = Line.objects.all()
    serializer_class = LineSerializer
    # 查询时增加过滤
    filter_backends = [DjangoFilterBackend]
    # 过滤字段，即 SQL 里的 WHERE
    filterset_fields = ['id', 'station_start', 'station_end', 'estimate_hour', 'estimate_minute',
                        'start_latitude', 'start_longitude', 'start_location', 'end_latitude',
                        'end_longitude', 'end_location']


class LineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Line.objects.all()
    serializer_class = LineSerializer


class BusList(generics.ListCreateAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    # 查询时增加过滤
    filter_backends = [DjangoFilterBackend]
    # 过滤字段，即 SQL 里的 WHERE
    filterset_fields = ['id', 'line_id', 'bus_number', 'ticket_price', 'threshold_price',
                        'current_passenger', 'threshold_passenger', 'latitude', 'longitude',
                        'location', 'station', 'status', 'driver_phone']


class BusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # 查询时增加过滤和排序
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    # 过滤字段，即 SQL 里的 WHERE
    filterset_fields = ['id', 'user_id', 'bus_id', 'line_id', 'order_number', 'base_order_number',
                        'order_type', 'order_time', 'passenger', 'payment', 'status', 'bus_start_time',
                        'bus_end_time', 'station_start', 'station_end']
    # 排序字段，即 SQL 里的 ORDER BY
    ordering_fields = ['order_time']
    # 默认排序字段。这里按照订单时间倒序
    ordering = ['-order_time']

    # 重写 POST 方法
    def create(self, request, *args, **kwargs):
        order_type = request.query_params.get('order_type', 0)
        if not request.data._mutable:
            request.data._mutable = True
        if order_type == 0:
            # 定制，生成相同的 order_number 和 base_order_number
            uuid4 = uuid.uuid4().__str__()
            request.data.update(
                {'order_number': uuid4, 'base_order_number': uuid4})
        elif order_type == 1:
            # 拼单，只生成 order_number
            uuid4 = uuid.uuid4().__str__()
            request.data.update({'order_number': uuid4})

        # HyperlinkedModelSerializer 在初始化的时候要设置 context
        serializer = OrderSerializer(
            data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
