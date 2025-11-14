from selenium.webdriver.common.by import By


class MainPageLocators:
#   кнопка "Конструктор" для перехода на главную страницу конструктора бургеров
    CONSTRUCTOR_PAGE_BUTTON = (By.XPATH, "//*[text()='Конструктор']/parent::a")
#   кнопка "Лента Заказов" для перехода к ленте заказов
    ORDERS_FEED_PAGE_BUTTON = (By.XPATH, "//*[text()='Лента Заказов']/parent::a")
#   кнопка "Оформить заказ" для завершения заказа
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
#   список всех доступных ингредиентов
    LIST_OF_INGREDIENTS = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]")
#   первая булка в списке ингредиентов
    FIRST_BUN = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]")
#   первый соус в списке ингредиентов
    FIRST_SAUCE = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[2]")
#   первая начинка в списке ингредиентов
    FIRST_MAIN = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[3]")
#   cчетчик количества первого ингредиента (показывает, сколько раз добавлен)
    FIRST_INGREDIENT_COUNTER = (By.XPATH, "(//*[contains(@class, 'counter_counter__num')])[1]")
#   область конструктора, куда перетаскиваются ингредиенты
    DROP_TARGET = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
#   модальное окно с информацией о заказе
    ORDER_MODAL = (By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]")
#   номер заказа в модальном окне
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class,'title_shadow')]")
#   кнопка закрытия модального окна заказа
    CLOSE_ORDER_MODAL = (By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]//button")
#   поле для ввода пароля
    EMAIL_INPUT = (By.NAME, "name")
#   поле для ввода пароля
    PASSWORD_INPUT = (By.NAME, "Пароль")
#   кнопка "Войти" для авторизации
    LOGIN_BUTTON = (By.XPATH, "//*[text()='Войти']")