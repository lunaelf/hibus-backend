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
