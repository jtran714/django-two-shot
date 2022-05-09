from django_webtest import WebTest
from django.contrib.auth.models import User
from django.conf import settings


class SignupFormTests(WebTest):
    def setUp(self):
        self.url = "/accounts/signup/"
        self.response = self.app.get(self.url)
        self.form = self.response.form

    def test_signup_form_has_username_field(self):
        self.assertIn("username", self.form.fields)

    def test_signup_form_has_password1_field(self):
        self.assertIn("password1", self.form.fields)

    def test_signup_form_has_password2_field(self):
        self.assertIn("password2", self.form.fields)

    def test_signup_form_is_post(self):
        self.assertEqual(self.form.method.lower(), "post")

    def test_signup_of_unknown_person(self):
        # This is needed because WebTest has it's own auth backend for testing
        # authenticated routes. This interferes with testing the signup form.
        # So we backup the original methods and restore them after this test
        original_auth_backends = settings.AUTHENTICATION_BACKENDS
        settings.AUTHENTICATION_BACKENDS = [
            "django.contrib.auth.backends.ModelBackend"
        ]

        self.form["username"] = "abcdefg"
        self.form["password1"] = "owiefoiasje"
        self.form["password2"] = "owiefoiasje"
        res = self.form.submit()
        self.assertNotIn("form", res)
        settings.AUTHENTICATION_BACKENDS = original_auth_backends

    def test_signup_of_known_person(self):
        User.objects.create_user("noor", password="abcdefg")
        self.form["username"] = "noor"
        self.form["password1"] = "owiejfoiasje"
        self.form["password2"] = "owiejfoiasje"
        res = self.form.submit()
        self.assertIn("form", res)
        self.assertIn("username", res.form.fields)
