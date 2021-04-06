#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:Gemini

import requests

from pony_pass.pass_page.alarm_page import AlarmPage
from pony_pass.pass_page.page import Page


class TestAlarm:
	def setup(self):
		self.main = AlarmPage()


	def test_alarm(self):
		print(self.main.alarm())