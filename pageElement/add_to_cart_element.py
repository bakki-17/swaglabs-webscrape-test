from pageElement.base_page import BasePage
from locators.add_to_cart_locator import AddToCartItem
from random import randint
import random


class AddToCart(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        
        
    def select_item_to_add(self, numberOfItemToAdd=2):
        buttons = self.get_elements(AddToCartItem.Product_Item_Button)
        # validate the number of buttons to click
        countOfItemsToAdd = min(len(buttons), numberOfItemToAdd)
        random_button = randint(1, len(buttons))
        if numberOfItemToAdd == 0:
            for selectedBtn, select_one_item in enumerate(buttons, start=1):
                if selectedBtn == random_button:
                    select_one_item.click()
        else: 
            for selectItem in random.sample(buttons, countOfItemsToAdd):
                selectItem.click()
            

        self.get_element(AddToCartItem.ShoppingCartButton).click()