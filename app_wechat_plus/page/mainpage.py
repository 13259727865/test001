from app_wechat_plus.page.basepage import BasePage
from app_wechat_plus.page.mail_list import MailList


class MainPage(BasePage):
    # 微信首页
    def goto_maillist(self):
        # 点击通讯录
        self.parese_action("../parese_action_yaml/main.yaml", "goto_maillist")
        # 跳转通讯录页面
        return MailList(self.driver)
