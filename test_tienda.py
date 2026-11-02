from login_page import LoginPage


def test_login_fallido(driver):
    login = LoginPage(driver)
    login.abrir()
    login.ingresar_credenciales("locked_out_user", "secret_sauce")
    login.click_login()
    assert "locked out" in login.obtener_error()


def test_login_exitoso(driver):
    login = LoginPage(driver)
    login.abrir()
    login.ingresar_credenciales("standard_user", "secret_sauce")
    login.click_login()
    assert "inventory.html" in driver.current_url