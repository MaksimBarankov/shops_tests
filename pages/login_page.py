from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        mail_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_MAIL)
        mail_form.send_keys(email)
        password_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        password_form.send_keys(password)
        password_form_confirmation = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRMATION)
        password_form_confirmation.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, f"URL '{self.browser.current_url}' does not contain 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"
