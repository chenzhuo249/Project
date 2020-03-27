import json

from django.http import HttpResponse
from django.shortcuts import render

def index_view(request):
    if request.method == "GET":
        with open("/home/tarena/month3/django/demo/demo02/static/data/comment.data", "r") as f:
            list_cont = json.loads(f.read())[:10]
        return render(request, "index.html", locals())
    elif request.method == 'POST':
        name = request.POST.get("uname", "not found")
        cont = request.POST.get("content", "not found")
        return HttpResponse("表单提交成功")