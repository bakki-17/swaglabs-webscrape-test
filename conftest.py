import pytest
# from selenium.webdriver import Chrome
from selenium.webdriver import Chrome, Firefox
from dotenv import load_dotenv
import os


load_dotenv()
URL = os.getenv('urlPage')

class Browser:
    def __init__(self, driver):
        self.driver = driver

    def page_url(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

@pytest.fixture(scope="session")
def url():
    return URL

@pytest.fixture(params=["chrome", "firefox"], scope="session")
# @pytest.fixture(scope="session")
def browser(request, url):
    if request.param == "chrome":
        driver = Chrome()
    if request.param == "firefox":
        driver = Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()

    driver.get(url)
    browser = Browser(driver)

    yield browser
    browser.quit()

