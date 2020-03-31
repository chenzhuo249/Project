from django.http import HttpResponse
from django.shortcuts import render
from .models import User

# Create your views here.
def login_view(request):
    if request.method == "GET":
        return render(request, "user/login.html")
    elif request.method == "POST":
        name = request.POST.get("userName", "error")
        pwd = request.POST.get("userPwd", "error")

        return HttpResponse(f"{name}--{pwd}, 登录成功")


def login2_view(request):
    if request.method == "GET":
        return render(request, "user/login2.html")
    elif request.method == "POST":
        name = request.POST.get("userName", "error")
        pwd = request.POST.get("userPwd", "error")

        old_users = User.objects.filter(username=name)
        if old_users:
            return HttpResponse("用户名存在, 重新注册")

        return HttpResponse(f"{name}--{pwd}")