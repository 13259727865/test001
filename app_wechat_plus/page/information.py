from app_wechat_plus.page.basepage import BasePage
from app_wechat_plus.page.information_add import Information_add


# 用户信息界面
class PeopleInformation(BasePage):
    def goto_informationadd(self):
        # 点击详情按钮
        self.parese_action("../parese_action_yaml/information.yaml", "goto_iInformationadd")
        # 跳转进入私人信息界面
        return Information_add(self.driver)
