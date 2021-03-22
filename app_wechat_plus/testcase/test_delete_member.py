import time

import pytest as pytest

from app_wechat_plus.page.app import App
from app_wechat_plus.page.mainpage import MainPage


class TestDeleteMember:
	def setup(self):
		self.app = App()

	@pytest.mark.parametrize('name', ['李四', '李四', '李四3', '李四6'])
	# 断言删除用户成功
	def test_delete_member(self, name):
		select = self.app.goto_main().goto_maillist().goto_select().select(name)
		delete_fronte = select.result_mem()
		select.goto_member_info().goto_informationadd().goto_edit_member().delete_member().delete_ok()
		time.sleep(5)
		delete_after = select.result_mem()

		if delete_after == 0:
			# 删除后如果返回列表为空就断言“无搜索结果”
			# a = self.app.goto_main().finds('xpath','//*[@text="无搜索结果"]')
			assert self.app.goto_main().finds('xpath', '//*[@text="无搜索结果"]')
		else:
			# 断言比删除之前少一个
			assert delete_fronte - delete_after == 1
