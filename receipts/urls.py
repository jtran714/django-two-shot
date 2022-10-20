from django.urls import path
from .views import receipt_list, create_receipt


urlpatterns = [
    path("", receipt_list, name="home"),
    path("create/", create_receipt, name="create_receipt"),
]