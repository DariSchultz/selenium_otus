import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import FirefoxOptions, ChromeOptions, EdgeOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://192.168.0.26:8081")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    if browser_name == 'chrome':
        service = Service
        driver = webdriver.Chrome()
    elif browser_name == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Driver {browser_name} not supported.")
    driver.get(url)
    driver.url = url
    yield driver
    driver.quit()
