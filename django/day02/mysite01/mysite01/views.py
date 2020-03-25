from django.http import HttpResponse

#day01-----------
def index_view(request):
    html = "<h1 style='color: red;'>加油陈卓</h1>"
    return HttpResponse(html)

def page1_view(request):
    html = "<h1 style='color: red;'>这是1网页</h1>"
    return HttpResponse(html)

def page2_view(request):
    html = "<h1 style='color: red;'>这是2网页</h1>"
    return HttpResponse(html)

def pagen_view(request, n):
    html = "<h1 style='color: red;'>这是"+ n +"网页</h1>"
    return HttpResponse(html)

def calculate_view(request, num1, symbol, num2):
    dic = {"a":"+", "b":"-", "c":"*", "d":"/"}
    if symbol not in dic:
        html = "<h1 style='color: red;'>error: " + symbol + "运算不存在</h1>"
        html += "<h1 style='color: red;'>"+str(dic)+"</h1>"
        return HttpResponse(html)
    else:
        result = eval(num1 + dic[symbol] + num2)
        html = "<h1 style='color: red;'>" + num1 + dic[symbol] + num2 + "=" + str(result) + "</h1>"
        return HttpResponse(html)

def person_view(request, names, age):
    # print("path_info", request.path_info)
    # print("method", request.method)
    # print("encoding", request.encoding)
    # print("GET", request.GET)
    # print("COOKIES", request.COOKIES)
    # print("session", request.session)
    # print("body", request.body)
    # print("scheme", request.scheme)
    # print("get_host()", request.get_host())
    # print("request.META['REMOTE_ADDR']", request.META['REMOTE_ADDR'])
    # print(request.META)
    return HttpResponse(f"姓名:{names}, 年龄:{age}")
    # str01 = json.dumps({"name":names, "age":age})
    # return HttpResponse(content=str01, content_type="application/json", status=200)

def birthday_view(request, year, month, day):
    return HttpResponse(f"{year}年{month}月{day}日")

#day02-----------
def test_get(request):
    if request.method == "GET":
        print("============")
        # print(request.GET.getlist("a", "not found!"))
        print(request.GET.get("a", "not found!"))
        print(request.GET)
        return HttpResponse("test get is ok!")
    return HttpResponse("test get is error!")

def login(request):
    if request.method == "GET":
        html = '<form method="post" action="/test_post">姓名:<input type="text" name="uname"><input type="submit" value="登陆"></form>'
        return HttpResponse(html)
    elif request.method == "POST":
        name = request.POST.get("uname")
        print("----post----")
        print(name)
        return HttpResponse("post is ok")
    return HttpResponse("not get or post")