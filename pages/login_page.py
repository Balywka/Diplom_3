import allure
from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from urls import PAGES

class LoginPage(BasePage):
    locators = LoginLocators

    @allure.step("Открыть страницу входа")
    def open_login_page(self):
        self.open(PAGES["login"])

    @allure.step("Войти как пользователь")
    def login_user(self, email, password):
        self.input_text(self.locators.EMAIL_FIELD, email)
        self.input_text(self.locators.PASSWORD_FIELD, password)
        self.click_element_js(self.locators.ENTER_BUTTON)
        self.wait_for_url_contains("/")