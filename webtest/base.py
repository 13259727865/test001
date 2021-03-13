from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Base:
    def setup(self):
        option = Options()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
