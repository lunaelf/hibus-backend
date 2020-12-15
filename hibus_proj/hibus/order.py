from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models.query import QuerySet
from hibus_proj.hibus import models
import json



def queryOrder(request):
    user_id = request.POST.get("user_id")
    station_end = request.POST.get("searchendplace")
    status = request.POST.get("status")#[0=已下单, 1=已完成]
    order_type = request.POST.get("order_type")#0=定制订单
    # searchstarttime = int(request.POST.get("searchstarttime"))
    # searchendtime = int(request.POST.get("searchendtime"))
    kwargs = {}#sql的参数列表
    if user_id is not None and user_id is not '':#或者 in locals().keys()
        kwargs['user_id'] = int(user_id)
    if station_end is not None and station_end is not '':
        kwargs['station_end'] = station_end
    if order_type is not None and order_type is not '':
        kwargs['order_type'] = int(order_type)
    # if status is not None  and status in dir():
    #     kwargs['status'] = status
    #values()将结果转换为字典数据
    orderlist = models.Order.objects.filter(**kwargs)
    data = []
    for row in orderlist:
        bus = row.bus_id#models.Bus.objects.filter(id = int(row.bus_id_id))
        # row.bus_number = bus.bus_number
        # row.driver_phone = bus.driver_phone
        new = {}
        new['bus_number'] = bus.bus_number
        new['driver_phone'] = bus.driver_phone
        new['threshold_passenger'] = bus.threshold_passenger
        new['id'] = row.id
        new['user_id'] = row.user_id_id
        new['bus_id'] = row.bus_id_id
        new['order_type'] = row.order_type
        new['order_time'] = row.order_time
        new['passenger'] = row.passenger
        new['payment'] = row.payment
        new['status'] = row.status
        new['bus_start_time'] = row.bus_start_time
        new['station_end'] = row.station_end
        new['create_time'] = row.create_time
        data.append(new)
    # orderlist = models.Order.objects.values().filter(**kwargs)
    # print(orderlistObject)
    # jsonRow = serializers.serialize("json",data)
    # data["data"] = json.loads(data)
    return JsonResponse(data ,safe=False,content_type='application/json')


def saveOrder(request):
    id = int(request.POST.get("id"))
    if int(id)<0:#定制
        models.Order.objects.create(order_type=0,station_end=request.POST.get("station_end"),bus_start_time=request.POST.get("bus_start_time"),bus_id_id=request.POST.get("bus_id"),user_id_id=request.POST.get("user_id"),payment=request.POST.get("payment"),passenger=1)
        models.Bus.objects.filter(pk=request.POST.get("bus_id")).update(status=1)
        return HttpResponse("res")
    else:#拼单
        models.Order.objects.create(order_type=1,station_end=request.POST.get("station_end"),bus_start_time=request.POST.get("bus_start_time"),bus_id_id=request.POST.get("bus_id"),user_id_id=request.POST.get("user_id"),payment=request.POST.get("payment"),passenger=request.POST.get("passenger"))
        models.Order.objects.filter(pk=request.POST.get("id")).update(passenger=request.POST.get("passenger"))
        return HttpResponse("res")