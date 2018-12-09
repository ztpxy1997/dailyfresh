# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import transaction
from django.shortcuts import render
from df_user import user_decorator
from df_order.models import OrderInfo,OrderDetailInfo
from df_user.models import UserInfo
from df_cart.models import *
from datetime import datetime
from django.http import JsonResponse
# Create your views here.
@user_decorator.login
def order(request):
    cart_ids =  request.GET.getlist('cart_id')
    cart_ids1 = [int(item) for item in cart_ids]
    user = UserInfo.objects.get(id = request.session['user_id'])
    carts = CartInfo.objects.filter(id__in = cart_ids1)
    context = {'title':'提交订单',
               'page_name':1,
               'carts':carts,
               'user':user,
               'cart_ids':','.join(cart_ids)
    }
    return render(request,'df_order/place_order.html',context)

@transaction.atomic()
def order_handle(request):
    print("进来了")
    #创建事物节点
    status = 1
    with transaction.atomic():
        tran_id = transaction.savepoint()
        try:
                post = request.POST
                orderlist = post.getlist('ids[]')
                total = post.get('totalPay')
                address = post.get('address')
                # 1、创建订单
                order = OrderInfo();
                now = datetime.now()
                uid = request.session['user_id']
                #时间戳
                order.id = '%s%d'%(now.strftime('%Y%m%d%H%M%S'),uid)
                order.user_id = uid
                order.odata = now
                order.ototal = total
                order.address = address
                order.save()
                # 2、遍历购物车
                for orderid in orderlist:
                    cart = CartInfo.objects.get(id = orderid)
                    goods = cart.goods
                    # 3、判断库存
                    print(int(goods.gstock),int(cart.num))
                    if int(goods.gstock) >= int(cart.num):
                        goods.gstock -= int(cart.num)
                        goods.save()
                        #创建详单
                        detailinfo = OrderDetailInfo()
                        detailinfo.goods_id = goods.id
                        detailinfo.order_id = order.oid
                        detailinfo.price = total
                        detailinfo.num = cart.num
                        detailinfo.save()
                        #删除购物车
                        cart.delete()
                    else:
                        transaction.savepoint_rollback(tran_id)
                        status = 2
        except Exception as e:
            print "%s"%e
            status = 3
            transaction.savepoint_rollback(tran_id)
    print(status)
    return JsonResponse({'status': status})

