from project.climbing_robot import ClimbingRobot
import unittest


class TestClimbingRobot(unittest.TestCase):
    def setUp(self):
        self.robot = ClimbingRobot('Alpine', "heart", 100, 100)

    def test_class_constant(self):
        expected = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']
        actual = ClimbingRobot.ALLOWED_CATEGORIES
        self.assertEqual(expected, actual)

    def test_init(self):
        expected = ["Alpine", "heart", 100, 100, []]
        actual = [self.robot.category, self.robot.part_type, self.robot.capacity, self.robot.memory,
                  self.robot.installed_software]
        self.assertEqual(expected, actual)

    def test_category_setter_raises(self):
        with self.assertRaises(ValueError) as error:
            self.robot.category = "Some"
        self.assertEqual(str(error.exception), f"Category should be one of {ClimbingRobot.ALLOWED_CATEGORIES}")

    def test_category_setter(self):
        self.category = "Mountain"
        expected = "Mountain"
        actual = self.category
        self.assertEqual(expected, actual)

    def test_get_used_capacity_with_software(self):
        self.robot.installed_software = [{"name": "PhotoShop", "capacity_consumption": 10, "memory_consumption": 10},
                                         {"name": "GitHub", "capacity_consumption": 10, "memory_consumption": 10}]
        expected = 20
        actual = self.robot.get_used_capacity()
        self.assertEqual(actual, expected)

    def test_get_used_capacity_without_software(self):
        expected = 0
        actual = self.robot.get_used_capacity()
        self.assertEqual(actual, expected)

    def test_get_available_capacity_with_software(self):
        self.robot.install_software({"name": "PhotoShop", "capacity_consumption": 10, "memory_consumption": 10})
        self.robot.install_software({"name": "GitHub", "capacity_consumption": 10, "memory_consumption": 10})
        expected = 80
        actual = self.robot.get_available_capacity()
        self.assertEqual(actual, expected)

    def test_get_available_capacity_without_software(self):
        expected = 100
        actual = self.robot.get_available_capacity()
        self.assertEqual(actual, expected)

    def test_get_used_memory_with_software(self):
        self.robot.installed_software = [{"name": "PhotoShop", "capacity_consumption": 10, "memory_consumption": 10},
                                         {"name": "GitHub", "capacity_consumption": 10, "memory_consumption": 10}]
        expected = 20
        actual = self.robot.get_used_memory()
        self.assertEqual(expected, actual)

    def test_get_used_memory_without_software(self):
        expected = 0
        actual = self.robot.get_used_memory()
        self.assertEqual(expected, actual)

    def test_get_available_memory_with_software(self):
        self.robot.installed_software = [{"name": "PhotoShop", "capacity_consumption": 10, "memory_consumption": 10},
                                         {"name": "GitHub", "capacity_consumption": 10, "memory_consumption": 10}]
        expected = 80
        actual = self.robot.get_available_memory()
        self.assertEqual(expected, actual)

    def get_available_memory_without_software(self):
        expected = 100
        actual = self.robot.get_available_memory()
        self.assertEqual(expected, actual)

    def test_install_software_with_enough_memory_and_capacity(self):
        actual_return = self.robot.install_software(
            {"name": "PhotoShop", "capacity_consumption": 10, "memory_consumption": 10})
        expected_return = f"Software 'PhotoShop' successfully installed on Alpine part."
        expected = [{"name": "PhotoShop", "capacity_consumption": 10, "memory_consumption": 10}]
        actual = self.robot.installed_software
        self.assertEqual(expected, actual)
        self.assertEqual(expected_return, actual_return)

    def test_install_software_with_not_enough_memory(self):
        actual_return = self.robot.install_software(
            {"name": "PhotoShop", "capacity_consumption": 10, "memory_consumption": 110})
        expected_return = f"Software 'PhotoShop' cannot be installed on Alpine part."
        self.assertEqual(expected_return, actual_return)

    def test_install_software_with_not_enough_capacity(self):
        actual_return = self.robot.install_software(
            {"name": "PhotoShop", "capacity_consumption": 110, "memory_consumption": 10})
        expected_return = f"Software 'PhotoShop' cannot be installed on Alpine part."
        self.assertEqual(expected_return, actual_return)


if __name__ == '__main__':
    unittest.main()
