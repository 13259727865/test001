import pytest

from api_wechat.page.wecahtpage import Address


class TestWe:
    def setup(self):
        self.wechat = Address()

    @pytest.mark.parametrize("userid,name,mobile,department", [("zhangsan1", "张三", "13278967896", [1])])
    def test_creat_member(self, userid, name, mobile, department):
        # 先删除要添加的成员
        self.wechat.delete_member(userid)
        # 正式添加成员
        r = self.wechat.creat_member(userid, name, mobile, department)
        print(r)
        assert r.get("errmsg") == "created"
        r = self.wechat.get_member(userid)
        print(r)
        assert r.get("userid") == userid
