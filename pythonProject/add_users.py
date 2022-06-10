# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import xlrd as xlrd
import pymysql
import requests

# user_name = user[0]
# phone_email = user[1]  0：手机  1：邮箱
# identity = user[2]

# host = "39.107.96.52"
host = "123.57.220.231"


class AddUser:
    conn_account = pymysql.connect(
        host=host,
        port=3307,
        user="db_huaxia",
        password="EKZBLx9iJ6+WLVuN3FvE6w",
        database="lux_account_x",
        charset="utf8"
    )
    cursor_account = conn_account.cursor()

    conn_studio = pymysql.connect(
        host=host,
        port=3307,
        user="db_huaxia",
        password="EKZBLx9iJ6+WLVuN3FvE6w",
        database="luxsimulation",
        charset="utf8"
    )
    cursor_studio = conn_studio.cursor()

    # 添加权限
    def add_auth(self, userid, identity='probationer'):
        select_sql = f"select * from pp_user_auth where user_id='{userid}'"
        print(self.cursor_studio.execute(select_sql))
        if self.cursor_studio.execute(select_sql):
            print(f"{userid}权限为打开状态")
        else:
            print(f"{userid}权限未打开")
            sql = f"""
                INSERT INTO `pp_user_auth` 
                    ( `id`, `user_id`, `rol`, `next_notice_time`, `identity`, 
                    `expired_at`, `create_time`, `update_time`, `status` )
                VALUES
                    ( NULL, '{userid}', 1, NOW(), '{identity}', NULL, NOW(), NOW(), 1 )
            """
            self.cursor_studio.execute(sql)
            self.conn_studio.commit()
            print("权限开通成功")

    # 添加新用户接口
    def requests_adduser(self, user, register_type):
        data = {
            # "registerPlatformId": 1,
            "password": "$2y$10$yaB9tRvXPglptd2xZRLhB.1.mFAZ6TWmKiaL4i5hCACs.tCZ37FuG"}
        if register_type == 0:
            data.update({"secPhone": "+86#" + str(int(user))})
        elif register_type == 1:
            data.update({"secEmail": user})
        # request_url="http://test-accountx.luxcreo.cn/cn/api/rpc/user/create"
        request_url = "https://auth.luxcreo.cn/cn/api/rpc/user/create"
        q = requests.request(method="post", url=request_url,
                             params=data
                             )
        try:
            userid = q.json()["uid"]
            print("新用户添加成功")
            self.add_auth(userid)
        except:
            print("用户添加异常", q.json())

    def reload_ex(self, path):
        excle = xlrd.open_workbook(path)
        table = excle.sheets()[0]
        # 从第一行开始
        for i in range(0, table.nrows):

            # 循环拿第一列的账号
            user = table.row_values(i)
            user_name = user[0]
            phone_email = user[1]
            print(f"===================={user[0]}===========================")
            # identity = user[2]
            if phone_email == 0:
                sql = f'select password from user where sec_phone="+86#{str(int(user_name))}" '
            else:
                sql = f'select password from user where sec_email="{user_name}"'
            if self.cursor_account.execute(sql):
                ispw = bool(list(self.cursor_account.fetchone())[0])
                if ispw is not False:
                    print(f"{user[0]}已存在且有密码，不做变更")
                elif ispw is False:
                    print(f"{user[0]}已存在但没密码，添加密码")
                    add_password_sql = \
                        f"""UPDATE user 
                        SET PASSWORD = 0x24327924313024796142397452765850676C70746432785A524C68422E312E6D46415A3654576D4
                        B69614C34693568434143732E74435A3337467547 
                        WHERE sec_phone = "+86#{str(int(user_name))}" """
                    self.cursor_account.execute(add_password_sql)
                    self.conn_account.commit()
                    print(f"{user[0]}添加密码完成")
                else:
                    print(f"{user[0]}已存在但密码查询出问题，请核实")
                if phone_email == 0:
                    userid_sql = f'select uid from user where sec_phone="+86#{str(int(user_name))}"'
                else:
                    userid_sql = f'select uid from user where sec_email="{user_name}"'
                self.cursor_account.execute(userid_sql)
                userid = self.cursor_account.fetchone()
                self.add_auth(userid[0])
            elif self.cursor_account.execute(sql) == 0:
                # 没有该用户，添加新用户
                print("没有该用户，添加新用户")
                self.requests_adduser(user_name, phone_email)


if __name__ == '__main__':
    a = AddUser()
    path = r"C:\Users\xiaoh\Desktop\批量上传模板 _correct.xls"
    a.reload_ex(path)
    # a.requests_adduser()
