from 作业1.money.money_info import Money


class Excellent(Money):
    def __init__(self):
        super().__init__()
        self.year_add = int(input("年终奖金额："))

    def sum_money_info(self):
        super().sum_money_info()
        print(f"年终奖金额：{self.year_add}")
        sum_money = self.saved_money + self.send_money + self.year_add
        return sum_money


if __name__ == '__main__':
    s = Excellent()
    s.sum_money_info()
