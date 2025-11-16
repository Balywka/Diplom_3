import pytest
from driver_factory import DriverFactory
from helpers.api_helpers import StellarBurgersAPI
from data import TestData
from pages.main_page import MainPage
from pages.login_page import LoginPage


def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: маркер для смоук-тестов")

def pytest_addoption(parser):
    parser.addoption("--browser-name", default="chrome", help="Browser: chrome or firefox")
    parser.addoption("--headless", action="store_true", help="Run in headless mode")

@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser-name")
    headless = request.config.getoption("--headless")
    driver = DriverFactory.get_driver(browser_name, headless)
    driver.implicitly_wait(10)
    # Увеличиваем размер окна для Firefox
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()

@pytest.fixture
def registered_user():
    api_client = StellarBurgersAPI()
    user_data = TestData.generate_user_data()
    resp = api_client.create_user(user_data)
    token = resp.json().get("accessToken")
    yield {"data": user_data, "token": token, "api": api_client}
    if token:
        try:
            api_client.delete_user(token)
        except Exception as e:
            print(f"Ошибка при удалении пользователя: {e}")

@pytest.fixture
def authorized_user_ready(driver, registered_user):
    main = MainPage(driver)
    login = LoginPage(driver)
    main.open_main_page()
    main.wait_after_action()
    main.click_sign_in_button()
    login.login_user(registered_user["data"]["email"], registered_user["data"]["password"])
    main.wait_for_login_completion()
    yield {"main": main, "user_data": registered_user}