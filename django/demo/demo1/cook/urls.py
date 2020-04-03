from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^tc$", views.test_cookies),
    url(r"^in$", views.index_view),
    url(r"^gc$", views.get_cookies),
    url(r"^ss$", views.set_session),
    url(r"^gs$", views.get_session),
    url(r"^ds$", views.delete_ss),
]