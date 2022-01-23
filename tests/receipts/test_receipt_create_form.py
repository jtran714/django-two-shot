from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from django.contrib.auth.models import User


class CreateReceiptFormTests(StaticLiveServerTestCase):
    def setUp(self):
        self.password = "abcdefg"
        self.owner = User.objects.create_user("noor", password=self.password)
        options = Options()
        options.headless = True
        self.client = webdriver.Chrome(options=options)
        self.login()
        self.url = f"{self.live_server_url}/receipts/create/"
        self.client.get(self.url)

    def test_create_form_has_vendor_field(self):
        self.client.find_element(By.ID, "id_vendor")

    def test_create_form_has_total_field(self):
        self.client.find_element(By.ID, "id_total")

    def test_create_form_has_tax_field(self):
        self.client.find_element(By.ID, "id_tax")

    def test_create_form_has_date_field(self):
        self.client.find_element(By.ID, "id_date")

    def test_create_form_has_category_field(self):
        self.client.find_element(By.ID, "id_category")

    def test_create_form_has_account_field(self):
        self.client.find_element(By.ID, "id_account")

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
