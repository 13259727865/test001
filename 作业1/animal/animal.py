# 比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
# 创建子类【猫】，继承【动物类】，
# 重写父类的__init__方法，继承父类的属性，
# 添加一个新的属性，毛发 = 短毛，
# 添加一个新的方法， 会捉老鼠，
# 重写父类的【会叫】的方法，改成【喵喵叫】

class Animal:
    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def run(self):
        print(f"{self.name}会跑")

    def call(self):
        print(f"{self.name}会叫")


if __name__ == '__main__':
    dog1 = Animal("Gii", "white", "3", "M")
    print(dog1.name)
    dog1.run()
    dog1.call()
