from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Login(BasePage):

    # 扫码
    def scan(self):
        pass

    # 进入注册
    def into_register(self):
        self.find(By.CSS_SELECTOR, ".login_registerBar_link").click()
        return resister()
