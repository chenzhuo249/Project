from django.http import HttpResponse


def page1_view(request):
    html = "<h1>加油陈卓</h1>"
    return HttpResponse(html)

