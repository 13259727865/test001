from 作业1.money.Excellent_staff import Excellent
from 作业1.money.money_info import Money

if __name__ == '__main__':
    people_no = input("普通员工还是领导：")
    if people_no == '普通':
        zs = Money()
        month_money = zs.sum_money_info()
        print(f"普通员工月工资：{month_money}")
        print(f"普通员工年工资：{month_money * 12}")
    elif people_no == '领导':
        zs = Excellent()
        month_money = zs.sum_money_info()
        print(f"普通员工月工资：{month_money}")
        print(f"普通员工年工资：{month_money * 12}")
