import allure
import pytest
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.ingredient_modal import IngredientModal


@allure.feature("Основной функционал")
class TestMainUI:

    @allure.title("Переход в 'Конструктор' по кнопке")
    def test_navigate_to_constructor(self, driver):
        main = MainPage(driver)
        feed = FeedPage(driver)
        main.open_main_page()
        main.click_feed_button()
        feed.wait_for_feed_page()
        main.click_constructor_button()
        main.wait_for_main_page()
        assert main.is_on_main_page(), "Не удалось перейти на главную страницу через конструктор"

    @allure.title("Переход в 'Ленту заказов' по кнопке")
    def test_navigate_to_feed(self, driver):
        main = MainPage(driver)
        feed = FeedPage(driver)
        main.open_main_page()
        main.click_feed_button()
        feed.wait_for_feed_page()
        assert feed.is_on_feed_page(), "Не удалось перейти на страницу ленты заказов"

    @allure.title("Открытие модального окна с деталями ингредиента")
    def test_ingredient_modal_opens(self, driver):
        main = MainPage(driver)
        modal = IngredientModal(driver)
        main.open_main_page()
        main.wait_for_ingredients_loaded()
        main.click_first_ingredient()
        assert modal.is_modal_opened(), "Модальное окно с деталями ингредиента не открылось"

    @allure.title("Закрытие модального окна с деталями ингредиента")
    def test_ingredient_modal_closes(self, driver):
        main = MainPage(driver)
        modal = IngredientModal(driver)
        main.open_main_page()
        main.wait_for_ingredients_loaded()
        main.click_first_ingredient()
        assert modal.is_modal_opened(), "Модальное окно должно быть открыто"
        modal.click_close_button()
        assert modal.is_modal_closed(), "Модальное окно не закрылось после клика на крестик"

    @allure.title("Увеличение счетчика ингредиента")
    def test_ingredient_counter_increases(self, driver):
        main = MainPage(driver)
        main.open_main_page()
        main.wait_for_ingredients_loaded()
        initial_counter = main.get_first_ingredient_counter()
        main.drag_first_bun_to_constructor()
        final_counter = main.get_first_ingredient_counter()
        assert final_counter > initial_counter, f"Счетчик не увеличился: было {initial_counter}, стало {final_counter}"