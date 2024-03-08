import unittest


class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')
        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')
        self.sleepy = False


class CatTests(unittest.TestCase):
    def test_cat_size_increases_after_eating(self):
        cat = Cat("Shadow")
        cat.eat()
        self.assertEqual(cat.size, 1)

    def test_cat_is_fed_after_eating(self):
        cat = Cat("Shadow")
        cat.eat()
        self.assertEqual(cat.fed, True)

    def test_cat_cant_eat_if_fed(self):
        cat = Cat("Shadow")
        cat.eat()
        with self.assertRaises(Exception) as E:
            cat.eat()
        self.assertEqual(str(E.exception), 'Already fed.')

    def test_cat_cant_sleep_if_not_fed(self):
        cat = Cat("Shadow")
        with self.assertRaises(Exception) as E:
            cat.sleep()
        self.assertEqual(str(E.exception), 'Cannot sleep while hungry')

    def test_cat_not_sleepy_after_sleep(self):
        cat = Cat("Shadow")
        cat.eat()
        cat.sleep()
        self.assertEqual(cat.sleepy, False)


if __name__ == '__main__':
    unittest.main()
