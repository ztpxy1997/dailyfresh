# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from df_cart.models import *
from django.shortcuts import render,redirect
from df_user import user_decorator
from django.http import JsonResponse

@user_decorator.login
def cart(request):
    uid = request.session['user_id']
    carts = CartInfo.objects.filter(user_id=uid)
    context={
        'title':'购物车',
        'page_name':1,
        'carts':carts
    }
    return  render(request,'df_cart/cart.html',context)

@user_decorator.login
def add(request,gid,count):
    uid = request.session['user_id']
    gid = int(gid)
    count = int(count)
    carts = CartInfo.objects.filter(user_id=uid,goods_id=gid)
    if len(carts) >= 1:
        cart = carts[0]
        cart.num = cart.num + count
    else:
        cart = CartInfo()
        cart.user_id = uid
        cart.goods_id = gid
        cart.num = count
    cart.save()
    if request.is_ajax():
        count = CartInfo.objects.filter(user_id=request.session['user_id']).count()
        return JsonResponse({'count':count})
    else:
        return redirect('/cart/')

@user_decorator.login
def edit(request,cart_id,count):
    try:
        cart = CartInfo.objects.get(pk = int(cart_id))
        count1 = cart.num = int(count)
        cart.save()
        data = {'ok':0}
    except Exception as e:
        data = {'ok':count1}
    return JsonResponse(data)

@user_decorator.login
def delete(request,cart_id):
    try:
        cart = CartInfo.objects.get(pk = int(cart_id))
        cart.delete()
        data = {'ok': 1}
    except:
        data = {'ok': 0}
    return JsonResponse(data)
