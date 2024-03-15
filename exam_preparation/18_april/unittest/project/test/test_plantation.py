from plantation import Plantation
import unittest


class TestPlantation(unittest.TestCase):
    def setUp(self):
        self.plant = Plantation(100)

    def test_init(self):
        expected = [100, {}, []]
        actual = [self.plant.size, {}, []]
        self.assertEqual(expected, actual)

    def test_size_setter_raises(self):
        with self.assertRaises(ValueError) as error:
            self.plant.size = -1
        self.assertEqual(str(error.exception), "Size must be positive number!")

    def test_size_setter(self):
        self.plant.size = 50
        expected = 50
        actual = self.plant.size
        self.assertEqual(actual, expected)

    def test_hire_worker_raises(self):
        self.plant.hire_worker("Pesho")
        with self.assertRaises(ValueError) as error:
            self.plant.hire_worker("Pesho")
        self.assertEqual(str(error.exception), "Worker already hired!")

    def test_hire_worker(self):
        expected_return = "Pesho successfully hired."
        actual_return = self.plant.hire_worker("Pesho")
        actual_list = self.plant.workers
        expected_list = ["Pesho"]
        self.assertEqual(actual_list, expected_list)
        self.assertEqual(expected_return, actual_return)

    def test_len_method(self):
        self.plant.hire_worker("Pesho")
        self.plant.hire_worker("Tosho")
        self.plant.planting("Pesho", "Lilac")
        self.plant.planting("Pesho", "Orchid")
        self.plant.planting("Tosho", "Rose")
        expected = 3
        actual = len(self.plant)
        self.assertEqual(actual, expected)

    def test_planting_worker_not_found(self):
        with self.assertRaises(ValueError) as error:
            self.plant.planting("Pesho", "rose")
        self.assertEqual(str(error.exception), "Worker with name Pesho is not hired!")

    def test_planting_plantation_full(self):
        self.plant.size = 1
        self.plant.hire_worker("Pesho")
        self.plant.planting("Pesho", "Lilac")
        with self.assertRaises(ValueError) as error:
            self.plant.planting("Pesho", "tulip")
        self.assertEqual(str(error.exception), "The plantation is full!")

    def test_planting_first_plant(self):
        self.plant.hire_worker("Pesho")
        actual_return = self.plant.planting("Pesho", "Lilac")
        expected_dict = {"Pesho": ["Lilac"]}
        actual_dict = self.plant.plants
        expected_return = "Pesho planted it's first Lilac."
        self.assertEqual(actual_return, expected_return)
        self.assertEqual(actual_dict, expected_dict)

    def test_planting_second_plant(self):
        self.plant.hire_worker("Pesho")
        self.plant.planting("Pesho", "Lilac")
        actual_return = self.plant.planting("Pesho", "Rose")
        expected_dict = {"Pesho": ["Lilac", "Rose"]}
        actual_dict = self.plant.plants
        expected_return = "Pesho planted Rose."
        self.assertEqual(actual_return, expected_return)
        self.assertEqual(actual_dict, expected_dict)

    def test_str(self):
        self.plant.hire_worker("Pesho")
        self.plant.hire_worker("Gosho")
        self.plant.planting("Pesho", "Lilac")
        self.plant.planting("Pesho", "Rose")
        self.plant.planting("Gosho", "Peony")

        expected = ("Plantation size: 100\n"
                    "Pesho, Gosho\n"
                    "Pesho planted: Lilac, Rose\n"
                    "Gosho planted: Peony")
        actual = str(self.plant)
        self.assertEqual(actual, expected)

    def test_repr(self):
        self.plant.hire_worker("Pesho")
        self.plant.hire_worker("Gosho")
        expected = ("Size: 100\n"
                    "Workers: Pesho, Gosho")
        actual = self.plant.__repr__()
        self.assertEqual(actual, expected)