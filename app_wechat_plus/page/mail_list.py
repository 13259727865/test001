from app_wechat_plus.page.basepage import BasePage
from app_wechat_plus.page.select import Select


# 通讯录页面
class MailList(BasePage):

    def goto_select(self):
        # 点击搜索按钮
        self.parese_action("../parese_action_yaml/maillist.yaml", "goto_select")
        # 跳转到搜索界面
        return Select(self.driver)
