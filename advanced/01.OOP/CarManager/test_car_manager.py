from car_manager import Car
import unittest


class CarTesting(unittest.TestCase):

    def setUp(self):
        self.car = Car("car", "toyota", 1, 100)

    def test_init_method(self):
        self.assertEqual(self.car.make, "car")
        self.assertEqual(self.car.model, "toyota")
        self.assertEqual(self.car.fuel_consumption, 1)
        self.assertEqual(self.car.fuel_capacity, 100)

    def test_make_empty_or_null_raises_exception(self):
        with self.assertRaises(Exception) as exc:
            self.car.make = ""
        self.assertEqual(str(exc.exception),"Make cannot be null or empty!")

    def test_model_empty_or_null_raises_exception(self):
        with self.assertRaises(Exception) as exc:
            self.car.model = ""
        self.assertEqual(str(exc.exception),"Model cannot be null or empty!")

    def test_fuel_consumption_zero_raises_exception(self):
        with self.assertRaises(Exception) as exc:
            self.car.fuel_consumption = 0
        self.assertEqual(str(exc.exception),"Fuel consumption cannot be zero or negative!")

    def test_fuel_consumption_negative_raises_exception(self):
        with self.assertRaises(Exception) as exc:
            self.car.fuel_consumption = -1
        self.assertEqual(str(exc.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity_zero_raises_exception(self):
        with self.assertRaises(Exception) as exc:
            self.car.fuel_capacity = 0
        self.assertEqual(str(exc.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_capacity_negative_raises_exception(self):
        with self.assertRaises(Exception) as exc:
            self.car.fuel_capacity = -1
        self.assertEqual(str(exc.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount_negative_raises_exception(self):
        with self.assertRaises(Exception) as exc:
            self.car.fuel_amount = -1
        self.assertEqual(str(exc.exception), "Fuel amount cannot be negative!")

    def test_refuel_with_zero_raises_exception(self):
        with self.assertRaises(Exception) as exc:
            self.car.refuel(0)
        self.assertEqual(str(exc.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_with_negative_raises_exception(self):
        with self.assertRaises(Exception) as exc:
            self.car.refuel(-1)
        self.assertEqual(str(exc.exception), "Fuel amount cannot be zero or negative!")

    def test_if_refuel_work_properly(self):
        self.car.refuel(10)
        self.assertEqual(self.car.fuel_amount,10)

    def test_if_refueling_with_more_than_capacity_work(self):
        self.car.refuel(101)
        self.assertEqual(self.car.fuel_amount,100)

    def test_if_drive_raises_exception_when_not_enough_fuel(self):
        with self.assertRaises(Exception) as exc:
            self.car.drive(1)
        self.assertEqual(str(exc.exception),"You don't have enough fuel to drive!")

    def test_if_drive_works_properly(self):
        self.car.refuel(100)
        self.car.drive(100)
        self.assertEqual(self.car.fuel_amount,99)


if __name__ == '__main__':
    unittest.main()