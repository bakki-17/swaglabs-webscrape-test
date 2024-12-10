import os
import time
from dotenv import load_dotenv
from pageElement.login_page import LoginPage
from pageElement.add_to_cart_element import AddToCart

load_dotenv()
username = os.getenv("username")
password = os.getenv("password")

def test_add_item_to_cart_randomly(browser):
    #initiate login
    loginToApp = LoginPage(browser)
    loginToApp.login(username, password)

    #initiate adding item to cart randomly

    addItem = AddToCart(browser)
    addItem.select_item_to_add()

    time.sleep(5)