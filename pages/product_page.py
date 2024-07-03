from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESSFUL_ALERT), \
            "Success message is presented, but should not be"

    def add_to_basket(self):
        add_to_basket_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_link.click()

    def book_name(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_NAME).text

    def book_price(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text

    def should_be_successful_add_alert(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESSFUL_ALERT), "There are no successful alert"

    def should_be_book_name_in_alert(self, name):
        successful_alerts = [i.text for i in self.browser.find_elements(*ProductPageLocators.BOOK_NAME_IN_ALERT)]
        assert any([name == i for i in successful_alerts]), "There is no book name in alert"

    def should_be_alert_with_basket_price(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_ALERT), "There is no alert with basket price"

    def should_be_correct_price_in_alert(self, price):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_ALERT).text
        assert price == basket_price, "The basket price isn't equal to book price"

    def should_disappear_success_alert(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESSFUL_ALERT), \
            "Success alert isn't disappear"
