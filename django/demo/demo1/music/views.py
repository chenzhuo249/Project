import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, "music/index.html")

def test_ajax(request):
    if request.method == "GET":
        return render(request, "music/ta.html")
    elif request.method == "POST":
        info = [
            {"name": "chhu", "age": "22"},
            {"name": "chen", "age": "12"},
            {"name": "huyue", "age": "13"},
                ]

        info1 = request.POST.get("age", "not found")
        print("-----------")
        print(info1)
        return HttpResponse(json.dumps(info))
    else:
        return HttpResponse("你不想看到我!")