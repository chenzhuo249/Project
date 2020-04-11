"""
10100 - 10199

error
10100: 发送请求的类型不是 POST
10101: 用户名已存在
10102: 写入数据库时,用户名已存在


"""

import hashlib
import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import UserProfile

# settings 配置文件导入方法
from django.conf import settings
from mytoken.views import make_token





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
        return JsonResponse({"code":200, "username":username, "data":{"token":token.decode()}, "carts_count":0})

    else:
        #  非POST请求执行的语句
        return JsonResponse({"code": 10100, "error":"Please use POST !"})




