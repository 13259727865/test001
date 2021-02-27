from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


# 基类
class BasePage:
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

    # 定位元素方法
    def find(self, by, locator):
        self._driver.find_element(by, locator)
