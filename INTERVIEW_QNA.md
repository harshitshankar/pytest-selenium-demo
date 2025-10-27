# Interview QnA: Pytest + Selenium (Short Answers)

Q: What is a fixture in pytest?
A: A fixture is a setup/teardown helper which provides test functions with resources (like drivers). Defined with @pytest.fixture.

Q: What are fixture scopes?
A: function, class, module, package, session — they control lifetime of fixture.

Q: Why use Page Object Model (POM)?
A: POM separates test logic from UI locators/actions. Each page is a class with locators and methods, improving maintainability.

Q: Difference between implicit and explicit wait?
A: Implicit wait is a global find_element polling. Explicit wait (WebDriverWait + ExpectedConditions) waits for specific conditions.

Q: How to capture screenshot on failure?
A: Use pytest hook pytest_runtest_makereport to detect failure and call driver.save_screenshot().

Q: How to parallelize tests?
A: Use pytest-xdist: pytest -n <workers>. Ensure tests are independent and avoid sharing stateful resources.

Q: What is Allure?
A: Allure is an advanced reporting tool; generate results with pytest --alluredir and view with allure serve.

Q: How to handle flaky tests?
A: Use reliable locators, explicit waits, avoid time.sleep, isolate tests, use retries carefully.
