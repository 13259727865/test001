from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


# 基类
class BasePage:
    _base_url = ""

    # _driver = ""

    def __init__(self, driver: WebDriver = None):
        self._driver = ""
        if driver is None:
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self._driver = webdriver.Chrome(options=option)
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

    # 定位元素方法
    def find(self, by, locator):
        return self._driver.find_element(by, locator)
