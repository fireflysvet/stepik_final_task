from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_cart(self):
        add_to_cart_link = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add_to_cart_link.click()

    def book_name(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_NAME).text

    def book_price(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text

    def should_be_successful_add_alert(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESSFUL_ALERT), "There are no successful alert"

    def should_be_book_name_in_alert(self, name):
        successful_alerts = [i.text for i in self.browser.find_elements(*ProductPageLocators.SUCCESSFUL_ALERT)]
        assert any([name in i for i in successful_alerts]), "There is no book name in alert"

    def should_be_alert_with_cart_price(self):
        assert self.is_element_present(*ProductPageLocators.CART_ALERT), "There is no alert with cart price"

    def should_be_correct_price_in_alert(self, price):
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE_ALERT).text
        assert price == cart_price, "The cart price isn't equal to book price"

