from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^d/(\d+)$", views.user_detail),
    url(r"^u$", views.user_update),
]