from django_webtest import WebTest
from django.contrib.auth.models import User
from receipts.models import ExpenseCategory


class CreateCategoryFormTests(WebTest):
    def setUp(self):
        self.password = "abcdefg"
        self.owner = User.objects.create_user("noor", password=self.password)
        self.url = "/receipts/categories/create/"
        self.response = self.app.get(self.url, user=self.owner)
        self.form = self.response.form

    def test_signup_form_has_name_field(self):
        self.assertIn("name", self.form.fields)

    def test_create_form_is_post(self):
        self.assertEqual(self.form.method.lower(), "post")

    def test_create_category(self):
        self.form["name"] = "Test Category"
        res = self.form.submit()
        self.assertNotIn("form", res)
        category = ExpenseCategory.objects.filter(name="Test Category").get()
        self.assertEqual(category.name, "Test Category")
