from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from hibus_proj.hibus import views
from hibus_proj.hibus import userinf
from hibus_proj.hibus import bus
from hibus_proj.hibus import order


urlpatterns = [
    path('', views.api_root),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('lines/', views.LineList.as_view(), name='line-list'),
    path('lines/<int:pk>/', views.LineDetail.as_view(), name='line-detail'),
    path('buses/', views.BusList.as_view(), name='bus-list'),
    path('buses/<int:pk>/', views.BusDetail.as_view(), name='bus-detail'),
    path('orders/', views.OrderList.as_view(), name='order-list'),
    path('orders/<int:pk>/', views.OrderDetail.as_view(), name='order-detail'),
    
    path('userinf/', userinf.queryUser),
    path('queryorder/', order.queryOrder),
    path('saveorder/', order.saveOrder),
    path('querybus/', bus.querystatusBus),
]

urlpatterns = format_suffix_patterns(urlpatterns)
