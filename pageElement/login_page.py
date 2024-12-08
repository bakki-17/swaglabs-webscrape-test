from pageElement.base_page import BasePage
from locators.login_locators import LoginLocators as loginElement

class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
    
    def login(self, username, password):
        self.get_element(loginElement.user_name_field).send_keys(username)
        self.get_element(loginElement.password_field).send_keys(password)
        self.get_element(loginElement.login_button).click()