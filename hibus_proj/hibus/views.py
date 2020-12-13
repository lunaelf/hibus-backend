from django.contrib.auth.models import User
from rest_framework import filters
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters.rest_framework import DjangoFilterBackend
from hibus_proj.hibus.models import Line, Bus, Order
from hibus_proj.hibus.serializers import UserSerializer, LineSerializer, BusSerializer, OrderSerializer

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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['url', 'id', 'station_start', 'station_end', 'estimate_hour', 'estimate_minute',
                        'start_latitude', 'start_longitude', 'start_location', 'end_latitude',
                        'end_longitude', 'end_location']


class LineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Line.objects.all()
    serializer_class = LineSerializer


class BusList(generics.ListCreateAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['url', 'id', 'line_id', 'bus_number', 'ticket_price', 'threshold_price',
                        'current_passenger', 'threshold_passenger', 'latitude', 'longitude',
                        'location', 'station', 'status', 'driver_phone']


class BusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['user_id', 'bus_id', 'line_id', 'order_type', 'status', 'station_start']
    ordering_fields = ['order_time']
    ordering = ['-order_time']


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
