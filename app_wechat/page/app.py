#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Author:Gemini
from appium import webdriver

from app_wechat.page.mainpage import MainPage


class App:
    def __init__(self):
        self.driver = None
        self.start()

    def start(self):
        caps = {}
        caps['platformName'] = 'Android'
        caps['deviceName'] = 'wework'
        caps['appPackage'] = 'com.tencent.wework'
        caps['appActivity'] = '.launch.LaunchSplashActivity'
        caps['noReset'] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def goto_main(self):
        return MainPage(self.driver)

    def driver_quit(self):
        self.driver.quit()
