from django.urls import path

from receipts.views import (
    AccountCreateView,
    AccountListView,
    ExpenseCategoryCreateView,
    ExpenseCategoryListView,
    ReceiptCreateView,
    ReceiptListView,
)


urlpatterns = [
    path("", ReceiptListView.as_view(), name="home"),
    path("create/", ReceiptCreateView.as_view(), name="create_receipt"),
    path("accounts/", AccountListView.as_view(), name="list_accounts"),
    path(
        "accounts/create/",
        AccountCreateView.as_view(),
        name="create_account",
    ),
    path(
        "categories/",
        ExpenseCategoryListView.as_view(),
        name="list_categories",
    ),
    path(
        "categories/create/",
        ExpenseCategoryCreateView.as_view(),
        name="create_category",
    ),
]
