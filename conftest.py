import pytest
from selenium import webdriver
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def base_url():
    return "https://aspire.atmecs.online/login"


@pytest.fixture(scope="function")
def dashboard_data():
    return {
        "email": "jenith.ravichandran@atmecs.com",
        "password": "Jenith@1234",

    }


@pytest.fixture(scope="function", autouse=True)
def browser_setup():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
