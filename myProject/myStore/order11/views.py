import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def order_view(request):
    orders = [
        {"id":"1", "name": "外星人笔记本", "price": "16785.00", "imgPath": "g_01.jpg", "count": "2", "status":"1"},
        {"id":"2", "name": "CASIO手表", "price": "340.00", "imgPath": "g_02.jpg", "count": "2", "status":"2"},
        {"id":"3", "name": "iPhone手表", "price": "3400.00", "imgPath": "g_03.jpg", "count": "2", "status":"1"},
        {"id":"4", "name": "华为手机", "price": "8899.00", "imgPath": "g_04.jpg", "count": "1", "status":"2"},
        {"id":"5", "name": "VIVO手机", "price": "3680.00", "imgPath": "g_05.jpg", "count": "1", "status":"1"},
    ]
    # 从数据库中查询出用户所对应的所有订单 orders
    for item in orders:
        item["total"] = str(float(item["price"]) * int(item["count"]))
    if request.method == "GET":
        return render(request, "order/order.html", locals())
    elif request.method == "POST":
        info = request.POST.get("INFO", "not found")
        print("----------")
        print(info)
        if info == "all":
            return HttpResponse(json.dumps(orders))
        elif info == "unpaid":
            unpaid_orders = [order for order in orders if order["status"] == "1"]
            return HttpResponse(json.dumps(unpaid_orders))
        elif info == "over":
            over_orders = [order for order in orders if order["status"] == "2"]
            return HttpResponse(json.dumps(over_orders))
        else:
            return HttpResponse("你不会想看到我的!")

