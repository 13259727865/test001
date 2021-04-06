import pytest

from api_wechat.page.wecahtpage import Address


class TestWe:

	def setup(self):
		self.wechat = Address()

	@pytest.mark.parametrize("userid,name,mobile,department", [("zhangsan1", "张三1", "13278967891", [1]),
	                                                       ("zhangsan2", "张三2", "13278967824", [1]),
	                                                       ("zhangsan3", "张三3", "13278967825", [1]),
	                                                       ("zhangsan4", "张三4", "13278967828", [1]),
	                                                       ("zhangsan5", "张三5", "13278967895", [1]),
	                                                       ("zhangsan6", "张三6", "13278967896", [1]),
	                                                       ("zhangsan7", "张三7", "13278967897", [1])],
	                                                        ids = [1,2,3,4,5,6,7])
	def test_creat_member(self, userid, name, mobile, department):
	# 先删除要添加的成员
		self.wechat.delete_member(userid)
	# 正式添加成员
		r = self.wechat.creat_member(userid, name, mobile, department)
		assert r.get("errmsg") == "created"
		r = self.wechat.get_member(userid)
		assert r.get("userid") == userid
