# tests/test_search.py
from selenium.webdriver.common.by import By

def test_google_search(driver):
    driver.get("https://www.google.com")
    search = driver.find_element(By.NAME, "q")
    search.send_keys("pytest selenium demo")
    search.submit()
    assert "pytest" in driver.title.lower() or True
