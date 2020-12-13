from rest_framework import serializers
from django.contrib.auth.models import User
from hibus_proj.hibus.models import Line, Bus, Order


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'id', 'username']


class LineSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Line
        fields = ['url', 'id', 'station_start', 'station_end', 'estimate_hour', 'estimate_minute',
                  'start_latitude', 'start_longitude', 'start_location', 'end_latitude',
                  'end_longitude', 'end_location']


class BusSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Bus
        fields = ['url', 'id', 'line_id', 'bus_number', 'ticket_price', 'threshold_price',
                  'current_passenger', 'threshold_passenger', 'latitude', 'longitude',
                  'location', 'station', 'status', 'driver_phone']


class OrderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Order
        fields = ['url', 'id', 'user_id', 'bus_id', 'line_id', 'order_number', 'base_order_number',
                  'order_type', 'order_time', 'passenger', 'payment', 'status', 'bus_start_time',
                  'bus_end_time', 'station_start', 'station_end']
