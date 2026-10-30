import pytest
from pages.home_page import HomePage
from pages.product_page import ProductPage

class TestCarrinho:
    def test_ct02_adicionar_carrinho(self, driver):
        home_page = HomePage(driver)
        product_page = ProductPage(driver)

        home_page.load()
        product_page.click_first_product()
        product_page.add_to_cart()

        contador_carrinho = product_page.get_cart_count()
        assert contador_carrinho >= 1, "O contador do carrinho não foi atualizado."
