# pytest-selenium-demo

Demo project: pytest + Selenium (Page Object Model) — Interview-ready.

## Structure
pytest-selenium-demo/
├─ README.md
├─ requirements.txt
├─ pytest.ini
├─ Jenkinsfile
├─ conftest.py
├─ tests/
│  ├─ test_login.py
│  └─ test_search.py
├─ pages/
│  ├─ base_page.py
│  └─ login_page.py
├─ utils/
│  ├─ browser_factory.py
│  ├─ wait_utils.py
│  └─ actions_utils.py
└─ resources/
   └─ testdata.json

## How to run
1. Create a virtualenv and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Run tests:
   ```bash
   pytest -q
   ```
3. Run a single test file:
   ```bash
   pytest tests/test_login.py -q -s
   ```
4. Generate HTML report (requires pytest-html):
   ```bash
   pytest --html=report.html
   ```

## Notes
- This demo uses `webdriver-manager` to download ChromeDriver automatically for local runs.
- For CI (Jenkins), set `headless` to true in conftest or use env variables.
- Intentionally simple pages; replace URLs and locators according to your AUT.


## Step 1: Run pytest and generate allure results
pytest -q --alluredir=reports

##Step 2: Serve allure report
allure serve reports


##   How to choose what goes inside:

After installing your needed packages manually (like Selenium, Pytest, etc.), just run:

pip freeze > requirements.txt

This captures your current environment versions into the file.
pip freeze > requirements.txt
