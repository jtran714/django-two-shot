from django_webtest import WebTest
from django.contrib.auth.models import User
from receipts.models import ExpenseCategory


class CategoryListViewTests(WebTest):
    def setUp(self):
        self.password = "abcdefg"
        self.owner = User.objects.create_user("noor", password=self.password)
        ExpenseCategory.objects.create(
            name="Test Category 1", owner=self.owner
        )
        ExpenseCategory.objects.create(
            name="Test Category 2", owner=self.owner
        )
        self.url = "/receipts/categories/"
        self.response = self.app.get(self.url, user=self.owner)

    def test_list_contains_test_account(self):
        self.response.mustcontain("Test Category 1", "Test Category 2")
