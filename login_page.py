from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://saucedemo.com"


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_msg = (By.CSS_SELECTOR, "[data-test='error']")

    def abrir(self):
        self.driver.get(URL)

    def ingresar_credenciales(self, usuario, password):
        self.wait.until(EC.visibility_of_element_located(self.username_field)).send_keys(usuario)
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def obtener_error(self):
        return self.wait.until(EC.visibility_of_element_located(self.error_msg)).text


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def agregar_mochila(self):
        self.wait.until(EC.element_to_be_clickable(self.add_backpack)).click()

    def items_en_carrito(self):
        return self.wait.until(EC.presence_of_element_located(self.cart_badge)).text