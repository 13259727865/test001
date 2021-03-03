#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Author:Gemini
from selenium.webdriver.common.by import By
from page3.page import Page


class Add_member(Page):
    def fill(self, name, lname, phone):
        self.find(By.XPATH, '//*[@id="username"]').send_keys(name)
        self.find(By.XPATH, '//*[@id="memberAdd_acctid"]').send_keys(lname)
        self.find(By.XPATH, '//*[@id="memberAdd_phone"]').send_keys(phone)
        self.find(By.XPATH, '//*[@id="main"]/div/div/div[2]/div/div[4]/div/form/div[1]/a[2]').click()
        return True

    def get_member(self):
        """
        获取所有联系人姓名
        :return:
        """
        self.wait_click(10, By.CSS_SELECTOR, ".member_colRight_memberTable_th_Checkbox")
        eles = self.finds(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        names = []
        for ele in eles:
            s = ele.get_attribute('title')
            names.append(s)
        return names
