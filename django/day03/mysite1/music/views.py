from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_view(request):
    # return HttpResponse("这是music下的首页")
    return render(request, "music/index.html")