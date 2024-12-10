import os
import time
import pytest
from dotenv import load_dotenv
from pageElement.login_page import LoginPage
from pageElement.add_to_cart_element import AddToCart

load_dotenv()
username = os.getenv("username")
password = os.getenv("password")

@pytest.mark.test_id("2")
def test_add_item_to_cart_randomly(browser):
    """Adding random Items in the Cart"""
    #initiate login
    loginToApp = LoginPage(browser)
    loginToApp.login(username, password)

    #initiate adding item to cart randomly

    addItem = AddToCart(browser)
    addItem.select_item_to_add()

    time.sleep(3)