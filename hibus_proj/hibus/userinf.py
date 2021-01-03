from django.http import JsonResponse
from django.http import HttpRequest
from django.db.models.query import QuerySet
from hibus_proj.hibus import models



def queryUser(request):
    user_id = request.POST.get("user_id")#获取user_id
    if user_id is not None and user_id in dir():
        user_id = int(user_id)#转换为int
    # 新增
    # books = models.Book.objects.create(title="如来神掌",price=200,publish="功夫出版社",pub_date="2010-10-10")
    # 查询全部
    # books = models.Book.objects.all() 
    # 查询一个
    # books = models.Book.objects.filter(pk=5)
    # 查询不符合条件的
    # books = models.Book.objects.exclude(pk=5)
    # 查询是否存在
    # books = models.Book.objects.first().exists()
    # 修改:__in=用于读取区间
    # books = models.Book.objects.filter(pk__in=[7,8]).update(price=888)
    # userinf = models.User.objects.values().filter(pk=id)#pk是主键
    userinf = models.CustomUser.objects.values().filter(pk=user_id).first()
    return JsonResponse(userinf ,safe=False,content_type='application/json')