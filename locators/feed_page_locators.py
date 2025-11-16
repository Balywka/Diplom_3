from selenium.webdriver.common.by import By

class FeedPageLocators:
    # Поиск заголовка "Лента заказов" на странице.
    FEED_TITLE = (By.XPATH, "//h1[contains(text(), 'Лента заказов')]")
    # Получение счетчика выполненных заказов за все время
    COUNTER_COMPLETED_FOR_ALL_TIME = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    # Получение счетчика выполненных заказов за сегодня
    COUNTER_COMPLETED_FOR_TODAY = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    # Поиск всех номеров заказов в ленте
    ORDERS_NUMBERS_LIST = (By.XPATH, "//*[contains(@class, 'OrderHistory_textBox__')]//p[contains(@class, 'digits-default')]")
    # Поиск заказов, в работе
    ORDERS_IN_PROGRESS_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady__')]//li")