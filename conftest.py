import pytest
from selenium.webdriver import Chrome, Firefox, ChromeOptions
from dotenv import load_dotenv
import os
from pytest_metadata.plugin import metadata_key
from datetime import datetime
from pwd import getpwuid
from os import getuid
from platform import python_version
import time

load_dotenv()
URL = os.getenv('urlPage')

class Browser:
    def __init__(self, driver):
        self.driver = driver

    def page_url(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()

@pytest.fixture(scope='class', params=['chrome', 'firefox'], ids=lambda x: 'Browser: {}'.format(x))
# @pytest.fixture(scope="session")
# @pytest.fixture(params=["chrome", "firefox"], autouse=True)
def browser(url, request):
    global browser
    if request.param == "chrome":
    # if browser_name == "chrome":
        driver = Chrome()
    if request.param == "firefox":
    # if browser_name == "firefox":
        driver = Firefox()

    driver.get(url)
    driver.implicitly_wait(4)
    driver.maximize_window()
    
    browser = Browser(driver)
    yield browser
    browser.quit()

# @pytest.fixture(scope="class", autouse=True)
# def browser_name(request):
#     return request.config.getoption("--browser_name")

@pytest.fixture(scope="class", autouse=True)
def url(request):
    # return request.config.getoption("--url")
    return URL

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store")
    parser.addoption("--url", action="store")


##################################################################
##################################################################
        #Implement Test Report using pytest-html#
##################################################################
##################################################################
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)
    metadata.pop("Base URL", None)

def pytest_html_report_title(report):
    report.title = "Pytest Project of Alfred"

def pytest_configure(config):
    username = getpwuid(getuid())[0]
    py_version = python_version()
    config._metadata = {
		"user_name": username,
		"python_version": py_version,
	}
    config.stash[metadata_key]["Environment"] = "Prod"
    config.stash[metadata_key]["Test URL"] = "https://www.saucedemo.com/"

    if not os.path.exists('test_reports'):
        os.makedirs('test_reports')
    config.option.htmlpath = 'test_reports/report_' + datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"

# Summary Section
pytest.mark.optionalhook
def pytest_html_results_summary(prefix, summary, postfix):
	prefix.extend([f'<h3>Adding prefix message</h3>'])
	prefix.extend([f'<h3>Adding prefix message</h3>'])

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