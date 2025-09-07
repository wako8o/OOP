from project.animals.animal import Bird
from project.food import Meat


class Owl(Bird):

    OWL = 0.25

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.food_eaten += food.quantity
        self.weight += food.quantity * Owl.OWL


class Hen(Bird):

    HEN = 0.35

    def make_sound(self):
        return "Cluck"

    def feed(self, food):

        self.food_eaten += food.quantity
        self.weight += food.quantity * Hen.HEN
