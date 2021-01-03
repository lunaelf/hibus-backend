from django.http import HttpRequest
from django.http import JsonResponse
from django.db.models.query import QuerySet
from hibus_proj.hibus import models

def querystatusBus(request):
    #bus = models.Bus.objects.filter(status=0).first()
    bus = models.Bus.objects.values().filter(status=0).first()
    #busobj=list(buses)
    return JsonResponse(bus, safe=False,content_type='application/json')