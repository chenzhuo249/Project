from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Book

# Create your views here.
def all_book(request):
    all_books = Book.objects.filter(is_active=True)
    print("-----------")
    print(all_books)
    return render(request, "bookstore/book.html", locals())


def update_book(request, book_id):
    try:
        book = Book.objects.get(id=int(book_id))
    except Exception as e:
        print("----get book is error----")
        print(e)
        return HttpResponse("您查询的数据不存在")
    if request.method == "GET":
        return render(request, "bookstore/update_book.html", locals())
    if request.method == "POST":
        # 更新数据
        price = request.POST.get('price')
        market_price = request.POST.get('m_price')

        if not price or not market_price:
            return HttpResponse('---Please give me price or market_price')
        import decimal
        # print(price)
        # print(type(price))
        # print('##########')
        # print(book.price)
        # print(type(book.price))
        # print(decimal.Decimal(price) == book.price)
        # book.market_price

        to_update = False
        if decimal.Decimal(price) != book.price:
            to_update = True
        if decimal.Decimal(market_price) != book.market_price:
            to_update = True

        if to_update:
            print('------to----update-----')
            book.price = price
            book.market_price = market_price
            # 保存
            book.save()

        return HttpResponseRedirect('/bookstore/all_book')


def delete_book(request, book_id):
    books = Book.objects.filter(id=int(book_id), is_active=True)

    if not books:
        return HttpResponse("----delete error----")

    book = books[0]
    book.is_active = False
    book.save()

    return HttpResponseRedirect(reverse("allBook"))


def index_view(request):
    return render(request, "bookstore/index1.html")
