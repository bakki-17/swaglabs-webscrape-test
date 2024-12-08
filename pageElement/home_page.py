from pageElement.base_page import BasePage
from locators.homeProduct_locator import HomePageLocators as HomePageElement

class HomePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
    
    def home_page(self):
        hompeageTitle = self.get_element(HomePageElement.HomePage_Title).text
        return hompeageTitle
        
