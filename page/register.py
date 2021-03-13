from selenium.webdriver.common.by import By

from page.base_page import BasePage


class Register(BasePage):
    def register(self):
        self.find(By.CSS_SELECTOR, "#corp_name").send_keys("杭州小驹")
        return True
