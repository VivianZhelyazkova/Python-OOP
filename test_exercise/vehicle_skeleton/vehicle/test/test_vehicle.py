from vehicle.project.vehicle import Vehicle
import unittest


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.v = Vehicle(90.0, 309.0)

    def test_init(self):
        actual = [self.v.fuel, self.v.capacity, self.v.horse_power, self.v.fuel_consumption]
        expected = [90.0, 90.0, 309.0, 1.25]
        self.assertEqual(actual, expected)

    def test_drive_raises(self):
        with self.assertRaises(Exception) as error:
            self.v.drive(100000)
        self.assertEqual(str(error.exception), "Not enough fuel")

    def test_drive_with_enough_fuel(self):
        expected = self.v.fuel - (10 * self.v.fuel_consumption)
        self.v.drive(10)
        actual = self.v.fuel
        self.assertEqual(actual, expected)

    def test_refuel_raises(self):
        with self.assertRaises(Exception) as error:
            self.v.refuel(100000)
        self.assertEqual(str(error.exception), "Too much fuel")

    def test_refuel_below_capacity(self):
        self.v.drive(20)
        expected = self.v.fuel + 10
        self.v.refuel(10)
        actual = self.v.fuel
        self.assertEqual(actual, expected)

    def test_str(self):
        expected = f"The vehicle has 309.0 " \
                   f"horse power with 90.0 fuel left and 1.25 fuel consumption"
        actual = self.v.__str__()
        self.assertEqual(actual, expected)
