from django.shortcuts import render

# Create your views here.
def index_view(request):
    list_img = [
        {"name":"外星人笔记本", "price":16785.00, "imgPath":"g_01.jpg"},
        {"name":"CASIO手表", "price":340.00, "imgPath":"g_02.jpg"},
        {"name":"iPhone手表", "price":3400.00, "imgPath":"g_03.jpg"},
        {"name":"华为手机", "price":8899.00, "imgPath":"g_04.jpg"},
        {"name":"VIVO手机", "price":3680.00, "imgPath":"g_05.jpg"},
        {"name":"抹茶蛋糕", "price":20.25, "imgPath":"g_06.jpg"},
        {"name":"良品铺子零食大礼包", "price":177.77, "imgPath":"g_07.jpg"},
        {"name":"卫龙辣条", "price":19.99, "imgPath":"g_08.jpg"},
        {"name":"Adidas阿迪达斯Yeezy椰子", "price":3568.00, "imgPath":"g_09.jpg"},
        {"name":"Air Jordan 1", "price":2567.00, "imgPath":"g_10.jpg"},
        {"name":"程序员必备单品", "price":1024.00, "imgPath":"g_11.jpg"},
        {"name":"YSL/杨树林", "price":520.00, "imgPath":"g_12.jpg"},
    ]
    return render(request, "indexWeb/index.html", locals())
