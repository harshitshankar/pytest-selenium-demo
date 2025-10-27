# conftest.py
import os
import pytest
import allure
from utils.browser_factory import create_driver

# Session-scoped fixture: config used across session
@pytest.fixture(scope="session")
def base_config():
    # central config for tests; in real projects read from env or files
    return {"base_url": "https://example.test", "headless": True}

# Function-scoped fixture: fresh browser per test (recommended)
@pytest.fixture(scope="function")
def driver(request, base_config):
    """Create and yield a webdriver instance for each test, then quit."""
    driver = create_driver(headless=base_config.get("headless", False))
    driver.implicitly_wait(5)  # small implicit wait; prefer explicit waits in test code
    yield driver
    driver.quit()

# Hook: take screenshot on failure and attach to Allure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Let pytest run the test and get the result object
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        # Try to get driver from fixtures or test class
        driver = item.funcargs.get("driver") or getattr(item.instance, "driver", None)
        if driver:
            try:
                png = driver.get_screenshot_as_png()
                allure.attach(png, name=item.name, attachment_type=allure.attachment_type.PNG)
                # Also save locally for convenience
                os.makedirs("screenshots", exist_ok=True)
                path = os.path.join("screenshots", f"{item.name}.png")
                with open(path, "wb") as f:
                    f.write(png)
                print(f"\nScreenshot saved to {path}")
            except Exception as e:
                print("Failed to capture screenshot for", item.name, e)
