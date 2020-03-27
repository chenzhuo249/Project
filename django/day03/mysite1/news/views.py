from django.http import HttpResponse
from django.shortcuts import render

def index_view(repuest):
    return HttpResponse("这是news下的首页")
