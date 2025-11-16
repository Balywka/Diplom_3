import allure
from pages.base_page import BasePage
from locators.ingredient_modal_locators import IngredientModalLocators


class IngredientModal(BasePage):
    @allure.step("Модалка открыта?")
    def is_modal_opened(self):
        return self.is_element_visible(IngredientModalLocators.MODAL)

    @allure.step("Модалка закрыта?")
    def is_modal_closed(self):
        return not self.is_element_visible(IngredientModalLocators.MODAL)

    @allure.step("Закрыть крестиком")
    def click_close_button(self):
        self.click_element_js(IngredientModalLocators.CLOSE_BUTTON)