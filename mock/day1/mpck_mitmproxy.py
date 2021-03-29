#!/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:Gemini
import json

from mitmproxy import ctx, http


# from mitmproxy.http import HTTPFlow
# from mitmproxy.io.proto.http_pb2 import HTTPFlow


class Counter:
	def __init__(self):
		self.num = 0

	# def request(self, flow:http.HTTPFlow):
	# 	self.num = self.num + 1
	# 	ctx.log.info("We've seen %d flows" % self.num)
	def response(self, flow:http.HTTPFlow):
		if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=" in flow.request.pretty_url:
			data = json.loads(flow.response.text)
			# data["data"]["items"][1]["quote"]["name"] = data["data"]["items"][1]["quote"]["name"]*2
			# data["data"]["items"][2]["quote"]["name"] = " "
			with open("F:/untitled1/testing/mock/day1/123","w",encoding="utf-8") as f1:
				json.dump(data,f1,indent=2,ensure_ascii=False)
			a = self.travel(data)
			with open("F:/untitled1/testing/mock/day1/234","w",encoding="utf-8") as f:
				json.dump(a,f,indent=2,ensure_ascii=False)
			flow.response.text = json.dumps(a)

	def travel(self,data):
		if isinstance(data,dict):
			for key,value in data.items():
				data[key] = self.travel(value)
		elif isinstance(data,list):
			data =[self.travel(i) for i in data]
		elif isinstance(data,int) or isinstance(data,float):
			data = data*2
		elif isinstance(data,bool):
			data = data
		elif isinstance(data,str):
			data = data
		else:
			data = data+1
		return data
	# def travel(self,data):
	# 	if  isinstance(data,dict):
	# 		for key,value in data.items():
	# 			data[key] = self.travel(value)
	# 	elif isinstance(data, list):
	# 		data =[self.travel(i) for i in data]
	# 	elif data=="隆基股份":
	# 		data += data
	# 	else:
	# 		data = data
	# 	return data
addons = [
	Counter()
]


