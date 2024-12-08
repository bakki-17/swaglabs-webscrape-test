from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv

load_dotenv()

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def get_element(self, locator):
        try: 
            element = self.browser.driver.find_element(By.XPATH, locator)
            return element
        except NoSuchElementException:
            raise
    
    def get_elements(self, locator):
        try:
            elements = self.browser.driver.find_elements(By.XPATH, locator)
            return elements
        except NoSuchElementException:
            raise