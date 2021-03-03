#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Author:Gemini
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Page:
	_page_url = ""

	def __init__(self, driver: WebDriver = None):
		if driver is None:
			option = Options()
			option.debugger_address = '127.0.0.1:9222'
			# option = Options()
			# option.debugger_address='127.0.0.1:9222'
			self._driver = webdriver.Chrome(options=option)
			self._driver.implicitly_wait(5)
		else:
			self._driver = driver
		if self._page_url != "":
			self._driver.get(self._page_url)

	def find(self, by, locator):
		return self._driver.find_element(by, locator)

	def finds(self, by, locator):
		return self._driver.find_elements(by, locator)

	def wait_click(self, time, by, locator):
		return WebDriverWait(self._driver, time).until(expected_conditions.element_to_be_clickable((by, locator)))
