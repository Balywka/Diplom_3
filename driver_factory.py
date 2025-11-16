from selenium import webdriver

class DriverFactory:
    @staticmethod
    def get_driver(browser_name, headless=False):
        if browser_name.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-blink-features=AutomationControlled")
            if headless:
                options.add_argument("--headless=new")
            return webdriver.Chrome(options=options)

        elif browser_name.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            return webdriver.Firefox(options=options)

        else:
            raise ValueError(f"Unsupported browser: {browser_name}")