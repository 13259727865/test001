import selenium
from selenium import webdriver


def test_ponysafety1():
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
