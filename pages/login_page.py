from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://practicesoftwaretesting.com/auth/login"

    EMAIL_INPUT = (By.CSS_SELECTOR, "[data-test='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[data-test='password']")
    LOGIN_BTN = (By.CSS_SELECTOR, "[data-test='login-submit']")
    ACCOUNT_TITLE = (By.CSS_SELECTOR, "[data-test='page-title']")

    def load(self):
        self.open_url(self.URL)

    def login(self, email, password):
        self.type_text(self.EMAIL_INPUT, email)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BTN)

    def get_account_title(self):
        element = self.find_element(self.ACCOUNT_TITLE)
        return element.text
