from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^all_book$", views.all_book, name="allBook"),
    url(r"^update_book/(\d*)$", views.update_book),
    url(r"^delete_book/(\d*)$", views.delete_book),
    url(r"^index$", views.index_view)
]