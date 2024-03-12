from project.mammal import Mammal

import unittest


class TestMammal(unittest.TestCase):

    def test_init(self):
        mammal = Mammal("Lion", "carnivore", "Rawr!")
        result = [mammal.name, mammal.type, mammal.sound]
        self.assertEqual(result, ["Lion", "carnivore", "Rawr!"])

    def test_sound(self):
        mammal = Mammal("Lion", "carnivore", "Rawr!")
        result = mammal.make_sound()
        self.assertEqual(result, "Lion makes Rawr!")

    def test_get_kingdom(self):
        mammal = Mammal("Lion", "carnivore", "Rawr!")
        result = mammal.get_kingdom()
        self.assertEqual(result, "animals")

    def test_info_method(self):
        mammal = Mammal("Lion", "carnivore", "Rawr!")
        result = mammal.info()
        self.assertEqual(result, "Lion is of type carnivore")


if __name__ == "__main__":
    unittest.main()
