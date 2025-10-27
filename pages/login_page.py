# pages/login_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Locators grouped as class-level constants
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "loginBtn")

    def __init__(self, driver):
        super().__init__(driver)

    def load(self, base_url):
        """Navigate to the login page."""
        self.open(base_url + "/login")

    def login(self, username, password):
        """Perform login using provided credentials."""
        self.type_text(*self.USERNAME, text=username)
        self.type_text(*self.PASSWORD, text=password)
        self.click(*self.LOGIN_BTN)
