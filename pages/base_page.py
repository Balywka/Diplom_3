import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть URL: {url}")
    def open(self, url):
        self.driver.get(url)
        self.wait_for_page_load()

    @allure.step("Дождаться загрузки страницы")
    def wait_for_page_load(self):
        WebDriverWait(self.driver, 2).until(lambda d: d.execute_script("return document.readyState") == "complete")

    @allure.step("Клик по элементу {locator}")
    def click_element(self, locator):
        element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(locator))
        # Для Firefox - попытка клика через JavaScript если обычный клик не работает
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Клик через JavaScript")
    def click_element_js(self, locator):
        element = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввести текст '{text}' в элемент {locator}")
    def input_text(self, locator, text):
        element = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator):
        element = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locator))
        return element.text

    @allure.step("Элемент {locator} видим?")
    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Элемент {locator} присутствует в DOM?")
    def is_element_present(self, locator):
        try:
            WebDriverWait(self.driver, 2).until(lambda driver: len(driver.find_elements(*locator)) > 0)
            return True
        except TimeoutException:
            return False

    @allure.step("Текущий URL")
    def current_url(self):
        return self.driver.current_url

    @allure.step("Ждать, пока URL содержит: {text}")
    def wait_for_url_contains(self, text):
        WebDriverWait(self.driver, 2).until(EC.url_contains(text))

    @allure.step("Перетащить элемент через JS")
    def drag_and_drop_js(self, source_locator, target_locator, js_script):
        source = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(source_locator))
        target = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(target_locator))
        self.driver.execute_script(js_script, source, target)

    @allure.step("Ждать исчезновения элемента {locator}")
    def wait_for_element_to_disappear(self, locator):
        WebDriverWait(self.driver, 2).until(EC.invisibility_of_element_located(locator))

    @allure.step("Ждать видимости элемента {locator}")
    def wait_for_element_visible(self, locator):
        return WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locator))

    @allure.step("Ждать кликабельности элемента {locator}")
    def wait_for_element_clickable(self, locator):
        return WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(locator))

    @allure.step("Закрыть модальное окно если есть")
    def close_modal_if_present(self):
        modal_overlay = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]")
        if self.is_element_visible(modal_overlay):
            # Нажимаем ESC для закрытия модального окна
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ESCAPE).perform()

    @allure.step("Ждать стабилизации страницы")
    def wait_for_page_stable(self, timeout=2):
        initial_state = self.driver.execute_script("return document.readyState")
        def page_is_stable(driver):
            current_state = driver.execute_script("return document.readyState")
            return current_state == "complete" and current_state == initial_state
        WebDriverWait(self.driver, timeout).until(page_is_stable)