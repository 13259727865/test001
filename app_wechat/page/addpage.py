#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Author:Gemini
from appium.webdriver.common.mobileby import MobileBy

from app_wechat.page.anualpage import AnualAdd
from app_wechat.page.basepage import BasePage


class Add_member(BasePage):
    def goto_anual(self):
        # self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/cth").click()
        # self.find_click('//*[@id="com.tencent.wework:id/cth"]')
        self.parse_action("../page/add.yaml", "goto_anual")
        return AnualAdd(self.driver)
