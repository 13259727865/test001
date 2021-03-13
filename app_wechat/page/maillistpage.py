#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Author:Gemini
from appium.webdriver.common.mobileby import MobileBy

from app_wechat.page.addpage import Add_member
from app_wechat.page.basepage import BasePage


class MailList(BasePage):
	def goto_add_member(self):
		# self.swip_click('添加用户')
		self.parse_action("../page/maillist.yaml", "goto_add_member")
		return Add_member(self.driver)
