import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators
from urls import PAGES


class FeedPage(BasePage):
    locators = FeedPageLocators

    @allure.step("Открыть страницу ленты заказов")
    def open_feed_page(self):
        self.open(PAGES["feed"])
        self.wait_for_feed_page()

    @allure.step("На странице ленты заказов?")
    def is_on_feed_page(self):
        return self.is_element_visible(self.locators.FEED_TITLE)

    @allure.step("Получить счетчик всех заказов")
    def get_total_orders_counter(self):
        text = self.get_text(self.locators.COUNTER_COMPLETED_FOR_ALL_TIME)
        return int(text.replace(" ", ""))

    @allure.step("Получить счетчик заказов за сегодня")
    def get_today_orders_counter(self):
        text = self.get_text(self.locators.COUNTER_COMPLETED_FOR_TODAY)
        return int(text.replace(" ", ""))

    @allure.step("Ждать загрузки страницы ленты заказов")
    def wait_for_feed_page(self):
        self.wait_for_element_visible(self.locators.FEED_TITLE)

    @allure.step("Получить все номера заказов из ленты")
    def get_all_order_numbers(self):
        elements = self.driver.find_elements(*self.locators.ORDERS_NUMBERS_LIST)
        return [el.text.lstrip('#') for el in elements if '#' in el.text]

    @allure.step("Получить заказы из раздела 'В работе'")
    def get_orders_in_progress(self):
        elements = self.driver.find_elements(*self.locators.ORDERS_IN_PROGRESS_LIST)
        return [el.text for el in elements if el.text.strip()]

    @allure.step("Дождаться появления заказа в разделе 'В работе'")
    def wait_for_order_in_progress(self, order_number, timeout=10):
        expected_order = f"0{order_number}"

        def order_appeared(driver):
            try:
                orders_in_progress = self.get_orders_in_progress()
                return expected_order in orders_in_progress
            except:
                return False

        return self.wait_until(
            order_appeared,
            timeout=timeout,
            message=f"Заказ {expected_order} не появился в разделе 'В работе' за {timeout} секунд"
        )

    @allure.step("Дождаться появления заказа в ленте")
    def wait_for_order_in_feed(self, order_number, timeout=10):
        expected_order = f"0{order_number}"

        def order_in_feed(driver):
            try:
                feed_orders = self.get_all_order_numbers()
                return expected_order in feed_orders
            except:
                return False

        return self.wait_until(
            order_in_feed,
            timeout=timeout,
            message=f"Заказ {expected_order} не появился в ленте за {timeout} секунд"
        )

    @allure.step("Ждать увеличения счетчика")
    def wait_for_counter_increase(self, counter_func, initial_value, timeout=10):
        def counter_increased(driver):
            current_value = counter_func()
            return current_value > initial_value

        # Ждем увеличения счетчика
        self.wait_until(
            counter_increased,
            timeout=timeout,
            message=f"Счетчик не увеличился за {timeout} секунд. Исходное значение: {initial_value}"
        )
        return counter_func()