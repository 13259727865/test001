import time

from app_wechat_plus.page.basepage import BasePage
from app_wechat_plus.page.information import PeopleInformation


# 查看搜索结果页面
class SelectResult(BasePage):
    def goto_member_info(self):
        # 点击搜索结果
        self.parese_action("../parese_action_yaml/goto_member_info.yaml", "goto_member_info")
        # 跳转到点击的用户信息页面
        return PeopleInformation(self.driver)

    # 查看当前用户名查找出来的数量
    def result_mem(self):
        result_mem = len(self.parese_action("../parese_action_yaml/goto_member_info.yaml", "result_mem"))
        return result_mem
