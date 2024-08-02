from datetime import datetime
from pathlib import Path

import pytest
import pytest_html
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from backend.utils.logger import logger
from backend.utils.params import screenshot_dir,log_dir


driver = None

@pytest.fixture
def browser():
    options = Options()
    # options.add_argument('--headless')  # Optional for headless mode
    options.add_argument('--disable-gpu')  # Optional for GPU disabling

    # If using remote WebDriver, adjust as needed
    driver = webdriver.Chrome(options=options)  # Adjust this if using remote WebDriver
    yield driver
    driver.quit()


# Hook to configure pytest
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Create logs directory if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    global Logger
    Logger = logger
    Logger.info("Test execution started")


@pytest.hookimpl(tryfirst=True)
def pytest_html_results_summary(prefix, summary, postfix):
    """Add metadata to the HTML report."""
    summary.append({"Project Name": "E-commerce Automation", "Tester": "Prakhar"})

# Hook to attach logs and screenshots to the HTML report
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Attach logs and screenshots to the HTML report."""
    outcome = yield
    rep = outcome.get_result()

    now = datetime.now()
    pytest_html = item.config.pluginmanager.getplugin('html')
    extra = getattr(rep, 'extra', [])
    log_file = os.path.join(log_dir, 'logfile.log')

    # Attach logs to the HTML report
    if rep.when == "call":
        if rep.failed:
            with open(log_file, 'r') as file:
                log_content = file.read()
                if not hasattr(rep, 'extra'):
                    rep.extra = []
                rep.extra.append(pytest_html.extras.text(log_content, 'Error Logs'))
        else:
            with open(log_file, 'r') as file:
                log_content = file.read()
                if not hasattr(rep, 'extra'):
                    rep.extra = []
                logger_content = "\n".join(line for line in log_content.splitlines() if line.startswith("INFO"))
                if logger_content:
                    rep.extra.append(pytest_html.extras.text(logger_content, 'Logger Logs'))


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    """Perform final operations after all tests have finished."""
    Logger.info("Test execution completed")
    Logger.info("Screenshots and logs have been attached to the HTML report")






