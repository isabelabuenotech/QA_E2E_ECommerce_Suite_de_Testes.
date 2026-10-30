import pytest
from pages.login_page import LoginPage

class TestLogin:
    def test_ct03_login_valido(self, driver):
        login_page = LoginPage(driver)
        login_page.load()

        # Utilize as credenciais de teste configuradas no ambiente
        login_page.login("customer@practicesoftwaretesting.com", "welcome01")

        titulo_pagina = login_page.get_account_title()
        assert "My account" in titulo_pagina, "O redirecionamento falhou após o login."
