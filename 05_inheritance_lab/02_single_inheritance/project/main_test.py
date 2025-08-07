from project.animal import Animal
from project.dog import Dog

a = Animal()
d = Dog()
print(a.eat())
print(d.eat())
print(d.bark())
print(isinstance(d, Dog))
print(isinstance(d, Animal))
print(isinstance(a, Dog))
print(isinstance(a, Animal))
print(issubclass(Dog, Animal))
print(issubclass(Animal, Dog))