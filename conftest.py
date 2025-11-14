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
def api_client():
    return StellarBurgersAPI()


@pytest.fixture
def registered_user(api_client):
    user_data = TestData.generate_user_data()
    resp = api_client.create_user(user_data)
    token = resp.json().get("accessToken")
    yield {"data": user_data, "token": token, "api": api_client}
    if token:
        api_client.delete_user(token)


@pytest.fixture
def drag_and_drop_js():
    return """
    function simulateDragDrop(sourceNode, destinationNode) {
        function createEvent(type) {
            const event = new MouseEvent(type, {bubbles: true, cancelable: true});
            if (type.includes('drag')) {
                event.dataTransfer = {setData: function () {}, setDragImage: function () {}};
            }
            return event;
        }

        sourceNode.dispatchEvent(createEvent('dragstart'));
        destinationNode.dispatchEvent(createEvent('dragover'));
        destinationNode.dispatchEvent(createEvent('drop'));
        sourceNode.dispatchEvent(createEvent('dragend'));
        return true;
    }
    return simulateDragDrop(arguments[0], arguments[1]);
    """


@pytest.fixture
def authorized_user_ready(driver, registered_user):
    main = MainPage(driver)
    login = LoginPage(driver)
    main.open_main_page()
    # Ждем стабилизации страницы перед кликом
    main.wait_after_action()
    main.click_sign_in_button()
    login.login_user(registered_user["data"]["email"], registered_user["data"]["password"])
    main.wait_for_login_completion()
    return {"main": main, "user_data": registered_user}