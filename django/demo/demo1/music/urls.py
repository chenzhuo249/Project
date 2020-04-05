from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^index$", views.index_view),
    url(r"^ta$", views.test_ajax)
]