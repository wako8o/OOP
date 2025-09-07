from project.animals.birds import Owl, Hen
from project.animals.mammals import Mouse, Dog, Cat, Tiger
from project.food import Vegetable, Meat, Fruit, Seed

# tigre
tiger = Tiger("San Dukan", 150.0, "S dvata noja")
meat = Meat(5)
veg = Vegetable(2)
print(tiger)  # Tiger [San Dukan, 150.0, S dvata noja, 0]
print(tiger.make_sound())  # ROAR!!
tiger.feed(meat)
print(tiger)  # Tiger [San Dukan, 155.0, S dvata noja, 5]
result = tiger.feed(veg)
print(result)  # Tiger does not eat vegetable
print('-----------------------------------')
# cat
cat = Cat("Tom", 5.0, "Bulqrovo")
meat = Meat(2)
veg = Vegetable(3)
fruit = Fruit(1)
print(cat)  # Cat [Tom, 5.0, Bulqrovo, 0]
print(cat.make_sound())  # Meow
cat.feed(meat)
cat.feed(veg)
print(cat)  # Cat [Tom, 6.5, Bulqrovo, 5]
result = cat.feed(fruit)
print(result)  # Cat does not eat fruit
print('-----------------------------------')
# dog
dog = Dog("Sharo", 25.0, "Sofia")
meat = Meat(4)
veg = Vegetable(2)
print(dog)  # Dog [Sharo, 25.0, Sofia, 0]
print(dog.make_sound())  # Woof!
dog.feed(meat)
print(dog)  # Dog [Sharo, 26.6, Sofia, 4]
result = dog.feed(veg)
print(result)  # Dog does not eat vegetable
print('-----------------------------------')
# mouse
mouse = Mouse("Jerry", 0.2, "Tutrakan")
veg = Vegetable(2)
fruit = Fruit(1)
meat = Meat(3)
print(mouse)  # Mouse [Jerry, 0.2, Tutrakan, 0]
print(mouse.make_sound())  # Squeak
mouse.feed(veg)
mouse.feed(fruit)
print(mouse)  # Mouse [Jerry, 0.5, Tutrakan, 3]
result = mouse.feed(meat)
print(result)  # Mouse does not eat meat
print('-----------------------------------')
# hen
hen = Hen("Penka", 3.0, 50.0)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
seed = Seed(2)
print(hen)  # Hen [Penka, 50.0, 3.0, 0]
print(hen.make_sound())  # Cluck
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
hen.feed(seed)
print(hen)  # Hen [Penka, 50.0, 6.85, 11]
print('-----------------------------------')
# owl
owl = Owl("Hari", 2.5, 60.0)
meat = Meat(3)
veg = Vegetable(2)
print(owl)  # Owl [Hari, 60.0, 2.5, 0]
print(owl.make_sound())  # Hoot Hoot
owl.feed(meat)
print(owl)  # Owl [Hari, 60.0, 5.5, 3]
result = owl.feed(veg)
print(result)  # Owl does not eat vegetable
