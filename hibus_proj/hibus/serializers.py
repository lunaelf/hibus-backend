from rest_framework import serializers
from django.contrib.auth.models import User
from hibus_proj.hibus.models import Line, Bus, Order, CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'is_admin']


class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line
        fields = ['id', 'station_start', 'station_end', 'estimate_hour', 'estimate_minute',
                  'start_latitude', 'start_longitude', 'start_location', 'end_latitude',
                  'end_longitude', 'end_location']


class BusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bus
        fields = ['id', 'line_id', 'bus_number', 'ticket_price', 'threshold_price',
                  'current_passenger', 'threshold_passenger', 'latitude', 'longitude',
                  'location', 'station', 'status', 'driver_phone']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'user_id', 'bus_id', 'line_id', 'order_number', 'base_order_number',
                  'order_type', 'order_time', 'passenger', 'payment', 'status', 'bus_start_time',
                  'bus_end_time', 'station_start', 'station_end']
