from app_wechat_plus.page.basepage import BasePage
from app_wechat_plus.page.private import Private


# 个人信息附加信息页面
class Information_add(BasePage):
    def goto_edit_member(self):
        # 点击编辑成员
        self.parese_action("../parese_action_yaml/information_add.yaml", "goto_edit_member")
        # 跳转进入私人信息页面
        return Private(self.driver)
