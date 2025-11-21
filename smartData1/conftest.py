import allure
import pytest
import logging
from allure_commons.types import AttachmentType
from selenium import webdriver
from io import StringIO
import os
import json
from datetime import datetime

from selenium.webdriver.chrome.options import Options

from Utilities.config_utility import ConfigUtility
import Utilities.logger_utility as log_utils

# Adding logger
log = log_utils.custom_logger(logging.INFO)

@pytest.fixture(scope='session', autouse=True)
def environment_setup():
    # current_date = datetime.now().strftime("%d-%m-%Y")
    output_dir = f"allure-results"
    create_environment_file(output_dir)
    create_executor_file(output_dir)

def create_environment_file(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, 'environment.properties'), 'w') as file:
        config_utility = ConfigUtility()
        browser = config_utility.read_configuration("basic info", "browser")
        app_url = config_utility.read_configuration("basic info", "smartData1")
        env_type = config_utility.read_configuration("basic info", "environment")
        file.write(f"Browser={browser}\n")
        file.write(f"URL={app_url}\n")
        file.write(f"Environment={env_type}\n")

def create_executor_file(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    executor_info = {
        "name": os.environ.get("EXECUTOR_NAME", ""),
        "type": os.environ.get("EXECUTOR_TYPE", ""),
        "url": os.environ.get("EXECUTOR_URL", ""),
        "buildOrder": os.environ.get("EXECUTOR_BUILD_ORDER", ""),
        "buildName": os.environ.get("EXECUTOR_BUILD_NAME", ""),
        "reportName": os.environ.get("EXECUTOR_REPORT_NAME", "")
    }
    with open(os.path.join(output_dir, 'executor.json'), 'w') as file:
        json.dump(executor_info, file)

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test", attachment_type=AttachmentType.PNG)
        log.error(f"Test failed: {item.name}")

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    if rep.failed:
        log.error(f"Test failed: {item.name}")

@pytest.fixture()
def setup_and_teardown(request):
    log.info("Setting up test...")
    setup_logs_stream = StringIO()
    setup_handler = logging.StreamHandler(setup_logs_stream)
    log.addHandler(setup_handler)

    config_utility = ConfigUtility()
    browser = config_utility.read_configuration("basic info", "browser")
    global driver
    driver = None
    if browser == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("force-device-scale-factor=0.8")  # Set zoom to 80%
        chrome_options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        log.error("Provide a valid browser name from this list chrome/firefox/edge")

    # driver.maximize_window()
    driver.execute_script("document.body.style.zoom='80%'")
    app_url = config_utility.read_configuration("basic info", "smartData1")
    driver.get(app_url)
    request.cls.driver = driver
    log.info(f"Test setup completed. Browser: {browser}, URL: {app_url}")

    yield

    allure.attach(setup_logs_stream.getvalue(), name="test_completion_logs", attachment_type=AttachmentType.TEXT)
    setup_handler.close()
    log.removeHandler(setup_handler)

    driver.quit()
    log.info("Test teardown completed.")