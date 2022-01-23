from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from django.contrib.auth.models import User


class SignupFormTests(StaticLiveServerTestCase):
    def setUp(self):
        options = Options()
        options.headless = True
        self.client = webdriver.Chrome(options=options)
        self.url = f"{self.live_server_url}/accounts/signup/"
        self.client.get(self.url)

    def test_signup_form_has_username_field(self):
        self.client.find_element(By.ID, "id_username")

    def test_signup_form_has_password1_field(self):
        self.client.find_element(By.ID, "id_password1")

    def test_signup_form_has_password2_field(self):
        self.client.find_element(By.ID, "id_password2")

    def test_signup_form_is_post(self):
        form = self.client.find_element(By.TAG_NAME, "form")
        method = form.get_attribute("method")
        self.assertEqual(method.lower(), "post")

    def test_signup_of_unknown_person(self):
        form = self.client.find_element(By.TAG_NAME, "form")
        button = form.find_element(By.TAG_NAME, "button")
        username = self.client.find_element(By.ID, "id_username")
        password1 = self.client.find_element(By.ID, "id_password1")
        password2 = self.client.find_element(By.ID, "id_password2")
        username.send_keys("abcdefg")
        password1.send_keys("owiejfoiasje")
        password2.send_keys("owiejfoiasje")
        button.click()
        self.client.implicitly_wait(1)
        with self.assertRaises(NoSuchElementException):
            self.client.find_element(By.ID, "id_username")

    def test_signup_of_known_person(self):
        User.objects.create_user("noor", password="abcdefg")
        form = self.client.find_element(By.TAG_NAME, "form")
        button = form.find_element(By.TAG_NAME, "button")
        username = self.client.find_element(By.ID, "id_username")
        password1 = self.client.find_element(By.ID, "id_password1")
        password2 = self.client.find_element(By.ID, "id_password2")
        username.send_keys("noor")
        password1.send_keys("owiejfoiasje")
        password2.send_keys("owiejfoiasje")
        button.click()
        self.client.implicitly_wait(1)
        self.client.find_element(By.ID, "id_username")
