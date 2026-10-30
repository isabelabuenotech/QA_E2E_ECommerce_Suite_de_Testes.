import pytest
from pages.home_page import HomePage
class TestProductSearch:
 def test_search_existing_product(self, driver):
 # 1. Arrange (Preparar)
    home_page = HomePage(driver)
    produto_alvo = "Pliers"
 # 2. Act (Agir)
    home_page.load()
    home_page.search_for_product(produto_alvo)
 # 3. Assert (Verificar)
    quantidade = home_page.get_number_of_products_displayed()
    assert quantidade > 0, f"Nenhum produto encontrado para '{produto_alvo}'"