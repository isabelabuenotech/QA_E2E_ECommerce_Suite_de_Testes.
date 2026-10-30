from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class HomePage(BasePage):
 URL = "https://practicesoftwaretesting.com/"
 # Locators (Tuplas)
 SEARCH_INPUT = (By.CSS_SELECTOR, "[data-test='search-query']")
 SEARCH_BUTTON = (By.CSS_SELECTOR, "[data-test='search-submit']")
 PRODUCT_CARDS = (By.CSS_SELECTOR, ".card")
 def __init__(self, driver):
    super().__init__(driver)
 def load(self):
    self.open_url(self.URL)
 def search_for_product(self, product_name):
    self.type_text(self.SEARCH_INPUT, product_name)
    self.click(self.SEARCH_BUTTON)
 def get_number_of_products_displayed(self):
 # Espera carregar os cards e retorna a contagem
    self.find_element(self.PRODUCT_CARDS)
    elements = self.driver.find_elements(*self.PRODUCT_CARDS)
    return len(elements)