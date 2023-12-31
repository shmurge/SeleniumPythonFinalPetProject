from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, '[class="btn-group"] > [class="btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '[id="content_inner"]')
    ITEMS_TO_BUY = (By.CSS_SELECTOR, '[class="basket-title hidden-xs"]')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '[id="login_form"]')
    REGISTER_FORM = (By.CSS_SELECTOR, '[id="register_form"]')
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, '[id="id_registration-email"]')
    REGISTER_PASSWORD_INPUT = (By.CSS_SELECTOR, '[id="id_registration-password1"]')
    REGISTER_CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, '[id="id_registration-password2"]')
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '[id="registration_link"]')


class ProductPageLocators():
    ITEM_NAME = (By.CSS_SELECTOR, '[class="col-sm-6 product_main"] > h1')
    ITEM_PRICE = (By.CSS_SELECTOR, '[class="price_color"]')
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-add-to-basket"]')
    ITEM_ADDED_MESSAGE = (By.CSS_SELECTOR, '[id="messages"] > [class="alert alert-safe alert-noicon alert-success  fade in"]'
                                           ':nth-child(1)')
    ITEM_NAME_IN_MESSAGE = (By.CSS_SELECTOR, '[id="messages"] > [class="alert alert-safe alert-noicon alert-success  fade in"]'
                                             ':nth-child(1) > [class="alertinner "] > strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '[class="alert alert-safe alert-noicon alert-info  fade in"]')

    #'[class="alert alert-safe alert-noicon alert-success  fade in"]:nth-child(1)'