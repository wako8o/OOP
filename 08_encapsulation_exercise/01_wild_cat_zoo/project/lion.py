from project.animal import Animal


class Lion(Animal):

    needed_money_lion = 50

    def __init__(self, name: str, gender: str, age: int):
        super().__init__(name, gender, age, 50)
