import os
import time
from dotenv import load_dotenv
from pageElement.login_page import LoginPage
from pageElement.home_page import HomePage


load_dotenv()
username = os.getenv('username')
password = os.getenv('password')


def test_homepage(browser):
    #Initiate the login
    urlPage = LoginPage(browser)
    urlPage.login(username, password)
    
    #Verify homepage
    homepage = HomePage(browser)
    hompeage_Title = homepage.home_page() 
    assert 'Swag Labs' == hompeage_Title
    time.sleep(3)