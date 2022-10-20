from django.urls import path
from .views import receipt_list


urlpatterns = [
    path("", receipt_list, name="home"),
]