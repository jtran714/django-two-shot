from django.contrib.auth.models import User
from django_webtest import WebTest


class LoginFormTests(WebTest):
    def setUp(self):
        self.url = "/accounts/login/"
        self.response = self.app.get(self.url)
        self.form = self.response.form

    def test_login_form_has_username_field(self):
        self.assertIn("username", self.form.fields)

    def test_login_form_has_password_field(self):
        self.assertIn("password", self.form.fields)

    def test_login_form_is_post(self):
        self.assertEqual(self.form.method.lower(), "post")

    def test_login_of_unknown_person(self):
        self.form["username"] = "abcdefg"
        self.form["password"] = "abcdefg"
        res = self.form.submit()
        self.assertIsNotNone(res.form["username"])

    def test_login_of_known_person(self):
        User.objects.create_user("noor", password="abcdefg")
        self.form["username"] = "noor"
        self.form["password"] = "abcdefg"
        res = self.form.submit()
        self.assertNotIn("form", res)
