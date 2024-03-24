from project.second_hand_car import SecondHandCar
import unittest


class TestSecondHandCar(unittest.TestCase):
    def setUp(self):
        self.car = SecondHandCar("Challenger", "muscle", 23000, 93000.00)

    def test_init(self):
        expected = ["Challenger", "muscle", 23000, 93000.00, []]
        actual = [self.car.model, self.car.car_type, self.car.mileage, self.car.price, self.car.repairs]
        self.assertEqual(expected, actual)

    def test_price_setter_raise(self):
        with self.assertRaises(ValueError) as error:
            self.car.price = 0
        self.assertEqual(str(error.exception), 'Price should be greater than 1.0!')

    def test_price_setter(self):
        self.car.price = 100000
        expected = 100000
        actual = self.car.price
        self.assertEqual(expected, actual)

    def test_mileage_setter_raise(self):
        with self.assertRaises(ValueError) as error:
            self.car.mileage = 100
        self.assertEqual(str(error.exception), 'Please, second-hand cars only! Mileage must be greater than 100!')

    def test_mileage_setter(self):
        self.car.mileage = 200
        expected = 200
        actual = self.car.mileage
        self.assertEqual(expected, actual)

    def test_set_promotional_price_raise(self):
        with self.assertRaises(ValueError) as error:
            self.car.set_promotional_price(500000)
        self.assertEqual(str(error.exception), 'You are supposed to decrease the price!')

    def test_set_promotional_price(self):
        expected = 'The promotional price has been successfully set.'
        actual = self.car.set_promotional_price(85000)
        self.assertEqual(expected, actual)

    def test_need_repair_impossible(self):
        expected = 'Repair is impossible!'
        actual = self.car.need_repair(80000, "false alarm")
        self.assertEqual(expected, actual)

    def test_need_repair(self):
        expected_return = 'Price has been increased due to repair charges.'
        actual_return = self.car.need_repair(100, "blinker")
        expected = [93100, ["blinker"]]
        actual = [self.car.price, self.car.repairs]
        self.assertEqual(expected, actual)
        self.assertEqual(expected_return, actual_return)

    def test_gt_mismatch(self):
        self.other_car = SecondHandCar("Durango", "SUV", 50000, 50000)
        expected = 'Cars cannot be compared. Type mismatch!'
        actual = self.car.__gt__(self.other_car)
        self.assertEqual(expected, actual)

    def test_gt(self):
        self.other_car = SecondHandCar("Charger", "muscle", 50000, 50000)
        expected = True
        actual = self.car.__gt__(self.other_car)
        self.assertEqual(expected, actual)

    def test_str(self):
        expected = f"""Model Challenger | Type muscle | Milage 23000km
Current price: 93000.00 | Number of Repairs: 0"""
        actual = self.car.__str__()
        self.assertEqual(expected, actual)
