from django.http import HttpResponse
from django.shortcuts import render
import redis
from .models import User

r = redis.Redis(host="127.0.0.1", port=6379, db=0, password="123456")

# Create your views here.
def user_detail(request, user_id):
    cache_key = f"user:{user_id}"
    if r.exists(cache_key):
        data = r.hgetall(cache_key)
        new_data = {k.decode():v.decode() for k,v in data.items()}
        html = f"nickname is {new_data['nickname']}, age is {new_data['age']}"
        return HttpResponse(html)
    else:
        users = User.objects.filter(id=user_id)
        user = users[0]
        html = f"mysql nickname is {user.nickname}, age is {user.age}"
        r.hmset(cache_key, {"nickname":user.nickname, "age":user.age})
        r.expire(cache_key, 20)
        return HttpResponse(html)

def user_update(request):
    user_id = request.GET.get("user_id")
    nickname = request.GET.get("nickname")
    age = request.GET.get("age")

    try:
        user = User.objects.get(id=user_id)
    except:
        return HttpResponse("---no user---")

    # 先更新数据库
    if nickname:
        user.nickname = nickname
    if age:
        user.age = age
    user.save()

    # 后删除缓存
    cache_key = f"user:{user_id}"
    r.delete(cache_key)

    return HttpResponse(f"{user_id} 更新成功")


