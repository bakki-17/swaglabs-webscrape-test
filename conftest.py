import pytest
from selenium.webdriver import Chrome, Firefox, ChromeOptions
from dotenv import load_dotenv
import os
# from py.xml import html
from pytest_metadata.plugin import metadata_key
from datetime import datetime


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
def browser_name(request):
    return request.config.getoption("--browser_name")

@pytest.fixture(scope="session")
def url():
    return URL

# @pytest.fixture(params=["chrome", "firefox"], scope="session")
@pytest.fixture(scope="session")
def browser(url, browser_name):
    # if request.param == "chrome":
    if browser_name == "chrome":
        driver = Chrome()
    # if request.param == "firefox":
    if browser_name == "firefox":
        driver = Firefox()
    driver.implicitly_wait(4)
    driver.maximize_window()

    driver.get(url)
    browser = Browser(driver)

    yield browser
    browser.quit()

##################################################################
##################################################################
        #Implement Test Report using pytest-html#
##################################################################
##################################################################
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Driver", None)

def pytest_html_report_title(report):
    report.title = "Pytest Project of Alfred"

def pytest_configure(config):
    config.stash[metadata_key]["Environment"] = "Prod"
    config.stash[metadata_key]["Test URL"] = "https://www.saucedemo.com/"

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_header(cells):
    cells.insert(2, "<th>Test Description</th>")
    cells.insert(1, "<th>Test ID</th>")
    cells.insert(0, '<th class="sortable time" data-column-type="time">Time</th>')

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_row(report, cells):
    description = getattr(report, "description", "")
    
    cells.insert(2, f'<td>{description}</td>')
    cells.insert(1, f'<td><a href="https://reqres.in/api/users/{report._testid}">{report._testid}</a></td>')
    cells.insert(0, f'<td class="col-time">{datetime.today()}</td>')

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    outcome._result.description = item.function.__doc__
    report = outcome.get_result()
    report._testid = item.get_closest_marker("test_id").args[0]
    setattr(report, "duration_formatter", "%M:%S.%f")
    

### reporting to test <bug tracker>
@pytest.fixture(scope="session")
def testrail_ids_collection():
    return []

# Fixture to associate Test IDs with tests
@pytest.fixture
def test_id(request, testrail_ids_collection):
    test_id = request.node.get_closest_marker('test_id')
    if test_id:
        test_id_value = test_id.args[0]
        testrail_ids_collection.append(test_id_value)
        return test_id_value
    return None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Name of the browser to run tests")
    parser.addoption("--language", action="store", default="ru", help="Choose language")


