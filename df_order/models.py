# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from df_cart.models import CartInfo
from df_user.models import UserInfo
from df_goods.models import GoodInfo
# Create your models here.
class OrderInfo(models.Model):
    oid = models.CharField(max_length=20,primary_key=True)
    user = models.ForeignKey(UserInfo)
    odata = models.DateField(auto_now=True)
    isPlay = models.BooleanField(default=False)
    ototal = models.DecimalField(max_digits=6,decimal_places=2)#总计
    oaddress = models.CharField(max_length=100)

class OrderDetailInfo(models.Model):
    goods = models.ForeignKey(GoodInfo)
    order = models.ForeignKey(OrderInfo)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    num = models.IntegerField()