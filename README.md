# AccuKnox User Management Tests

## Project Overview



### Application Under Test (AUT)

* URL: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
* Username: Admin
* Password: admin123

## Test Scenarios Automated

The following scenarios have been automated:

1. Login to OrangeHRM
2. Navigate to Admin Module
3. Add a New User
4. Search the Newly Created User
5. Edit User Details
6. Validate Updated Details
7. Delete User
8. Verify User Deletion

## Tech Stack

* Python
* Playwright




## Project Setup Steps

### 1. Clone the Repository

```bash
git clone <repository-url>
cd AccuKnox-user-management-tests
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Playwright Browsers

```bash
playwright install
```

## How to Run the Test Cases

### Run All Test Cases

```bash
pytest
```

### Run Specific Test File

```bash
pytest tests/test_add_user.py
```

### Run Tests in Headed Mode

```bash
pytest -s
```

### Generate HTML Report (Optional)

```bash
pytest --html=report.html
```

## Playwright Version Used

```text
Playwright Python v1.54.0
```

*(Update this version based on the version installed in your environment using:)*

```bash
pip show playwright
```

## Author

Mohammed Fayiz PV

QA Analyst | Software Tester
