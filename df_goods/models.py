# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class TypeInfo(models.Model):
    title = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.title.encode('utf-8')
    pass

class GoodInfo(models.Model):
    gtitle = models.CharField(max_length=20)
    gpic = models.ImageField(upload_to='df_goods')
    gprice = models.DecimalField(max_digits=5,decimal_places=2)
    isDelete = models.BooleanField(default=False)
    gunit = models.CharField(max_length=20,default='500g')
    gclick = models.IntegerField(default=0)
    gbrief = models.CharField(max_length=200)
    gstock = models.IntegerField(default=0)
    gcontent = HTMLField()
    gtype = models.ForeignKey(TypeInfo)
    def __str__(self):
        return self.gtitle.encode('utf-8')