from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    ADD_TO_CART = (By.CLASS_NAME, 'btn-add-to-basket')
    SUCCESSFUL_ALERT = (By.CLASS_NAME, 'alert-success')
    BOOK_NAME_IN_ALERT = (By.CSS_SELECTOR, '.alert-success>div>strong')
    BOOK_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_main>p.price_color')
    CART_ALERT = (By.CSS_SELECTOR, '.alert-info')
    CART_PRICE_ALERT = (By.CSS_SELECTOR, '.alert-info>div>p>strong')