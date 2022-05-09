from django_webtest import WebTest
from django.contrib.auth.models import User
from receipts.models import Account


class CreateAccountFormTests(WebTest):
    def setUp(self):
        self.password = "abcdefg"
        self.owner = User.objects.create_user("noor", password=self.password)
        self.url = "/receipts/accounts/create/"
        self.response = self.app.get(self.url, user=self.owner)
        self.form = self.response.form

    def test_signup_form_has_name_field(self):
        self.assertIn("name", self.form.fields)

    def test_signup_form_has_number_field(self):
        self.assertIn("number", self.form.fields)

    def test_create_form_is_post(self):
        self.assertEqual(self.form.method.lower(), "post")

    def test_create_account(self):
        self.form["name"] = "test_account"
        self.form["number"] = "12345"
        res = self.form.submit()
        self.assertNotIn("form", res)
        account = Account.objects.filter(name="test_account").get()
        self.assertEqual(account.name, "test_account")
        self.assertEqual(account.number, "12345")
