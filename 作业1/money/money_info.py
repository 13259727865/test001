"""原有存款 1000元， 发工资之后存款变为2000元
定义模块
1、money.py saved_money = 1000
2、定义发工资模块 send_money，用来增加收入计算
3、定义工资查询模块 select_money，用来展示工资数额
4、定义一个start.py ，启动文件展示最终存款金额"""


# 原有存款1000
class Money:
    def __init__(self):
        self.saved_money = int(input("原有存款："))
        self.send_money = int(input("月底薪金额："))

    def sum_money_info(self):
        print(f"原有金额：{self.saved_money}")
        print(f"工资金额：{self.send_money}")
        sum_money = self.saved_money + self.send_money
        return sum_money
