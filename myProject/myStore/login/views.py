import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login_view(request):
    if request.method == "GET":
        return render(request, "login/login.html")
    elif request.method == "POST":
        name = request.POST.get("uName")
        pwd = request.POST.get("uPwd1")
        print("-----------")
        print(name, pwd)
        return HttpResponse("注册成功")