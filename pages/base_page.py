# pages/base_page.py
from utils.wait_utils import wait_for_element_clickable
from selenium.webdriver.common.by import By

class BasePage:
    """BasePage: common actions shared across page objects."""
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        """Open specified URL in browser."""
        self.driver.get(url)

    def click(self, by, locator):
        """Click element after waiting for it to be clickable."""
        el = wait_for_element_clickable(self.driver, by, locator)
        el.click()

    def type_text(self, by, locator, text):
        """Clear input and type text."""
        el = self.driver.find_element(by, locator)
        el.clear()
        el.send_keys(text)
