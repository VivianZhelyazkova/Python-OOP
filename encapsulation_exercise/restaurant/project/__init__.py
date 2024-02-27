# zero test
from project.product import Product
from project.beverage.beverage import Beverage

import unittest

class Tests(unittest.TestCase):
    def test(self):
        product = Product("coffee", 2.5)
        self.assertEqual(product.__class__.__name__, "Product")
        self.assertEqual(product.name, "coffee")
        self.assertEqual(product.price, 2.5)
        beverage = Beverage("coffee", 2.5, 50)
        self.assertEqual(beverage.__class__.__name__, "Beverage")
        self.assertEqual(beverage.__class__.__bases__[0].__name__, "Product")
        self.assertEqual(beverage.name, "coffee")
        self.assertEqual(beverage.price, 2.5)
        self.assertEqual(beverage.milliliters, 50)


if __name__ == "__main__":
    unittest.main()