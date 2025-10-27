# utils/wait_utils.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element_clickable(driver, by, locator, timeout=15):
    """Wait until element is clickable and return it."""
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.element_to_be_clickable((by, locator)))

def wait_for_presence(driver, by, locator, timeout=15):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.presence_of_element_located((by, locator)))
