from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Line(models.Model):
    station_start = models.CharField(max_length=50)
    station_end = models.CharField(max_length=50)
    estimate_hour = models.IntegerField()
    estimate_minute = models.IntegerField()
    start_latitude = models.DecimalField(max_digits=10, decimal_places=7)
    start_longitude = models.DecimalField(max_digits=10, decimal_places=7)
    end_latitude = models.DecimalField(max_digits=10, decimal_places=7)
    end_longitude = models.DecimalField(max_digits=10, decimal_places=7)
    create_time = models.DateTimeField(auto_now_add=True)


class Bus(models.Model):
    line_id = models.ForeignKey(Line, on_delete=models.CASCADE)
    bus_number = models.CharField(max_length=20)
    ticket_price = models.FloatField()
    threshold_price = models.FloatField()
    current_passenger = models.IntegerField()
    threshold_passenger = models.IntegerField()
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    location = models.CharField(max_length=100)
    status = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    bus_id = models.ForeignKey(Bus, on_delete=models.CASCADE)
    line_id = models.ForeignKey(Line, on_delete=models.CASCADE)
    order_number = models.UUIDField(default=uuid.uuid4, editable=False)
    base_order_number = models.UUIDField()
    order_time = models.DateTimeField(auto_now_add=True)
    payment = models.FloatField()
    status = models.IntegerField()
    bus_start_time = models.DateTimeField()
    bus_end_time = models.DateTimeField()
    station_start = models.CharField(max_length=50)
    station_end = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_time']
