#!/usr/bin/env python
# -*-coding:utf-8 -*-

# Author:Gemini
from typing import List, Dict

import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.android.webdriver import WebDriver


class BasePage:
    # 每个页面接收到的driver重新赋值
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_click(self, by, locator):
        return self.find(by, locator).click()

    def find_sendkey(self, by, locator, value):
        return self.find(by, locator).send_keys(value)

    def swip_click(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 f'.text("{text}").instance(0));').click()

    def parse_action(self, path, fun):
        with open(path, "r", encoding='utf-8') as f:
            yaml_mile = yaml.safe_load(f)
            steps: List[Dict] = yaml_mile[fun]
            for step in steps:
                if step["action"] == "find":
                    self.find(step["by"], step["locator"])
                elif step["action"] == "find_click":
                    self.find_click(step["by"], step["locator"])
                elif step["action"] == "send_keys":
                    self.find_sendkey(step["by"], step["locator"], step["value"])
                elif step["action"] == "swip_click":
                    self.swip_click(step["text"])
