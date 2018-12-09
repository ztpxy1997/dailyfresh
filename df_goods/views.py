# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from df_goods.models import *
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
def index(request):
    uname = request.session['user_name']
    if uname != '':
        login = 1
    typelist = TypeInfo.objects.all()
    type0 = typelist[0].goodinfo_set.order_by('id')[0:4]
    type0_1 = typelist[0].goodinfo_set.order_by('-gclick')[0:4]
    type1 = typelist[1].goodinfo_set.order_by('-id')[0:4]
    type1_1 = typelist[1].goodinfo_set.order_by('-gclick')[0:4]
    type2 = typelist[2].goodinfo_set.order_by('-id')[0:4]
    type2_1 = typelist[2].goodinfo_set.order_by('-gclick')[0:4]
    type3 = typelist[3].goodinfo_set.order_by('-id')[0:4]
    type3_1 = typelist[3].goodinfo_set.order_by('-gclick')[0:4]
    type4 = typelist[4].goodinfo_set.order_by('-id')[0:4]
    type4_1 = typelist[4].goodinfo_set.order_by('-gclick')[0:4]
    type5 = typelist[5].goodinfo_set.order_by('-id')[0:4]
    type5_1 = typelist[5].goodinfo_set.order_by('-gclick')[0:4]
    context = {'title':'首页','guest_cat':1,
               'uname':uname,'login':login,
               'type0':type0,'type0_1':type0_1,
               'type1':type1,'type1_1':type1_1,
               'type2':type2,'type2_1':type2_1,
               'type3':type3,'type3_1':type3_1,
               'type4':type4,'type4_1':type4_1,
               'type5':type5,'type5_1':type5_1,}
    return render(request,'df_goods/index.html',context)
    pass

def list(request,tid,pindex,sort):
    typeinfo = TypeInfo.objects.get(pk = int(tid))
    hot = typeinfo.goodinfo_set.order_by('-id')[0:2]
    if sort == '1':
        # 最新
        good_list = GoodInfo.objects.filter(gtype = int(tid)).order_by('id')
    elif sort == '2':
        # 价格
        good_list = GoodInfo.objects.filter(gtype=int(tid)).order_by('gprice')
    elif sort == '3':
        # 点击量
        good_list = GoodInfo.objects.filter(gtype=int(tid)).order_by('gclick')
    paginator = Paginator(good_list,5)
    page = paginator.page(int(pindex))  # 获取某页对应的记录
    for g in page:
        print(g)
    print(page)
    #if int(pindex) == paginator.num_pages:
        #page = paginator.page(paginator.num_pages)  # 取最后一页的记录

    context = {
        'title':typeinfo.title,
        'page':page,
        'paginator':paginator,
        'typeinfo':typeinfo,
        'sort':sort,
        'pindex':int(pindex),
        'hot':hot,
        'login':1,
        'uname':request.session['user_name'],
        'good_list':good_list,
    }
    return render(request,'df_goods/list.html',context)


def detail(request,id):
    goods = GoodInfo.objects.get(pk = int(id))
    goods.gclick = goods.gclick + 1
    goods.save()
    hot = goods.gtype.goodinfo_set.order_by('-id')[0:2]
    context = {
        'title':goods.gtitle,
        'uname':request.session['user_name'],
        'hot':hot,
        'id':id,
        'goods':goods,
        'login':1
    }
    response = render(request,'df_goods/detail.html',context)
    goods_ids = request.COOKIES.get('goods_ids','')
    goods_id = '%d'%goods.id
    if goods_ids != '':
        goods_ids1 = goods_ids.split(',')
        if goods_ids1.count(goods_id) >= 1:
            goods_ids1.remove(goods_id)
        goods_ids1.insert(0,goods_id)
        if len(goods_ids1)>=6:
            del goods_ids1[5]
        goods_ids = ','.join(goods_ids1)
    else:
        goods_ids = goods_id

    response.set_cookie('goods_ids',goods_ids)

    return response