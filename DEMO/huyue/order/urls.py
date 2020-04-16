from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^0$", views.order_view, name="chenzhuo")
]