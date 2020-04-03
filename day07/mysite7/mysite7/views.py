import os
from time import time, sleep

from django.conf import settings
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page


@cache_page(10)
def test_cache(request):
    sleep(4)
    t1 = time()
    # return HttpResponse(f"时间t1: {t1}")
    return render(request, "test_cache.html", locals())


def test_mw(request):
    print("--test_mw do --")
    return HttpResponse("----------test mw---------")


def test_csrf(request):
    pass


def t_page(request):
    datas = ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"]
    # 初始化分页对象
    paginator = Paginator(datas, 2)

    cur_page = request.GET.get("page", 1)

    page = paginator.page(cur_page)
    return render(request, "t_page.html", locals())


def t_upload(request):
    if request.method == "GET":
        return render(request, "test_upload.html")
    elif request.method == "POST":
        file_obj = request.FILES["myfile"]
        f_path = os.path.join(settings.MEDIA_ROOT, file_obj.name)
        with open(f_path, "wb") as f:
            data = file_obj.file.read()
            f.write(data)
            return HttpResponse(f"{file_obj.name} 上传成功")


def t_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment;filename='mybook.csv'"
    all_data = [{"id":1, "title":"Java"}, {"id":2, "title":"Linux"}, {"id":3, "title":"Python3"}]
    import csv
    writer = csv.writer(response)
    writer.writerow(["id", "title"])
    for data in all_data:
        writer.writerow([data["id"], data["title"]])

    return response

    # response = HttpResponse(content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="mybook.csv"'
    # all_book = Book.objects.all()
    # writer = csv.writer(response)
    # writer.writerow(['id', 'title'])
    # for b in all_book:
    #     writer.writerow([b.id, b.title])
    #
    # return response