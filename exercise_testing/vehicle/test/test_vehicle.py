from project.vehicle import Vehicle
from unittest import TestCase, main

class TestVehicle(TestCase):
    fuel_test = 45.5
    horse_power_test = 150.5

    def setUp(self):
        self.car = Vehicle(self.fuel_test, self.horse_power_test)

    def test_class_attributes(self):
        self.assertTrue(isinstance(self.car.DEFAULT_FUEL_CONSUMPTION, float))
        self.assertTrue(isinstance(self.car.fuel_consumption, float))
        self.assertTrue(isinstance(self.car.fuel, float))
        self.assertTrue(isinstance(self.car.horse_power, float))
        self.assertTrue(isinstance(self.car.capacity, float))

    def test_initialization(self):
        self.assertEqual(self.fuel_test, self.car.fuel)
        self.assertEqual(self.horse_power_test, self.car.horse_power)
        self.assertEqual(1.25, self.car.fuel_consumption)
        self.assertEqual(self.fuel_test,  self.car.capacity)

    def test_drive_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_reduces_fuel(self):
        initial_fuel = self.car.fuel
        distance = 10
        needed_fuel = self.car.fuel_consumption * distance
        self.car.drive(distance)
        result = initial_fuel - needed_fuel
        self.assertEqual(result, self.car.fuel)

    def test_refuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_increases_fuel(self):
        initial_fuel = self.car.fuel
        distance = 10
        needed_fuel = self.car.fuel_consumption * distance
        self.car.drive(distance)
        self.car.refuel(needed_fuel)
        self.assertEqual(initial_fuel, self.car.fuel)

    def test_str_representation(self):
        result = f"The vehicle has {self.car.horse_power} " \
                f"horse power with {self.car.fuel} fuel left and "\
                f"{self.car.fuel_consumption} fuel consumption"

        self.assertEqual(result, str(self.car))

if __name__ == '__main__':
    main()
#