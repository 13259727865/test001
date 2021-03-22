import json

import allure
import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.android.webdriver import WebDriver

from app_wechat_plus.conftest import root_log


class BasePage:
	_black_list = []
	_black_num = 5
	_black_is = 0
	_trans = {}

	def __init__(self, driver: WebDriver):
		# 把每个页面接收到的driver赋值给对象
		self.driver = driver

	# 自定义查找元素方法
	def _find(self, by, locator):
		root_log.info(f'find:by={by},locator={locator}')
		try:
			# 找到直接执行点击
			ele = self.driver.find_element(by, locator)
			self._black_is = 0
			return ele
		# 异常处理
		except Exception as e:
			root_log.error("未找到元素")
			self.driver.get_screenshot_as_file("tmp.png")
			allure.attach.file("tmp.png", attachment_type=allure.attachment_type.PNG)
			if self._black_is < self._black_num:
				self._black_is = + 1
				# 黑名单循环
				for i in self._black_list:
					# 查找黑名单元素，找到返回[ele1,ele2]，未找到返回[]
					black_ele = self.driver.find_elements(*i)
					# 判断已找到
					if len(black_ele):
						# 点击找到的黑名单
						black_ele[0].click()
						self._find(by, locator)
			self._black_is = 0
			raise e

	# 自定义查找多个相同元素
	def finds(self, by, locator):
		return self.driver.find_elements(by, locator)

	# 自定义查找点击方法
	def _find_click(self, by, locator):
		self._find(by, locator).click()

	# 自定义查找输入方法
	def _find_sendkeys(self, by, locator, value):
		self._find(by, locator).send_keys(value)

	# 自定义滑动点击方法
	def _swip_click(self, text):
		self._find(MobileBy.ANDROID_UIAUTOMATOR,
				   'new UiScrollable(new UiSelector()'
				   '.scrollable(true).instance(0))'
				   '.scrollIntoView(new UiSelector()'
				   f'.text("{text}").instance(0));').click()

	# 读取yaml文件，收集关键字参数
	def parese_action(self, path, fun):
		with open(path, "r", encoding="utf-8") as yaml_file:
			file = yaml.safe_load(yaml_file)
			fun_file = file[fun]
			str_file = json.dumps(fun_file)
			for key, value in self._trans.items():
				str_file = str_file.replace('${' + key + '}', value)
			fun_file = json.loads(str_file)
			for i in fun_file:
				if i["action"] == "find":
					self._find(i["by"], i["locator"])
				elif i["action"] == "find_click":
					self._find_click(i["by"], i["locator"])
				elif i["action"] == "send_keys":
					self._find_sendkeys(i["by"], i["locator"], i["value"])
				elif i["action"] == "swip_click":
					self._swip_click(i["text"])
				elif i["action"] == "finds":
					return self.driver.find_elements(i["by"], i["locator"])
