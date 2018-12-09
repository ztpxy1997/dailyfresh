# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from  models import *

# Register your models here.
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','title']

class GoodInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id','gtitle','gpic','gprice','isDelete','gunit','gclick','gbrief','gstock','gcontent','gtype']

admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodInfo,GoodInfoAdmin)