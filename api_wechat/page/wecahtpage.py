import requests


class Address:
    """
    企业微信通讯录增删改查page
    """

    def get_token(self):
        # 获取token接口
        token_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid": "ww9c7dae8f91bb0f1c",
            "corpsecret": "lnmHtUhqRJRLdYiUioDR71kbO0IQ4J9LBaiEb4BJEns"
        }
        r = requests.get(url=token_url, params=params)
        # 返回response中token值

        return r.json()["access_token"]

    def creat_member(self, userid, name, mobile, department):
        # 增加成员接口
        creat_url = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
        params = {
            "access_token": self.get_token()
        }
        json = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        r = requests.post(url=creat_url, params=params, json=json)
        # 返回responese整体
        return r.json()

    def get_member(self, userid):
        # 查询成员接口
        get_url = "https://qyapi.weixin.qq.com/cgi-bin/user/get"
        params = {
            "access_token": self.get_token(),
            "userid": userid
        }
        r = requests.get(url=get_url, params=params)
        return r.json()

    def update_member(self):
        # 更新成员接口
        update_url = "https://qyapi.weixin.qq.com/cgi-bin/user/update"
        params = {
            "access_token": self.get_token()
        }
        r = requests.post(url=update_url, params=params)
        return r.json()

    def delete_member(self, userid):
        # 删除成员接口
        delete_url = "https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        params = {
            "access_token": self.get_token(),
            "userid": userid
        }
        r = requests.get(url=delete_url, params=params)
        print(r.json())
        return r.json()
