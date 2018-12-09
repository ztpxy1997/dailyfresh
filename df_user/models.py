# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
    ushou = models.CharField(max_length=10,default='')
    uaddress = models.CharField(max_length=100,default='')
    zipCode = models.CharField(max_length=6,default='')
    phone = models.CharField(max_length=11,default='')