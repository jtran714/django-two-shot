from django_webtest import WebTest
from django.contrib.auth.models import User
from receipts.models import Receipt, ExpenseCategory, Account
from datetime import datetime, timezone


class ReceiptListViewTests(WebTest):
    def setUp(self):
        self.password = "abcdefg"
        self.date = datetime.now(timezone.utc)
        self.owner = User.objects.create_user("noor", password=self.password)
        account = Account.objects.create(
            name="Test Account", number="12345", owner=self.owner
        )
        category = ExpenseCategory.objects.create(
            name="Test Category", owner=self.owner
        )
        Receipt.objects.create(
            vendor="Vendor 1",
            purchaser=self.owner,
            total=99.99,
            tax=11.11,
            date=self.date,
            category=category,
            account=account,
        )
        self.url = "/receipts/"
        self.response = self.app.get(self.url, user=self.owner)

    def test_list_contains_test_vendor(self):
        self.response.mustcontain("Vendor 1")

    def test_list_contains_total(self):
        self.response.mustcontain("99.99")

    def test_list_contains_tax(self):
        self.response.mustcontain("11.11")

    def test_list_contains_date(self):
        self.response.mustcontain(self.date.strftime("%m-%d-%Y"))

    def test_list_contains_category_name(self):
        self.response.mustcontain("Test Category")

    def test_list_contains_account_name(self):
        self.response.mustcontain("Test Account")
