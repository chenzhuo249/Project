"""
10100 - 10199

error
10100: 发送请求的类型不是 POST
10101: 用户名已存在
10102: 写入数据库时,用户名已存在
10103: 发送请求的类型不是 GET


"""
import base64
import hashlib
import json
import random

from django.core.mail import send_mail
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from .models import UserProfile, Address, WeiboProfile

# settings 配置文件导入方法
from django.conf import settings

from mytoken.views import make_token
from django.core.cache import cache

from .tasks import send_active_email_async

from tools.logging_decorator import logging_check

import requests



# Create your views here.
def users_view(request):
    if request.method == "POST":
        json_str = request.body
        data = json.loads(json_str)
        username = data["uname"]
        password = data["password"]
        email = data["email"]
        phone = data["phone"]

        # 检查用户名是否已经存在
        old_users = UserProfile.objects.filter(username=username)
        if old_users:
            result = {"code":10101, "error":"Your username is already existed!"}
            return JsonResponse(result)

        # 密码加密
        m = hashlib.md5()
        m.update(password.encode())

        # 将用户信息写入数据库, 注意此时有可能多个用户同时注册同一个用户名
        try:
            user = UserProfile.objects.create(username=username, password=m.hexdigest(), email=email, phone=phone)
        except Exception as e:
            print("-----create user error-----")
            print(e)
            return JsonResponse({"code":10102, "error":"Your username is already existed !"})

        # 生成令牌
        token = make_token(username)

        try:
            random_code = str(random.randint(100000, 999999))
            str_code = f"{random_code}_{username}"
            active_code = base64.urlsafe_b64encode(str_code.encode())

            #存储随机数 3天有效期
            cache.set(f"email_active_{username}", random_code, 60*60*24*3)
            verify_url = f"http://127.0.0.1:7000/dadashop/templates/active.html?code={active_code.decode()}"
            print(verify_url)

            # 发送邮件
            # send_active_email(email, verify_url) # 同步执行发邮件 会有1.2s卡顿
            send_active_email_async(email, verify_url) # 生产者消费者模型 异步执行

        except Exception as e:
            print("---active error---")
            print(e)
            pass


        return JsonResponse({"code":200, "username":username, "data":{"token":token.decode()}, "carts_count":0})



    else:
        #  非POST请求执行的语句
        return JsonResponse({"code": 10100, "error":"Please use POST !"})


def send_active_email(email_address, v_url):
    """
    发送激活邮件
    :param email_address:
    :param v_url:
    :return:
    """
    subject = "卓卓商城激活邮件"
    html_msg = f"""
    <p>尊敬的用户您好</p>
    <p>请点击此连接激活您的账户(3天内有效):</p>
    <p><a href="{v_url}" target="_blank">点击激活</a></p>
    """
    send_mail(subject=subject, html_message=html_msg, from_email=settings.EMAIL_HOST_USER, recipient_list=[email_address])


def active_view(request):
    if request.method == "GET":
        # 校验链接中的查询字符串
        # 修改用户的 is_active 值
        code = request.GET.get("code")
        if not code:
            return JsonResponse({"code":10104, "error": "not code"})

        verify_code = base64.urlsafe_b64decode(code.encode()).decode()
        # 290322_username
        random_code, username = verify_code.split("_")
        old_code = cache.get(f"email_active_{username}")
        if not old_code:
            return JsonResponse({"code":10105, "error": "The link is invalid"})
        if old_code != random_code:
            return JsonResponse({"code":10106, "error": "The link is invalid!!"})

        user = UserProfile.objects.get(username=username)
        user.is_active = True
        user.save()

        # 激活成功，删除redis中的随机码
        cache.delete(f"email_active_{username}")
        return JsonResponse({"code":200, "data": "OK"})

    else:
        #  非GET请求执行的语句
        return JsonResponse({"code": 10103, "error":"Please use GET !"})


#FBV function base view
def address_view(request):
    # 增查 /v1/users/guoxiaonao/address
    # 改删 /v1/users/guoxiaonao/address/id

    if request.method == 'GET':
        #获取用户地址
        pass
    elif request.method == 'POST':
        #创建用户地址
        pass
    elif request.method == 'PUT':
        #更新用户地址
        pass
    elif request.method == 'DELETE':
        #删除地址
        pass

