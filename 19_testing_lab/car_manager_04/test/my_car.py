from car_manager_04.car_manager import Car
from unittest import TestCase, main


class TestCar(TestCase):

    def setUp(self):
        self.car = Car('Audi', 'A4', 8, 250)

    def test_init(self):
        self.assertEqual('Audi', self.car.make)
        self.assertEqual('A4', self.car.model)
        self.assertEqual(8, self.car.fuel_consumption)
        self.assertEqual(250, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_setter_raises_exception_when_value_is_empty_string(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
            self.car.make = None
            self.car.make = []
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_setter_raises_exception_when_value_is_empty_string(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
            self.car.model = None
            self.car.model = []
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_setter_raises_exception_when_value_is_zero_or_negative(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
            self.car.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_setter_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
            self.car.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_setter_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_increases_fuel_amount(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_above_capacity_sets_to_capacity(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.assertEqual(250, self.car.fuel_capacity)

        self.car.refuel(260)

        self.assertEqual(250, self.car.fuel_amount)

    def test_derive_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_works_fine(self):
        self.car.fuel_amount = 8

        self.car.drive(100)

        self.assertEqual(0, self.car.fuel_amount)

    def test_drive_reduces_fuel_amount(self):
        self.car.fuel_amount = 9
        self.car.drive(100)
        self.assertEqual(1, self.car.fuel_amount)


if __name__ == '__main__':
    main()