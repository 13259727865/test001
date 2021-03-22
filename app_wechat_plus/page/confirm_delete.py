from app_wechat_plus.page.basepage import BasePage


# 删除成员确认框
class ConfirmDelete(BasePage):
    # 确认删除
    def delete_ok(self):
        self.parese_action("../parese_action_yaml/confirm_delete.yaml", "delete_ok")

    # 取消删除
    def delete_no(self):
        self.parese_action("../parese_action_yaml/confirm_delete.yaml", "delete_no")
