from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


class Line(models.Model):
    """
    路线表
    """
    # 起点车站名
    station_start = models.CharField(max_length=50)
    # 终点车站名
    station_end = models.CharField(max_length=50)
    # 预计时间，小时
    estimate_hour = models.PositiveIntegerField()
    # 预计时间，分钟
    estimate_minute = models.PositiveIntegerField()
    # 起点车站，维度
    start_latitude = models.DecimalField(
        max_digits=10, decimal_places=7, null=True)
    # 起点车站，经度
    start_longitude = models.DecimalField(
        max_digits=10, decimal_places=7, null=True)
    # 起点车站，位置
    start_location = models.CharField(max_length=200, default='')
    # 终点车站，维度
    end_latitude = models.DecimalField(
        max_digits=10, decimal_places=7, null=True)
    # 终点车站，经度
    end_longitude = models.DecimalField(
        max_digits=10, decimal_places=7, null=True)
    # 终点车站，位置
    end_location = models.CharField(max_length=200, default='')
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)


class Bus(models.Model):
    """
    客车表
    """
    # 路线 id
    line_id = models.ForeignKey(Line, on_delete=models.CASCADE)
    # 车牌号
    bus_number = models.CharField(max_length=20, unique=True)
    # 初始票价
    ticket_price = models.DecimalField(max_digits=20, decimal_places=2)
    # 票价阀值，用来计算拼单价格
    threshold_price = models.DecimalField(max_digits=20, decimal_places=2)
    # 当前乘客人数
    current_passenger = models.PositiveIntegerField(default=0)
    # 最大乘客人数
    threshold_passenger = models.PositiveIntegerField()
    # 维度
    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True)
    # 经度
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True)
    # 位置
    location = models.CharField(max_length=200, default='')
    # 当前所在车站
    station = models.CharField(max_length=50)
    # 客车状态，[0=空闲, 1=已派单, 2=行程中]
    status = models.IntegerField(default=0)
    # 司机手机号
    driver_phone = models.IntegerField()
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    """ 
    订单表
    """
    # 用户 id
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # 客车 id
    bus_id = models.ForeignKey(Bus, on_delete=models.CASCADE)
    # 路线 id
    line_id = models.ForeignKey(Line, on_delete=models.CASCADE)
    # 订单号
    order_number = models.UUIDField()
    # 上一级订单号，用来确定是否为拼单
    base_order_number = models.UUIDField()
    # 订单类型，[0=客车定制, 1=客车拼单]
    order_type = models.IntegerField()
    # 下单时间
    order_time = models.DateTimeField(auto_now_add=True)
    # 乘客人数
    passenger = models.PositiveIntegerField(default=1)
    # 支付金额
    payment = models.DecimalField(max_digits=20, decimal_places=2)
    # 订单状态，[0=已下单, 1=已完成]
    status = models.IntegerField(default=0)
    # 客车预计发车时间
    bus_start_time = models.DateTimeField()
    # 客车预计到达时间
    bus_end_time = models.DateTimeField()
    # 起点车站名
    station_start = models.CharField(max_length=50)
    # 终点车站名
    station_end = models.CharField(max_length=50)
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True)
