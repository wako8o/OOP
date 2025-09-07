from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):

    MOUSE = 0.10

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if not isinstance(food, (Vegetable, Fruit)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * Mouse.MOUSE


class Dog(Mammal):

    DOG = 0.40

    def make_sound(self):
        return "Woof!"


    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * Dog.DOG


class Cat(Mammal):

    CAT = 0.30

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if not isinstance(food, (Vegetable, Meat)):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * Cat.CAT

class Tiger(Mammal):

    TIGER = 1.0

    def make_sound(self):
        return "ROAR!!!"


    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * Tiger.TIGER

