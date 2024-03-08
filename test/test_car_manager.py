import unittest
from car_manager import Car


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car("Dodge", "Challenger", 12, 90)

    def test_init_stores_data(self):
        result = [self.car.make, self.car.model, self.car.fuel_consumption, self.car.fuel_capacity,
                  self.car.fuel_amount]
        self.assertEqual(result, ["Dodge", "Challenger", 12, 90, 0])

    def test_make_setter(self):
        self.car.make = "Subaru"
        self.assertEqual("Subaru", self.car.make)

    def test_make_setter_raises_exception_for_none(self):
        with self.assertRaises(Exception) as error:
            self.car.make = None
        self.assertEqual("Make cannot be null or empty!", str(error.exception))

    def test_make_setter_raises_exception_for_empty(self):
        with self.assertRaises(Exception) as error:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(error.exception))

    def test_model_setter(self):
        self.car.model = "Outback"
        self.assertEqual("Outback", self.car.model)

    def test_model_setter_raises_exception_for_none(self):
        with self.assertRaises(Exception) as error:
            self.car.model = None
        self.assertEqual("Model cannot be null or empty!", str(error.exception))

    def test_model_setter_raises_exception_for_empty(self):
        with self.assertRaises(Exception) as error:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(error.exception))

    def test_fuel_consumption_setter(self):
        self.car.fuel_consumption = 12
        self.assertEqual(12, self.car.fuel_consumption)

    def test_fuel_consumption_setter_raises_exception_for_negative(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(error.exception))

    def test_fuel_consumption_setter_raises_exception_for_zero(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(error.exception))

    def test_fuel_capacity_setter(self):
        self.car.fuel_capacity = 90
        self.assertEqual(90, self.car.fuel_capacity)

    def test_fuel_capacity_setter_raises_exception_for_negative(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(error.exception))

    def test_fuel_capacity_setter_raises_exception_for_zero(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(error.exception))

    def test_fuel_amount_setter(self):
        self.car.fuel_amount = 90
        self.assertEqual(90, self.car.fuel_amount)

    def test_fuel_amount_setter_raises_exception_for_negative(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(error.exception))

    def test_refuel_raises_for_negative(self):
        with self.assertRaises(Exception) as error:
            self.car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(error.exception))

    def test_refuel_raises_for_zero(self):
        with self.assertRaises(Exception) as error:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(error.exception))

    def test_refuel_below_capacity(self):
        self.car.refuel(30)
        self.assertEqual(self.car.fuel_amount, 30)

    def test_refuel_above_capacity(self):
        self.car.refuel(100)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_drive_raises(self):
        with self.assertRaises(Exception) as error:
            self.car.drive(40)
        self.assertEqual(str(error.exception), "You don't have enough fuel to drive!")

    def test_drive_with_enough_fuel(self):
        self.car.refuel(90)
        initial_fuel = self.car.fuel_amount
        self.car.drive(10)
        fuel_needed = (10 / 100) * self.car.fuel_consumption
        self.assertEqual(self.car.fuel_amount, initial_fuel - fuel_needed)


if __name__ == "__main__":
    unittest.main()
