from project.animal import Animal


class Cheetah(Animal):

    needed_money_cheetah = 60

    def __init__(self, name: str, gender: str, age: int) -> None:
        super().__init__(name, gender, age, 60)

