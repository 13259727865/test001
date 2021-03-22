from app_wechat_plus.page.basepage import BasePage
from app_wechat_plus.page.confirm_delete import ConfirmDelete


# 私人信息页面
class Private(BasePage):

    def delete_member(self):
        # 点击删除成员
        self.parese_action("../parese_action_yaml/private.yaml", "delete_member")
        # 跳转确认弹框
        return ConfirmDelete(self.driver)
