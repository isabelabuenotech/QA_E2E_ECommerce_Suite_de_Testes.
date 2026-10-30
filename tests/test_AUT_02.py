import pytest
from pages.home_page import HomePage

class TestBuscaProduto:
    def test_ct01_busca_produto(self, driver):
        home_page = HomePage(driver)
        home_page.load()
        home_page.search_for_product("Pliers")

        quantidade = home_page.get_number_of_products_displayed()
        assert quantidade > 0, "Nenhum produto foi retornado na busca."
