from project.animal import Animal


class Tiger(Animal):

    needed_money_tiger = 45

    def __init__(self, name: str, gender: str, age: int) -> None:
        super().__init__(name, gender, age, 45)
