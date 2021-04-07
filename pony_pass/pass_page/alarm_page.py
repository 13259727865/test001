#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:Gemini
import requests

from pony_pass.pass_page.page import Page


class AlarmPage(Page):

	def __init__(self):
		self.session = requests.session()
		self.session.cookies=requests.utils.cookiejar_from_dict(self.login())
		print(self.session.cookies.items)

	def login(self):
		self.response = self.session.request(method="POST",
		                            url="http://121.40.214.242:8080/ponysafety2/login",
		                            headers={"Accept": "application/json"},
		                            json={"user_name":"hanc","pass_word":"dnRya2FvdGRmYnRhdGRtaWtuMTJzcWR6eDdwOXpwaGtmYw==",}
		                            )
		self.root_log.info("登录状态",self.response.json())
		# self.set_cookie=self.response.headers["Set-Cookie"]
		# cook = self.response.cookies.get_dict()["ponytech_sid"]
		# self.cookie = f"ponytech_sid={cook}"
		return self.response.cookies.get_dict()


	def alarm(self):
		response = self.session.post(
		                            url="http://121.40.214.242:8080/ponysafety2/a/report/getalarminfopage",
		                            headers={"Accept": "application/json",
		                                     },
		                            json={"start_time": "2021-04-06 00:00:00", "end_time": "2021-04-06 23:59:59",
		                                  "max_speed": 150, "min_speed": 0, "count": 30, "page": 1, "type": 4,
		                                  "alarmtype_list": [14, 1],
		                                  "vehicle_id": ["25831", "12914"]}
		                            )
		self.root_log.info(f'报警查询返回:{response.headers}')
		return response.json()