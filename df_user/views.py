# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from models import *
from hashlib import sha1
from django.http import JsonResponse,HttpResponseRedirect
import user_decorator
from df_goods.models import *
from df_order.models import *
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.

def register(request):
    return render(request,'df_user/register.html')

def register_exist(request):
    username = request.GET.get('username')
    count = UserInfo.objects.filter(uname=username).count()
    return JsonResponse({'count':count})

def register_handle(request):
    # 接收用户输入
    post = request.POST
    user_name = post.get('user_name')
    pwd = post.get('pwd')
    cpwd = post.get('cpwd')
    email = post.get('email')
    # 判断密码
    if pwd != cpwd:
        return redirect('/user/register/')
    # 密码加密
    s1 = sha1()
    s1.update(pwd)
    upwd = s1.hexdigest()
    # 创建对象
    user = UserInfo()
    user.uname = user_name
    user.upwd = upwd
    user.uemail = email
    user.save()
    return redirect('/user/login/')

def login(request):
    uname = request.COOKIES.get('uname','')
    context = {'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
    return render(request,'df_user/login.html',context)
    pass

def login_hander(request):
    post = request.POST
    username = post.get('username')
    pwd = post.get('pwd')
    jizhu = post.get('jizhu',0)
    s1 = sha1()
    s1.update(pwd)
    upwd = s1.hexdigest()
    user = UserInfo.objects.filter(uname = username)
    if len(user) != 0:
        if upwd == user[0].upwd:
            url = request.COOKIES.get('url','/')
            red = HttpResponseRedirect('/goods/index/')
            if jizhu != 0:
                red.set_cookie('uname',username)
            else:
                red.set_cookie('uname','',max_age=-1)
            request.session['user_id'] = user[0].id
            request.session['user_name'] = user[0].uname
            return red
            pass
        else:
            context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1, 'username': username, 'upwd': upwd}
            return render(request, 'df_user/login.html', context)

    else:
        context = {'title':'用户登录','error_name':1,'error_pwd':0,'username':username,'upwd':upwd}
        return render(request,'df_user/login.html',context)

def loginout(request):
    request.session.flush()
    return redirect('/user/login/')
    pass

@user_decorator.login
def info(request):
    uname = request.COOKIES.get('uname','')
    if len(uname) != 0:
        user = UserInfo.objects.get(uname = uname)
        goods_ids = request.COOKIES.get('goods_ids','')
        goods_ids1 = goods_ids.split(',')
        goods_list = []
        if goods_ids != '':
            for goods_id in goods_ids1:
                goods_list.append(GoodInfo.objects.get(id=int(goods_id)))
                pass
        phone = user.phone
        uemail = user.uemail
        context = {'title':'登陆成功','uname':uname,'phone':phone,'uemail':uemail,'login':1,'goods_list':goods_list}
        return render(request, 'df_user/user_center_info.html', context)
    else:
        context = {'title':'登陆失败','uname': '', 'phone': '', 'uemail': '', 'login': 0}
        return redirect('/user/login')


@user_decorator.login
def order(request):
    uname = request.session['user_name']
    context = {'title': '用户中心','uname':uname}
    return render(request,'df_user/user_center_order.html',context)
    pass

#订单提交，由购物车跳转过来，后转到用户中心的全部订单页面
@user_decorator.login
def user_centent_order(request,pageid):
    uid = request.session.get('user_id')
    order = OrderInfo.objects.filter(user_id = uid).order_by('-oid')
    context = {
        'pagename':1,
        'title':'全部订单',
        'order':order,
        #'uname': request.session['user_name'],
    }
    return render(request,'df_user/user_center_order.html',context)


@user_decorator.login
def center_site(request):
    user = UserInfo.objects.get(id = request.session['user_id'])
    if request.method=='POST':
        post = request.POST
        user.uname = post.get('name')
        user.uaddress = post.get('address')
        user.zipCode = post.get('youbian')
        user.phone = post.get('phone')
        user.save()
    context = {'title':'用户中心','user':user}

    return render(request,'df_user/user_center_site.html',context)
    pass