"""
10200-10299

error
10200 不是POST请求


"""
import hashlib
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from user.models import UserProfile

# Create your views here.
def tokens_view(request):
    if request.method == "POST":

        # 获取数据
        data = json.loads(request.body)
        username = data["username"]
        password = data["password"]

        #TODO 校验参数

        old_users = UserProfile.objects.filter(username=username)
        if not old_users:
            result = {"code":10201, "error":"Your username or password is wrong!"}
            return JsonResponse(result)

        user = old_users[0]
        m = hashlib.md5()
        m.update(password.encode())
        if m.hexdigest() != user.password:
            result = {"code":10202, "error":"Your username or password is wrong!"}
            return JsonResponse(result)

        # 签发token
        token = make_token(username)

        result = {"code":200, "username": username, "data":{"token":token.decode()}, "carts_count":0}
        return JsonResponse(result)

    else:
        result = {"code":10200, "error":"Please use POST!"}
        return JsonResponse(result)


def make_token(username, exp=3600*24):
    """
    生成 token 令牌， 保存用户会话状态
    :param username: str 用户名
    :param exp: int 过期时间,单位秒
    :return: 字节串
    """
    import jwt
    import time
    now = time.time()
    payload = {"username": username, "exp": now + exp}
    return jwt.encode(payload, settings.MY_JWT_TOKEN_KEY, algorithm="HS256")