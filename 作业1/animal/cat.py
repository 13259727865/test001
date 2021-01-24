from 作业1.animal.animal import Animal


class Cat(Animal):
    def __init__(self, name, color, age, sex, master):
        super().__init__(name, color, age, sex)
        self.master = master
        self.hair = "short"

    def hunting(self):
        print(f"{self.name}捉到一只老鼠")

    def call(self):
        super().call()
        print(f"{self.name}每天都会喵喵喵")


if __name__ == '__main__':
    cat1 = Cat("mi", "ywllo", "2", "F", "jone")
    print(cat1.master)
    cat1.call()
