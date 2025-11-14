from selenium.webdriver.common.by import By

class IngredientModalLocators:
    # модальное окно
    MODAL = (By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]")
    # Поиск заголовка модального окна
    MODAL_TITLE = (By.XPATH, "//h2[contains(text(), 'Детали ингредиента')]")
    # названия ингредиента внутри модального окна
    INGREDIENT_NAME = (By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]/div/div/p")
    # Поиск кнопки закрытия модального окна
    CLOSE_BUTTON = (By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]//button")