from selenium.webdriver.common.by import By

class BasePageLocators():
     BASKET_LINK = (By.CSS_SELECTOR, 'a.btn.btn-default[href$="/basket/"]')
     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
     USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
     ITEM = (By.CSS_SELECTOR, ".basket-items")

class MainPageLocators():
    pass

class LoginPageLocators():
     LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
     REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
     REGISTRATION_MAIL = (By.CSS_SELECTOR, "#id_registration-email[required]")
     REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1[required]")
     REGISTRATION_PASSWORD_CONFIRMATION = (By.CSS_SELECTOR, "#id_registration-password2[required]")
     REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
     SUBMIT_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
     PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
     PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main h1 + p")
     SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")
     SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alertinner strong")
     SUCCESS_MESSAGE_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages .alert-info .alertinner p strong")


