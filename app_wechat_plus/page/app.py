from appium import webdriver

from app_wechat_plus.page.basepage import BasePage
from app_wechat_plus.page.mainpage import MainPage


class App():
    a = bin

    def __init__(self):
        # 初始化dirver
        self.driver = None
        self.start()

    # 生成driver
    def start(self):
        caps = {}
        caps['platformName'] = 'Android'
        caps['deviceName'] = 'wework'
        caps['appPackage'] = 'com.tencent.wework'
        caps['appActivity'] = '.launch.LaunchSplashActivity'
        caps['noReset'] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    # 跳转访问企业微信app首页
    def goto_main(self):
        return MainPage(self.driver)
