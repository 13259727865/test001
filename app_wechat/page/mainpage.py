#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Author:Gemini
from appium.webdriver.common.mobileby import MobileBy

from app_wechat.page.basepage import BasePage
from app_wechat.page.maillistpage import MailList


class MainPage(BasePage):
    def goto_maillist(self):
        # self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        self.parse_action("../page/mainpage.yaml", "goto_maillist")
        return MailList(self.driver)
