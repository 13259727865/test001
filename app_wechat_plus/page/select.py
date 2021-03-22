from app_wechat_plus.page.basepage import BasePage
from app_wechat_plus.page.information import PeopleInformation
from app_wechat_plus.page.select_result import SelectResult


# 搜索页面
class Select(BasePage):
    def select(self, name):
        self._trans['name'] = name
        # 填写搜索信息
        self.parese_action("../parese_action_yaml/select.yaml", "select")

        # 跳转查看搜索结果
        return SelectResult(self.driver)
