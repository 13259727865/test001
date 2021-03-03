#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Author:Gemini
from page3.main import Main


class TestWechat:

    def setup(self):
        self.main = Main()

    def test_add(self):
        name = '李四5'
        lname = 'lisi25'
        phone = '13250565655'
        page = self.main.goto_add_member()
        page.fill(name, lname, phone)
        names = page.get_member()
        print(names)
        assert name in names
