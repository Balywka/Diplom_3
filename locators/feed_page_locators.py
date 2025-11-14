from selenium.webdriver.common.by import By

class FeedPageLocators:
    # Поиск заголовка "Лента заказов" на странице.
    FEED_TITLE = (By.XPATH, "//h1[contains(text(), 'Лента заказов')]")
    # Получение счетчика выполненных заказов за все время
    COUNTER_COMPLETED_FOR_ALL_TIME = (By.XPATH, "//*[text()='Выполнено за все время:']/parent::div/p[2]")
    #  Получение счетчика выполненных заказов за сегодня
    COUNTER_COMPLETED_FOR_TODAY = (By.XPATH, "//*[text()='Выполнено за сегодня:']/parent::div/p[2]")
    # Поиск всех номеров заказов в ленте
    ORDERS_NUMBERS_LIST = (By.XPATH, "//*[contains(text(), '#')]")
    #  Поиск заказов, в работе
    ORDERS_IN_PROGRESS_LIST = (By.XPATH, "//li[contains(@class, 'text_type_digits-default')]")