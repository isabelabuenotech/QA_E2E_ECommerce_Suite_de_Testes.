from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    FIRST_PRODUCT = (By.CSS_SELECTOR, ".card")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='add-to-cart']")
    CART_COUNTER = (By.CSS_SELECTOR, "[data-test='cart-quantity']")

    def click_first_product(self):
        self.click(self.FIRST_PRODUCT)

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)

    def get_cart_count(self):
        element = self.find_element(self.CART_COUNTER)
        return int(element.text)
