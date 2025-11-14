import allure
import pytest
from pages.feed_page import FeedPage


@allure.suite('Лента заказов')
class TestOrderFeedSection:

    @allure.title('Отображение заказов пользователя в ленте')
    def test_user_orders_display_in_feed(self, driver, authorized_user_ready, drag_and_drop_js):
        main = authorized_user_ready["main"]
        feed = FeedPage(driver)
        order_id = main.create_order_ui(drag_and_drop_js)
        allure.attach(f"Создан заказ №: {order_id}", name="Номер заказа")
        main.click_feed_button()
        feed.wait_for_feed_page()
        feed.wait_for_order_in_feed(order_id)
        expected_order = f"0{order_id}"
        feed_orders = feed.get_all_order_numbers()
        assert expected_order in feed_orders, (
            f"Заказ {expected_order} не найден в ленте. "
            f"Найдены заказы: {feed_orders}")

    @allure.title('Увеличение счетчика «Выполнено за все время» после создания заказа')
    def test_total_orders_counter_increment(self, driver, authorized_user_ready, drag_and_drop_js):
        main = authorized_user_ready["main"]
        feed = FeedPage(driver)
        main.click_feed_button()
        feed.wait_for_feed_page()
        initial_counter = feed.get_total_orders_counter()
        main.click_constructor_button()
        main.wait_for_main_page()
        main.create_order_ui(drag_and_drop_js)
        main.click_feed_button()
        feed.wait_for_feed_page()
        updated_counter = feed.wait_for_counter_increase(
            feed.get_total_orders_counter, initial_counter)

        assert updated_counter > initial_counter, (
            f"Счётчик 'Выполнено за все время' не увеличился: "
            f"было {initial_counter}, стало {updated_counter}")

    @allure.title('Увеличение счетчика «Выполнено за сегодня» после создания заказа')
    def test_today_orders_counter_increment(self, driver, authorized_user_ready, drag_and_drop_js):
        main = authorized_user_ready["main"]
        feed = FeedPage(driver)
        main.click_feed_button()
        feed.wait_for_feed_page()
        initial_counter = feed.get_today_orders_counter()
        main.click_constructor_button()
        main.wait_for_main_page()
        main.create_order_ui(drag_and_drop_js)
        main.click_feed_button()
        feed.wait_for_feed_page()
        updated_counter = feed.wait_for_counter_increase(
            feed.get_today_orders_counter, initial_counter)

        assert updated_counter > initial_counter, (
            f"Счётчик 'Выполнено за сегодня' не увеличился: "
            f"было {initial_counter}, стало {updated_counter}")

    @allure.title('Появление номера заказа в разделе «В работе»')
    def test_order_number_appears_in_progress_section(self, driver, authorized_user_ready, drag_and_drop_js):
        main = authorized_user_ready["main"]
        feed = FeedPage(driver)
        order_id = main.create_order_ui(drag_and_drop_js)
        allure.attach(f"Создан заказ №: {order_id}", name="Номер заказа")
        main.click_feed_button()
        feed.wait_for_feed_page()
        feed.wait_for_order_in_progress(order_id)
        expected_order = f"0{order_id}"
        orders_in_progress = feed.get_orders_in_progress()

        assert expected_order in orders_in_progress, (
            f"Заказ {expected_order} не найден в разделе 'В работе'. "
            f"Найдены заказы: {orders_in_progress}")


@pytest.mark.smoke
@allure.suite('Лента заказов')
@allure.feature('Основные сценарии')
class TestOrderFeedSmoke:

    @allure.title('Смоук: создание заказа и проверка ленты')
    def test_smoke_order_creation_and_feed_validation(self, driver, authorized_user_ready, drag_and_drop_js):
        main = authorized_user_ready["main"]
        feed = FeedPage(driver)
        main.click_feed_button()
        feed.wait_for_feed_page()
        initial_total = feed.get_total_orders_counter()
        initial_today = feed.get_today_orders_counter()
        main.click_constructor_button()
        main.wait_for_main_page()
        order_id = main.create_order_ui(drag_and_drop_js)
        main.click_feed_button()
        feed.wait_for_feed_page()
        feed.wait_for_order_in_feed(order_id)
        updated_total = feed.wait_for_counter_increase(feed.get_total_orders_counter, initial_total)
        updated_today = feed.wait_for_counter_increase(feed.get_today_orders_counter, initial_today)
        expected_order = f"0{order_id}"
        feed_orders = feed.get_all_order_numbers()

        assert updated_total > initial_total, f"Общий счетчик не увеличился: {initial_total} → {updated_total}"
        assert updated_today > initial_today, f"Дневной счетчик не увеличился: {initial_today} → {updated_today}"
        assert expected_order in feed_orders, f"Заказ {expected_order} не отображается в ленте. Найдены: {feed_orders}"