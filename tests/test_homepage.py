import os
import time
import pytest
from dotenv import load_dotenv
from pageElement.login_page import LoginPage
from pageElement.home_page import HomePage


load_dotenv()
username = os.getenv('username')
password = os.getenv('password')

@pytest.mark.test_id("3")
def test_homepage(browser):
    """Asserting the Title of the Login Page"""
    #Initiate the login
    try: 
        loginToApp = LoginPage(browser)
        loginToApp.login(username, password)
    except Exception as e:
        pass
    
    #Verify homepage
    homepage = HomePage(browser)
    hompeage_Title = homepage.home_page() 
    assert 'Swag Labs' == hompeage_Title
    time.sleep(3)