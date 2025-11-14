import allure
import re
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.login_locators import LoginLocators
from selenium.webdriver.support.ui import WebDriverWait
from urls import PAGES


class MainPage(BasePage):
    locators = MainPageLocators

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open(PAGES["main"])
        self.wait_for_main_page()
        # Закрываем возможное модальное окно в Firefox
        self.close_modal_if_present()

    @allure.step("Дождаться загрузки ингредиентов")
    def wait_for_ingredients_loaded(self):
        self.wait_for_element_visible(self.locators.LIST_OF_INGREDIENTS)

    @allure.step("Нажать кнопку 'Лента заказов'")
    def click_feed_button(self):
        # Для Firefox используем JavaScript клик
        self.click_element_js(self.locators.ORDERS_FEED_PAGE_BUTTON)

    @allure.step("Нажать кнопку 'Конструктор'")
    def click_constructor_button(self):
        self.click_element_js(self.locators.CONSTRUCTOR_PAGE_BUTTON)

    @allure.step("На главной странице?")
    def is_on_main_page(self):
        return self.is_element_visible(self.locators.CONSTRUCTOR_PAGE_BUTTON)

    @allure.step("Ждать загрузки главной страницы")
    def wait_for_main_page(self):
        self.wait_for_element_visible(self.locators.CONSTRUCTOR_PAGE_BUTTON)

    @allure.step("Кликнуть на первый ингредиент")
    def click_first_ingredient(self):
        self.click_element_js(self.locators.FIRST_BUN)

    @allure.step("Перетащить первую булку в конструктор")
    def drag_first_bun_to_constructor(self, js_script):
        self.drag_and_drop_js(self.locators.FIRST_BUN, self.locators.DROP_TARGET, js_script)

    @allure.step("Получить счетчик первого ингредиента")
    def get_first_ingredient_counter(self):
        if self.is_element_present(self.locators.FIRST_INGREDIENT_COUNTER):
            counter_text = self.get_text(self.locators.FIRST_INGREDIENT_COUNTER)
            return int(counter_text) if counter_text.isdigit() else 0
        return 0

    @allure.step("Нажать кнопку 'Войти в аккаунт'")
    def click_sign_in_button(self):
        login_btn_locator = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
        self.click_element_js(login_btn_locator)

    @allure.step("Перетащить соус в конструктор")
    def drag_first_sauce_to_constructor(self, js_script):
        self.drag_and_drop_js(self.locators.FIRST_SAUCE, self.locators.DROP_TARGET, js_script)

    @allure.step("Перетащить основной ингредиент в конструктор")
    def drag_first_main_to_constructor(self, js_script):
        self.drag_and_drop_js(self.locators.FIRST_MAIN, self.locators.DROP_TARGET, js_script)

    @allure.step("Нажать кнопку 'Оформить заказ'")
    def click_place_order_button(self):
        self.click_element_js(self.locators.PLACE_ORDER_BUTTON)

    @allure.step("Дождаться появления номера заказа")
    def wait_for_order_number(self):
        def order_number_loaded(driver):
            try:
                order_text = driver.find_element(*self.locators.ORDER_NUMBER).text
                numbers = re.findall(r'\d{6}', order_text)
                return bool(numbers)
            except:
                return False

        self.wait_for_element_visible(self.locators.ORDER_NUMBER)
        WebDriverWait(self.driver, 15).until(order_number_loaded)

    @allure.step("Получить номер заказа из модального окна")
    def get_order_id_from_modal(self):
        self.wait_for_order_number()
        order_text = self.get_text(self.locators.ORDER_NUMBER)
        numbers = re.findall(r'\d{6}', order_text)
        order_id = int(numbers[0]) if numbers else None
        assert order_id, f"Не найден 6-значный номер в '{order_text}'"
        return order_id

    @allure.step("Закрыть модальное окно заказа")
    def close_order_modal(self):
        self.click_element_js(self.locators.CLOSE_ORDER_MODAL)

    @allure.step("Модальное окно заказа закрыто?")
    def wait_for_order_modal_closed(self):
        self.wait_for_element_to_disappear(self.locators.ORDER_MODAL)

    @allure.step("Ждать модальное окно заказа")
    def wait_for_order_modal(self):
        self.wait_for_element_visible(self.locators.ORDER_MODAL)

    @allure.step("Создать заказ через UI")
    def create_order_ui(self, drag_and_drop_script):
        self.wait_for_ingredients_loaded()
        self.drag_first_bun_to_constructor(drag_and_drop_script)
        self.drag_first_sauce_to_constructor(drag_and_drop_script)
        self.drag_first_main_to_constructor(drag_and_drop_script)
        self.click_place_order_button()
        self.wait_for_order_modal()
        order_id = self.get_order_id_from_modal()
        self.close_order_modal()
        self.wait_for_order_modal_closed()
        return order_id

    @allure.step("Авторизоваться")
    def login(self, email, password):
        current_url = self.current_url()
        if "login" not in current_url:
            self.click_sign_in_button()
        self.input_text(LoginLocators.EMAIL_FIELD, email)
        self.input_text(LoginLocators.PASSWORD_FIELD, password)
        self.click_element_js(LoginLocators.ENTER_BUTTON)
        self.wait_for_url_contains("/")
        self.wait_for_element_visible(self.locators.PLACE_ORDER_BUTTON)

    @allure.step("Пользователь авторизован?")
    def is_user_logged_in(self):
        return self.is_element_present(self.locators.PLACE_ORDER_BUTTON)

    @allure.step("Ждать завершения авторизации")
    def wait_for_login_completion(self):
        self.wait_for_url_contains("/")
        self.wait_for_element_visible(self.locators.PLACE_ORDER_BUTTON)

    @allure.step("Ждать стабилизации после действия")
    def wait_after_action(self):
        self.wait_for_page_stable()