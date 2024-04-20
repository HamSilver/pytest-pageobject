from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage): 
    def __init__(self, *args, **kwargs):
        super(BasketPage, self).__init__(*args, **kwargs)

    def should_not_be_goods_title(self):
        assert self.is_element_absent(*BasketPageLocators.BASKET_TITLE), \
            "Goods table is present, but should not"
