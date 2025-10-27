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

---

🧱 1️⃣ What’s the point of using venv

👉 Command:

python -m venv venv
source venv/bin/activate   # (Windows: venv\Scripts\activate)

💡 Meaning:

A virtual environment (venv) is like a clean isolated mini-Python just for your project.

🧠 Why use it:

Imagine your system has many projects — one needs Selenium==4.10, another needs Selenium==4.20.
If you install both globally, they’ll conflict and break each other.

✅ venv solves this:

Keeps all packages local to your project in the venv/ folder

No interference with other projects

Ensures anyone who downloads your project can reproduce your exact setup



---

⚙️ Example:

# Create venv
python -m venv venv

# Activate it
source venv/bin/activate

# Install project dependencies
pip install -r requirements.txt

Now all Selenium, Pytest, Allure packages install inside your project’s venv — not system-wide.


---

📦 2️⃣ What’s the point of requirements.txt

💡 Meaning:

It’s a text file listing all the Python packages and versions needed to run your project.

📄 Example:

pytest==8.0.0
selenium==4.22.0
webdriver-manager==4.0.2
allure-pytest==2.13.2

💡 Why use it:

So that anyone (including Jenkins, teammates, or future you) can set up the exact same environment by running:

pip install -r requirements.txt

✅ No guessing, no missing dependencies!


---

🧠 How to choose what goes inside:

After installing your needed packages manually (like Selenium, Pytest, etc.), just run:

pip freeze > requirements.txt

This captures your current environment versions into the file.

Example output:

allure-pytest==2.13.2
pytest==8.0.0
selenium==4.22.0
webdriver-manager==4.0.2


---

⚙️ 3️⃣ What’s the point of pytest.ini

💡 Meaning:

pytest.ini is a configuration file that tells Pytest how to behave globally in your project.

Example from your project:

[pytest]
addopts = -ra -q --alluredir=reports
testpaths = tests
markers = smoke

Now let’s break it down 👇

Setting	Purpose

addopts = -ra -q --alluredir=reports	Adds default command-line options for pytest. <br>-ra → shows summary of skipped/failed tests <br>-q → quiet mode <br>--alluredir=reports → store allure result JSON files in reports/ folder
testpaths = tests	Tells pytest where to look for test files (so you don’t have to type pytest tests/ every time)
markers = smoke	Registers custom markers (like @pytest.mark.smoke) used for grouping or selective runs



---

🧪 Example usage:

If your pytest.ini looks like this:

[pytest]
addopts = -ra -q
testpaths = tests
markers = smoke

Then you can simply run:

pytest

✅ Pytest will:

Automatically run tests from tests/ folder

Apply the quiet mode

Recognize @pytest.mark.smoke decorators



pytest.ini → configuration file for pytest behavior

conftest.py → reusable fixtures, hooks, setup/teardown logic

requirements.txt → package dependencies list



---

🔧 How they all work together in your project:

1. venv → isolates your project environment


2. requirements.txt → installs all the required dependencies inside that venv


3. pytest.ini → configures pytest’s default behavior


4. conftest.py → provides fixtures like driver() and hooks like screenshot capture


conftest.py	Global setup → creates driver, base URL, hooks, fixtures
base_page.py	Common reusable methods for all pages (load, click, wait, type, find)
login_page.py	Child page → specific locators & actions (like login())
test_login.py	Actual test → uses page objects and fixtures

✅ super().load() → needed because you’re overriding load() to add /login
❌ super().click() → not needed because you’re not overriding click(); just calling it normally
