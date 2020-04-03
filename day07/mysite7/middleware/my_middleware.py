from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

'''
class MyMw1(MiddlewareMixin):
    def process_request(self, request):
        print("这是 MyMw1 的 process_request 被调用")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("这是 MyMw1 的 process_view 被调用")

    def process_response(self, request, response):
        print("这是 MyMw1 的 process_response 被调用")
        return response

class MyMw2(MiddlewareMixin):
    def process_request(self, request):
        print("这是 MyMw2 的 process_request 被调用")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("这是 MyMw2 的 process_view 被调用")

    def process_response(self, request, response):
        print("这是 MyMw2 的 process_response 被调用")
        return response

'''


class MyMw3(MiddlewareMixin):
    count = 0
    def process_request(self, request):
        if request.META['REMOTE_ADDR'] == "127.0.0.1" and request.path_info == "/t_mw":
            MyMw3.count +=1
            if MyMw3.count > 5:
                return HttpResponse("访问次数已达到上限")
        # print(request.META['REMOTE_ADDR'])
        # print(request.path_info)
        print("这是 MyMw3 的 process_request 被调用")

