from django.conf.urls import url
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/v1/users
    url(r"^$", views.users_view),
    url(r"^/activation$", views.active_view),

    # http://127.0.0.1:8000/v1/users/chenzhuo001/address
    url(r"^/(?P<username>\w+)/address$", views.AddressView.as_view()),

    # weibo 相关
    # http://127.0.0.1:8000/v1/users/weibo/authorization
    url(r"^/weibo/authorization$", views.author_view),

    #http://127.0.0.1:8000/v1/users/weibo/users?code=8676f54241a1085bb27f9af316f39b88
    url(r"^/weibo/users$", views.OauthWeiboView.as_view())

]