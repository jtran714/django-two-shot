from django_webtest import WebTest
from django.contrib.auth.models import User
from receipts.models import Receipt, ExpenseCategory, Account


class CreateReceiptFormTests(WebTest):
    def setUp(self):
        self.password = "abcdefg"
        self.owner = User.objects.create_user("noor", password=self.password)

        self.test_category = ExpenseCategory.objects.create(
            name="Test Category 2", owner=self.owner
        )
        self.test_account = Account.objects.create(
            name="Test Account 2", number="12345", owner=self.owner
        )
        self.url = "/receipts/create/"
        self.response = self.app.get(self.url, user=self.owner)
        self.form = self.response.form

    def test_create_form_has_vendor_field(self):
        self.assertIn("vendor", self.form.fields)

    def test_create_form_has_total_field(self):
        self.assertIn("total", self.form.fields)

    def test_create_form_has_tax_field(self):
        self.assertIn("tax", self.form.fields)

    def test_create_form_has_date_field(self):
        self.assertIn("date", self.form.fields)

    def test_create_form_has_category_field(self):
        self.assertIn("category", self.form.fields)

    def test_create_form_has_account_field(self):
        self.assertIn("account", self.form.fields)

    def test_create_form_is_post(self):
        self.assertEqual(self.form.method.lower(), "post")

    def test_create_receipt(self):
        self.form["vendor"] = "Test Vendor"
        self.form["total"] = "100"
        self.form["tax"] = "10"
        self.form["date"] = "1979-01-01"
        self.form["category"] = self.test_category.pk
        self.form["account"] = self.test_account.pk
        res = self.form.submit(user=self.owner)
        self.assertNotIn("form", res)
        receipt = Receipt.objects.filter(vendor="Test Vendor").get()
        self.assertEqual(receipt.vendor, "Test Vendor")
