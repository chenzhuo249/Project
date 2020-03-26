from django.http import HttpResponse
from django.shortcuts import render

def form_view(request):
    if request.method == "GET":
        return render(request, "test_form.html")
    if request.method == "POST":
        uname = request.POST.get("name")
        upwd = request.POST.get("pwd")
        print("------------")
        print(uname, upwd)
        return render(request, "test_form.html", locals())
