from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^login$", views.login_view),
    url(r"^login2$", views.login2_view),
]