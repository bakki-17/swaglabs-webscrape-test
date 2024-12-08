from pageElement.base_page import BasePage
from locators.add_to_cart_locator import AddToCartItem
from random import randint

class AddToCart(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def select_item_to_add(self):
        # returns an integer number between 1 and the number of buttons
        buttons = self.get_elements(AddToCartItem.Product_Item_Button)
        # returns an integer number between 1 and the number of buttons
        random_button = randint(1, len(buttons))
        for button_number, selectItem in enumerate(buttons, start=1):
            if button_number == random_button:
                selectItem.click()
                break
            else:
                pass
        # try:
        #     items = self.get_elements(AddToCartItem.Product_Item_Button)
        #     randomButton = randint(0, len(items))
        #     items[randomButton].click()
        # except IndexError:
        #     randomButton = 'null' 
        
        # try:
        #     items1 = self.get_elements(AddToCartItem.Product_Item_Button)
        #     randomButton1 = randint(0, len(items1))
        #     items1[randomButton1].click()
        # except IndexError:
        #     randomButton1 = 'null'

        #Click all buttons
        # for selectItem in self.get_elements(AddToCartItem.Product_Item_Button):
        #     selectItem.click()

        self.get_element(AddToCartItem.ShoppingCartButton).click()