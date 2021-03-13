#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Author:Gemini
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestAppWechat:
    def setup(self):
        caps = {}
        caps['platformName'] = 'Android'
        caps['deviceName'] = 'wework'
        caps['appPackage'] = 'com.tencent.wework'
        caps['appActivity'] = '.launch.LaunchSplashActivity'
        caps['noReset'] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="工作台"]').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/i1x"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/awt"]').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']")
