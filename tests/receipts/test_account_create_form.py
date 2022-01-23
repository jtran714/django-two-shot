from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from django.contrib.auth.models import User


class CreateAccountFormTests(StaticLiveServerTestCase):
    def setUp(self):
        self.password = "abcdefg"
        self.owner = User.objects.create_user("noor", password=self.password)
        options = Options()
        options.headless = True
        self.client = webdriver.Chrome(options=options)
        self.login()
        self.url = f"{self.live_server_url}/receipts/accounts/create/"
        self.client.get(self.url)

    def test_signup_form_has_name_field(self):
        self.client.find_element(By.ID, "id_name")

    def test_signup_form_has_number_field(self):
        self.client.find_element(By.ID, "id_number")

    def test_create_form_is_post(self):
        form = self.client.find_element(By.TAG_NAME, "form")
        method = form.get_attribute("method")
        self.assertEqual(method.lower(), "post")

    def login(self):
        self.client.get(f"{self.live_server_url}/accounts/login/")
        form = self.client.find_element(By.TAG_NAME, "form")
        button = form.find_element(By.TAG_NAME, "button")
        username = self.client.find_element(By.ID, "id_username")
        password = self.client.find_element(By.ID, "id_password")
        username.send_keys(self.owner.username)
        password.send_keys(self.password)
        button.click()
