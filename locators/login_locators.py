from selenium.webdriver.common.by import By

class LoginLocators:
    # Поле для ввода email
    EMAIL_FIELD = (By.NAME, "name")
    # Поле для ввода пароля
    PASSWORD_FIELD = (By.NAME, "Пароль")
    # Кнопка "Войти"
    ENTER_BUTTON = (By.XPATH, "//*[text()='Войти']")
    # Заголовок страницы авторизации "Вход"
    LOGIN_TITLE = (By.XPATH, "//h2[text()='Вход']")