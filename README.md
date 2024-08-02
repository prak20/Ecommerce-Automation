# E-commerce Automation Framework

This project provides a comprehensive frontend and backend automation framework for e-commerce websites (Amazon and Flipkart).

## Prerequisites

- Python 3.10+
- Google Chrome browser

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/prak20/Ecommerce-Automation.git
    cd ecommerce-automation
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Tests

1. Frontend Automation Tests:
    ```sh
    pytest -v --html=Result/Report/report.html backend/tests/test_frontend.py
    ```

2. Performance Tests:
    ```sh
   locust -f backend/tests/test_performance.py    
   ```

## CI/CD Integration

This project uses Jenkins for continuous integration. The workflow is defined in `.github/workflows/ci.yml`.

## Framework Overview

### Frontend Automation

- Utilizes Selenium for browser automation.
- Pages are located in `frontend/pages/` folder.
- PageUtils are located in `frontend/pageUtils/` folder.

### Backend Automation

- Utilizes pytest and Locust for Testing Scenarios.
- Pytest Test Cases are located in `backend/tests/test_frontend.py`.
- Locust Test Cases are located in `backend/tests/test_performance.py`.
- Backend Support Utils are located in `backend/utils` folder.

### Comparison

- Compares product prices from both platforms.
- Test is located inside `backend/tests/test_frontend.py`.