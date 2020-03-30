# 在应用app中的admin.py中导入注册要管理的模型models类
from django.contrib import admin
from .models import Book, Author



class BookManager(admin.ModelAdmin):
    # 控制哪些字段会显示在Admin 的修改列表页面中
    list_display = ["id", "title", "price", "pub", "is_active"]

    # 控制list_display中的字段是否应该链接到对象的“更改”页面
    list_display_links = ["title"]

    # 设置激活Admin 修改列表页面右侧栏中的过滤器
    list_filter = ["pub", "is_active"]

    # 设置启用Admin 更改列表页面上的搜索框
    search_fields = ["title"]

    # 设置为模型上的字段名称列表，这将允许在更改列表页面上进行编辑
    list_editable = ["price", "is_active"]

admin.site.register(Book, BookManager)


class AuthorManager(admin.ModelAdmin):
    list_display = ["id", "name", "age", "email"]
    list_display_links = ["name"]
    list_filter = ["age"]
    search_fields = ["name"]
    list_editable = ["age", "email"]

admin.site.register(Author, AuthorManager)
