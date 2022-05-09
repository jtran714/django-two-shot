from django_webtest import WebTest
from django.contrib.auth.models import User
from receipts.models import Account


class AccountListViewTests(WebTest):
    def setUp(self):
        self.password = "abcdefg"
        self.owner = User.objects.create_user("noor", password=self.password)
        self.test_account = Account.objects.create(
            name="Test Account 1", number="12345", owner=self.owner
        )
        self.test_account2 = Account.objects.create(
            name="Test Account 2", number="12345", owner=self.owner
        )
        self.url = "/receipts/accounts/"
        self.response = self.app.get(self.url, user=self.owner)

    def test_list_contains_test_account(self):
        self.response.mustcontain("Test Account 1", "Test Account 2")
