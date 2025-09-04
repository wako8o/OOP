from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, fuel):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass

class Car(Vehicle):

    def drive(self, distance):
        consumption = (self.fuel_consumption + 0.9) * distance
        if self.fuel_quantity - consumption >= 0:
            self.fuel_quantity -= consumption
        return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += fuel
        return self.fuel_quantity

class Truck(Vehicle):


    def drive(self, distance):

        consumption = (self.fuel_consumption + 1.6) * distance
        if self.fuel_quantity - consumption >= 0:
            self.fuel_quantity -= consumption

        return self.fuel_quantity


    def refuel(self, fuel):
        self.fuel_quantity += (fuel * 0.95)
        return self.fuel_quantity

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
