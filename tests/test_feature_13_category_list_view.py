from django.contrib.auth.models import User
from django.test import TestCase, Client

from .utils import Document
from receipts.models import ExpenseCategory


class FeatureTests(TestCase):
    fixtures = ["users", "categories", "accounts", "receipts"]

    def setUp(self):
        self.client = Client()
        self.client.force_login(self.noor)

    @classmethod
    def setUpTestData(cls):
        cls.noor = User.objects.get(username="noor")

    def test_categories_list_returns_200(self):
        path = "/receipts/categories/"
        response = self.client.get(path)
        self.assertEqual(
            response.status_code,
            200,
            msg="Did not get a 200 for categories list",
        )

    def test_categories_list_show_category_name(self):
        category = ExpenseCategory.objects.get(name="Test Category 1")
        path = "/receipts/categories/"
        response = self.client.get(path)
        document = Document()
        document.feed(response.content.decode("utf-8"))
        html = document.select("html")
        self.assertIn(
            category.name,
            html.inner_text(),
            msg="Did not find the category name on the page",
        )

    def test_categories_list_show_category_receipts_count(self):
        category = ExpenseCategory.objects.get(name="Test Category 1")
        receipts = category.receipts.all()
        path = "/receipts/categories/"
        response = self.client.get(path)
        document = Document()
        document.feed(response.content.decode("utf-8"))
        html = document.select("html")
        self.assertIn(
            str(len(receipts)),
            html.inner_text(),
            msg="Did not find the receipts count on the page",
        )
