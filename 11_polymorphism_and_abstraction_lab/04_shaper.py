import math
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return math.pi * (self.__radius ** 2)

    def calculate_perimeter(self):
        return (self.__radius * 2) * math.pi

class Rectangle:
    def __init__(self, height, width):
        self.__height = height
        self.___width = width

    def calculate_area(self):
        return self.___width * self.__height

    def calculate_perimeter(self):
        return (self.__height + self.___width) * 2


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
