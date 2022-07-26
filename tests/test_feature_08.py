from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class FeatureTests(TestCase):
    def setUp(self):
        self.client = Client()

    def login(self):
        self.noor_credentials = {"username": "noor", "password": "1234abcd."}
        self.noor = User.objects.create_user(**self.noor_credentials)
        self.alisha = User.objects.create_user(
            username="alisha", password="1234abcd."
        )
        self.client.post(reverse("login"), self.noor_credentials)

    def test_receipts_list_is_protected(self):
        response = self.client.get("/receipts/")
        self.assertEqual(
            response.status_code,
            302,
            msg="Receipt list view is not protected",
        )
        self.assertTrue(
            response.headers.get("Location").startswith(reverse("login")),
            msg="Receipt list view did not redirect to login page",
        )
