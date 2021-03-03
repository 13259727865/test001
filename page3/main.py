#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Author:Gemini
from selenium.webdriver.common.by import By

from page3.add_member import Add_member
from page3.page import Page


class Main(Page):
    _page_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        self.find(By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div').click()
        return Add_member(self._driver)

    def goto_group_sendout(self):
        pass
