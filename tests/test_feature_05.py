from django.test import TestCase, Client
from django.contrib.auth.models import User
from .utils import Document
from receipts.models import Receipt


class FeatureTests(TestCase):
    fixtures = [
        "tests/fixtures/users",
        "tests/fixtures/categories",
        "tests/fixtures/accounts",
        "tests/fixtures/receipts",
    ]

    def setUp(self):
        self.client = Client()
        self.client.force_login(self.noor)
        self.response = self.client.get("/receipts/create/")
        self.content = self.response.content.decode("utf-8")
        self.document = Document()
        self.document.feed(self.content)

    @classmethod
    def setUpTestData(cls):
        cls.noor = User.objects.get(username="noor")

    def test_can_get_receipts_urlpatterns(self):
        try:
            from receipts.urls import urlpatterns  # noqa: F401
        except ModuleNotFoundError:
            self.fail("Could not find module 'receipts.urls'")
        except ImportError:
            self.fail("Could not find 'receipts.urls.urlpatterns'")

    def test_list_response_is_200(self):
        response = self.client.get("/receipts/")
        if (
            response.status_code != 302
            or not response.has_header("Location")
            or not response.headers.get("Location", "").startswith(
                "/accounts/login/"
            )
        ):
            self.assertEqual(
                response.status_code,
                200,
                msg="Did not get a 200 OK for the path receipts/",
            )

    def test_page_has_fundamental_five(self):
        response = self.client.get("/receipts/")
        if (
            response.status_code != 302
            or not response.has_header("Location")
            or not response.headers.get("Location", "").startswith(
                "/accounts/login/"
            )
        ):
            content = response.content.decode("utf-8")
            document = Document()
            document.feed(content)
            self.assertTrue(
                document.has_fundamental_five(),
                msg="The response did not have the fundamental five",
            )

    def test_div_tag_has_an_h1_tag_with_content_my_receipts(self):
        response = self.client.get("/receipts/")
        if (
            response.status_code != 302
            or not response.has_header("Location")
            or not response.headers.get("Location", "").startswith(
                "/accounts/login/"
            )
        ):
            content = response.content.decode("utf-8")
            document = Document()
            document.feed(content)
            h1 = document.select("html", "body", "main", "h1")
            self.assertIsNotNone(
                h1,
                msg="The response did not have an h1 tag as a direct child of the main",  # noqa: E501
            )
            self.assertIn(
                "Receipts",
                h1.inner_text(),
                msg="h1 did not have content 'Receipts'",
            )

    def test_div_tag_has_a_table_with_headers_name_and_number(
        self,
    ):

        response = self.client.get("/receipts/")
        if (
            response.status_code != 302
            or not response.has_header("Location")
            or not response.headers.get("Location", "").startswith(
                "/accounts/login/"
            )
        ):
            content = response.content.decode("utf-8")
            document = Document()
            document.feed(content)
            table = document.select("html", "body", "main", "table")
            self.assertIsNotNone(
                table,
                msg="The response did not have a table tag as a direct child of the main",  # noqa: E501
            )
            self.assertIn(
                "Vendor",
                table.inner_text(),
                msg="table did not have 'Vendor' header in it",
            )
            self.assertIn(
                "Total",
                table.inner_text(),
                msg="table did not have 'Total' header in it'",
            )
            self.assertIn(
                "Tax",
                table.inner_text(),
                msg="table did not have 'Tax' header in it'",
            )
            self.assertIn(
                "Date",
                table.inner_text(),
                msg="table did not have 'Date' header in it'",
            )
            self.assertIn(
                "Category",
                table.inner_text(),
                msg="table did not have 'Category' header in it'",
            )
            self.assertIn(
                "Account",
                table.inner_text(),
                msg="table did not have 'Account' header in it'",
            )

    def test_div_tag_has_a_table_tag_when_receipts_exist_with_receipt_fields(
        self,
    ):
        receipts = Receipt.objects.all()
        response = self.client.get("/receipts/")
        if (
            response.status_code != 302
            or not response.has_header("Location")
            or not response.headers.get("Location", "").startswith(
                "/accounts/login/"
            )
        ):
            content = response.content.decode("utf-8")
            document = Document()
            document.feed(content)
            table = document.select("html", "body", "main", "table")
            self.assertIsNotNone(
                table,
                msg="The response did not have a table tag as a direct child of the main",  # noqa: E501
            )
            for receipt in receipts:
                inner_text = table.inner_text()
                self.assertIn(
                    receipt.vendor,
                    inner_text,
                    msg="table did not have receipt vendor in it",
                )
                self.assertIn(
                    str(receipt.total),
                    inner_text,
                    msg="table did not have receipt total in it",
                )
                self.assertIn(
                    str(receipt.tax),
                    inner_text,
                    msg="table did not have receipt tax in it",
                )
                self.assertIn(
                    str(receipt.category.name),
                    inner_text,
                    msg="table did not have category name in it",
                )
                self.assertIn(
                    str(receipt.account.name),
                    inner_text,
                    msg="table did not have account name in it",
                )
