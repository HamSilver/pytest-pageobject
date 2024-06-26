from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage): 
    def add_product_to_basket(self):
        self.perform_add_product_to_basket()
        time.sleep(1)
        self.solve_quiz_and_get_code()
        time.sleep(2)
        self.should_names_be_same()
        self.should_prices_be_same()

    def perform_add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()

    def should_names_be_same(self):
        name_basket = self.browser.find_element(*ProductPageLocators.NAME_IN_BASKET)
        name_product = self.browser.find_element(*ProductPageLocators.NAME_IN_PRODUCT)
        assert name_basket.text == name_product.text, \
            "Product name in message should be same as name in product page"

    def should_prices_be_same(self):
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET)
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_IN_PRODUCT)
        assert price_basket.text == price_product.text, \
            "Price in message should be same as price in product page"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_disapper_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is not presented, but should be"
