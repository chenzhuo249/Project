from django.http import HttpResponse
from django.shortcuts import render
from .models import Order
# Create your views here.

def order_view(request):
    # return render(request, "order/order.html")
    # Order.objects.create(order_number="201903220002", order_time="2019/03/22", name="良品铺子", price=89.00, count=1, img_path="g_02.jpg",  total=89, status=2)
    # res = Order.objects.all()
    # return HttpResponse(res[0].name)

    return render(request, "order/order.html")