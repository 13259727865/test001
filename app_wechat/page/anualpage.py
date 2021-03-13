#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Author:Gemini
from appium.webdriver.common.mobileby import MobileBy

from app_wechat.page.basepage import BasePage


class AnualAdd(BasePage):
    def anual_add(self):
        # self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/b7m").send_keys("手动1")
        # self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/fwi").send_keys("13223232323")
        # self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/aj_").click()
        self.parse_action("../page/anual.yaml", "anual_add")

    def ok_add(self):
        self.parse_action("../page/anual.yaml", "ok_add")
