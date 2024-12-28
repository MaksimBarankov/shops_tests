from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.SUBMIT_BUTTON)
        link.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_success_message_name(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME).text

    def get_success_message_price(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_PRICE).text

    def should_be_correct_book_name_in_message(self):
        page_name = self.get_product_name()
        alert_name = self.get_success_message_name()
        assert page_name == alert_name, "book titles don't match"

    def should_be_correct_book_price_in_message(self):
        page_price = self.get_product_price()
        message_name = self.get_success_message_price()
        assert page_price == message_name, "the prices of the books do not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"











