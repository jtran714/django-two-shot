from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from django.contrib.auth.models import User


class LoginFormTests(StaticLiveServerTestCase):
    def setUp(self):
        options = Options()
        options.headless = True
        self.client = webdriver.Chrome(options=options)
        self.url = f"{self.live_server_url}/accounts/login/"
        self.client.get(self.url)

    def test_login_form_has_username_field(self):
        self.client.find_element(By.ID, "id_username")

    def test_login_form_has_password_field(self):
        self.client.find_element(By.ID, "id_password")

    def test_login_form_is_post(self):
        form = self.client.find_element(By.TAG_NAME, "form")
        method = form.get_attribute("method")
        self.assertEqual(method.lower(), "post")

    def test_login_of_unknown_person(self):
        form = self.client.find_element(By.TAG_NAME, "form")
        button = form.find_element(By.TAG_NAME, "button")
        username = self.client.find_element(By.ID, "id_username")
        password = self.client.find_element(By.ID, "id_password")
        username.send_keys("abcdefg")
        password.send_keys("abcdefg")
        button.click()
        self.client.implicitly_wait(1)
        self.client.find_element(By.ID, "id_username")

    def test_login_of_known_person(self):
        User.objects.create_user("noor", password="abcdefg")
        form = self.client.find_element(By.TAG_NAME, "form")
        button = form.find_element(By.TAG_NAME, "button")
        username = self.client.find_element(By.ID, "id_username")
        password = self.client.find_element(By.ID, "id_password")
        username.send_keys("noor")
        password.send_keys("abcdefg")
        button.click()
        self.client.implicitly_wait(1)
        with self.assertRaises(NoSuchElementException):
            self.client.find_element(By.ID, "id_username")