#CBV  class base view
class AddressView(View):
    #特点1 对于没有定义动作方法[def get]的请求，会直接返回 405的 response
    #特点2 所有该url的请求进入到视图类 统一先走 dispatch方法

    @logging_check
    def dispatch(self, request, *args, **kwargs):
        #所有该url的请求进入到视图类 优先走该方法
        #集中的参数检查
        print('----dispatch do--')
        json_str = request.body

        if json_str:
            json_obj = json.loads(json_str)
            request.json_obj = json_obj

        return super().dispatch(request, *args, **kwargs)


    def get(self, request, username):
        """
        接收GET请求,
        :param request:
        :param username:
        :return:
        """
        user = request.myuser
        # print("------request ------")
        # print(request.myuser)

        all_address = user.address_set.filter(is_active=True)

        list_address = []
        for item in all_address:
            # print("=====item=====")
            # print(item)
            #
            dict_address = {}
            dict_address["is_default"] = item.is_default
            dict_address["tag"] = item.tag
            dict_address["receiver"] = item.receiver
            dict_address["address"] = item.address
            dict_address["receiver_mobile"] = item.receiver_mobile
            dict_address["id"] = item.user_profile.id
            list_address.append(dict_address)

        # print("---- list_address ----")
        # print(list_address)

        return JsonResponse({"code":200, "addresslist":list_address})


    def post(self, request, username):
        """
        接受POST请求，添加收货地址信息
        :param request:
        :param username: 请求用户的用户名
        :return:
        """
        data = request.json_obj
        #增加地址时, 用户的第一个地址 设置为默认地址
        receiver = data["receiver"]
        address = data["address"]
        phone = data["receiver_phone"]
        postcode = data["postcode"]
        tag = data["tag"]
        is_default = False

        try:
            user = UserProfile.objects.get(username=username)
            # print("-------id-----")
            # print(user.id)
        except Exception as e:
            print("------UserProfile get error-------")
            print(e)
            return JsonResponse({"code": 10108, "error": "no user"})

        # old_addr = user.address_set.all()
        old_addr = Address.objects.filter(user_profile=user)
        if not old_addr:
            is_default = True

        try:
            addr = Address.objects.create(user_profile=user,
                                          receiver=receiver,
                                          address=address,
                                          is_default=is_default,
                                          postcode=postcode,
                                          receiver_mobile=phone,
                                          tag=tag)
            # print(addr.__dict__)
        except Exception as e:
            print("----- create address error -----")
            print(e)
            return JsonResponse({"code":10206, "error": "info is error"})


        return JsonResponse({"code":200, "data":"地址添加成功!"})


def author_view(request):
    """
    获取微博授权地址
    :param request:
    :return:
    """

    # 将字典转换为查询字符串
    from urllib.parse import urlencode

    params = {
        "client_id": settings.WEIBO_CLIENT_ID,
        "response_type": "code",
        "redirect_uri": settings.WEIBO_REDIRECT_URI
    }

    weibo_url = "https://api.weibo.com/oauth2/authorize?"

    oauth_url = weibo_url + urlencode(params)

    return JsonResponse({"code":200, "oauth_url":oauth_url})


class OauthWeiboView(View):

    def get(self, request):
        """
        接受前端传过来的 授权码
        :param request:
        :return:
        """

        # 获取查询字符串中的 code
        code = request.GET.get("code", "not found")
        if not code:
            return JsonResponse({"code":10109, "error": "no code"})

        token_url = "https://api.weibo.com/oauth2/access_token"

        req_data = {
            "client_id": settings.WEIBO_CLIENT_ID,
            "client_secret": settings.WEIBO_CLIENT_SECRET,
            "grant_type": "authorization_code",
            "redirect_uri": settings.WEIBO_REDIRECT_URI,
            "code": code
        }

        # 按照表单提交的形式，向微博服务器发送POST请求，交换access_token
        response = requests.post(token_url, data=req_data)
        if response.status_code == 200:
            weibo_data = json.loads(response.text)
        else:
            print("weibo server error is %s"%(response.status_code))
            return JsonResponse({"code":10110, "error":"Oauth error"})

        # 如果返回数据中有 error字段, 则证明交换失败
        if weibo_data.get("error"):
            return JsonResponse({"code":10111, "error":"Oauth error!"})

        print("--------weibo data--------")
        print(weibo_data)
        # {'access_token': '2.00VRobxGAwG5tC85a91101ee0_YxsX', 'remind_in': '157679999', 'expires_in': 157679999, 'uid': '6377612237', 'isRealName': 'true'}
        weibo_uid = weibo_data["uid"]
        weibo_accsee_token = weibo_data["access_token"]


        # 查询当前微博用户是否是第一次光临
        try:
            weibo_user = WeiboProfile.objects.get(wuid=weibo_uid)
        except Exception as e:
            # 没找到数据 报错, 用户第一次来
            WeiboProfile.objects.create(access_token=weibo_accsee_token,
                                        wuid=weibo_uid)
            return JsonResponse({"code":201, "uid":weibo_uid})
        else:
            # 之前来过， 检查是否绑定过
            user = weibo_user.user_profile
            if user:
                # 证明之前绑定过 UserProfile的用户
                username = user.username
                token = make_token(username)
                return JsonResponse({"code":200, "username":username, "token": token.decode()})
            else:
                # 未绑定
                return JsonResponse({"code":201, "uid":weibo_uid})


    def post(self, request):

        data = json.loads(request.body)
        uid = data["uid"]
        username = data["username"]
        password = data["password"]
        phone = data["phone"]
        email = data["email"]

        m = hashlib.md5()
        m.update(password.encode())
        password_h = m.hexdigest()

        try:
            with transaction.atomic():
                # 创建UserProfile数据
                user = UserProfile.objects.create(username=username,
                                                  password=password_h,
                                                  email=email,
                                                  phone=phone)
                # 绑定WeiboProfile的外键
                weibo_user = WeiboProfile.objects.get(wuid=uid)
                weibo_user.user_profile = user
                weibo_user.save()
        except Exception as e:
            print("---------UserProfile create or WeiboProfile get error --------")
            print(e)
            return JsonResponse({"code":10112, "error":"Create user error"})

        token = make_token(username)
        return JsonResponse({"code":200, "username":username, "token": token.decode()})





