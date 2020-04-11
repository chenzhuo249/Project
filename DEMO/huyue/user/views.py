import json

from django.http import HttpResponse
from django.shortcuts import render
from .models import Goods

# Create your views here.
def user_view(request):
    Goods.objects.create(name="咖啡", count=3, price=19.99)
    res = Goods.objects.all()
    return render(request, "user/user.html", locals())
    # result = [item.name for item in res]
    # return HttpResponse("--".join(result))



