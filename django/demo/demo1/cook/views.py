from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_view(request):
    return HttpResponse("首页")

def test_cookies(request):
    res_obj = HttpResponse("cookies 测试")
    res_obj.set_cookie("uname", "chenzhuo", 300)
    # res_obj.set_cookie("user", "chenzhuo")
    # res_obj.delete_cookie("uname")
    return res_obj

def get_cookies(request):
    value = request.COOKIES.get("uname", "not found")
    return HttpResponse(f"cookies是 {value}")

def set_session(request):
    request.session["age"] = 21
    return HttpResponse("设置 session 成功")

def get_session(request):
    val = request.session.get("age", "not found")
    return HttpResponse(f"session值为 {val}")

def delete_ss(request):
    del request.session["age"]
    return HttpResponse("删除成功")