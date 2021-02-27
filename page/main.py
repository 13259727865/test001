from selenium.webdriver.common.by import By

from page.base_page import BasePage
from page.login import Login
from page.register import Register


class Main(BasePage):
    """
    首页page
    """
    # 重写首页url
    _base_url = "https://work.weixin.qq.com/"

    # 登录按钮
    def into_login(self):
        # 点击登录按钮
        self.find(By.CSS_SELECTOR, ".index_top_operation_loginBtn").click()
        # 跳转登录页面
        return Login(self._driver)

    # 注册按钮
    def into_register(self):
        # 点击注册按钮
        self.find(By.CSS_SELECTOR, "index_head_info_pCDownloadBtn").click()
        return Register(self._driver)
