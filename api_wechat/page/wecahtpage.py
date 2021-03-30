import requests

from api_wechat.page.page import Page


class Address(Page):
	"""
	企业微信通讯录增删改查page
	"""


	def creat_member(self, userid, name, mobile, department):
		# 增加成员接口
		creat_url = "https://qyapi.weixin.qq.com/cgi-bin/user/create"

		json = {
		    "userid": userid,
		    "name": name,
		    "mobile": mobile,
		    "department": department
		}
		# r = self.session.post(url=creat_url, json=json)
		r = self.send("POST",url=creat_url,json = json)
		# 返回responese整体
		return r.json()

	def get_member(self, userid):
		# 查询成员接口
		get_url = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
		params = {
		    "userid": userid
		}
		# r = self.session.get(url=get_url, params=params)
		r = self.send("GET",url=get_url,params=params)
		return r.json()

	def update_member(self):
		# 更新成员接口
		update_url = "https://qyapi.weixin.qq.com/cgi-bin/user/update"
		# r = self.session.post(url=update_url)
		r = self.send("POST",url=update_url)
		return r.json()

	def delete_member(self, userid):
		# 删除成员接口
		delete_url = "https://qyapi.weixin.qq.com/cgi-bin/user/delete"
		params = {
		    "userid": userid
		}
		# r =self.session.get(url=delete_url, params=params)
		r = self.send("GET",url=delete_url,params=params)
		print(r.json())
		return r.json()
