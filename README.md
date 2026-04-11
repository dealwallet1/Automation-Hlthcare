# Healthcare Automation Framework (Python + Playwright)

## Overview

This project is a scalable UI automation framework built using:

* Python
* Playwright
* Pytest

It follows:

* Page Object Model (POM)
* Data-driven testing
* Clean and maintainable structure
* Easily extendable for future healthcare workflows

---

## Project Structure

```
automation-healthcare/
│
├── tests/
│   ├── auth/
│   │   └── test_login.py
│   └── conftest.py
│
├── pages/
│   ├── base_page.py
│   └── login_page.py
│
├── locators/
│   └── login_locators.py
│
├── test_data/
│   └── login_data.json
│
├── utils/
│   ├── config.py
│   └── data_reader.py
│
├── core/
│   └── browser_manager.py
│
├── reports/
│
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Setup Instructions (From Scratch)

### 1. Clone Repository

```
git clone <your-repo-url>
cd automation-healthcare
```

### 2. Create Virtual Environment

```
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

### 4. Install Dependencies

```
pip install -r requirements.txt
```

### 5. Install Playwright Browsers

```
playwright install
```

---

## Running Tests

Run all tests:

```
pytest
```

Run specific file:

```
pytest tests/auth/test_login.py
```

Run specific test:

```
pytest tests/auth/test_login.py::TestLogin::test_valid_login
```

Run with detailed logs:

```
pytest -v
```

Stop on first failure:

```
pytest -x
```

Run only failed tests:

```
pytest --lf
```

---

## Reports

Generate HTML report:

```
pytest --html=reports/report.html
```

Open report:

Windows:

```
start reports/report.html
```

Mac:

```
open reports/report.html
```

---

## Login Scenarios Covered

* Valid login
* Invalid credentials
* Empty email and password
* Invalid email format
* Empty password
* Empty email

---

## Framework Features

* Page Object Model (POM)
* Data-driven testing (JSON)
* Centralized locators
* Reusable base methods
* Pytest fixtures for setup and teardown

---

## Important Notes

* Update BASE_URL in:

```
utils/config.py
```

* Avoid hardcoding data inside tests
* Always use locators from locators folder
* Do not use absolute XPath

---

## Debug Commands

Print logs in console:

```
pytest -s
```

Run in headed mode (UI visible):

```
pytest --headed
```

Run tests in parallel:

```
pip install pytest-xdist
pytest -n auto
```

---

## Future Enhancements

* Login session reuse (skip login)
* Allure reporting
* Retry for flaky tests
* API testing integration
* Database validation (ClickHouse)
* CI/CD (GitHub Actions)

---

## Author

Automation framework built for Healthcare Project
Using Python and Playwright
