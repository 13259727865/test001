#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Author:Gemini
from app_wechat.page.app import App


class TestAddMember:
    def setup(self):
        self.main = App()

    def teardown(self):
        # self.main.driver_quit()
        pass

    def test_addmember(self):
        self.main.goto_main().goto_maillist().goto_add_member().goto_anual().anual_add()
