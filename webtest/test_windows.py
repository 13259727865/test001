from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from webtest.base import Base


class TestWin(Base):
    def test_window(self):
        # self.driver.get('https://www.baidu.com/')
        self.driver.find_element(By.XPATH, '//*[@id="u1"]/a').click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        self.driver.find_element(By.XPATH, '//*[@class="pass-reglink pass-link"]').click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        window = self.driver.window_handles
        self.driver.switch_to_window(window[-1])
        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_4__userName"]').send_keys('1245')
        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_4__phone"]').send_keys('1324545454')
        sleep(5)
        self.driver.switch_to_window(window[0])
        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_11__footerULoginBtn"]').click()
