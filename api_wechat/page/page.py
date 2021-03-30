#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:Gemini
import requests


class Page:
	def __init__(self):
		self.session = requests.session()
		self.session.params = {"access_token":self.get_token()}



	def send(self,*args,**kwargs):
		return self.session.request(*args,**kwargs)



	def get_token(self):
		# 获取token接口
		token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
		params = {
			"corpid": "ww9c7dae8f91bb0f1c",
			"corpsecret": "lnmHtUhqRJRLdYiUioDR71kbO0IQ4J9LBaiEb4BJEns"
		}
		r = requests.get(url=token_url, params=params)
		# 返回response中token值

		return r.json()["access_token"]