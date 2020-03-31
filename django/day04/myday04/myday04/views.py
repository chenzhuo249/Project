from django.http import HttpResponse
from django.shortcuts import render


def index_view(request):
    return render(request, "index.html")


def test_cookies(request):

    resp = HttpResponse("sss---")
    # resp.set_cookie("username", "chenzhuo", 10)
    res = request.COOKIES.get("username", "3333")
    print("#############3")
    print(res)
    return resp


def set_se(request):
    request.session["name"] = "chenzhuo"
    return HttpResponse("====ok=====")

def get_se(request):
    na = request.session["name"]
    return HttpResponse(f"---get-----{na}")
