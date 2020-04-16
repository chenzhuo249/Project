from django.conf.urls import url
from . import views
urlpatterns = [
    url(r"^/celery$", views.test_celery)
]