from project.bookstore import Bookstore
import unittest


class TestBookstore(unittest.TestCase):
    def setUp(self):
        self.bookstore = Bookstore(2)

    def test_init(self):
        expected = [2, {}, 0]
        actual = [self.bookstore.books_limit, self.bookstore.availability_in_store_by_book_titles,
                  self.bookstore.total_sold_books]
        self.assertEqual(expected, actual)

    def test_books_limit_raises(self):
        with self.assertRaises(ValueError) as error:
            self.bookstore.books_limit = 0
        self.assertEqual(str(error.exception), f"Books limit of 0 is not valid")

    def test_books_limit(self):
        self.bookstore.books_limit = 3
        expected = 3
        actual = self.bookstore.books_limit
        self.assertEqual(expected, actual)

    def test_len(self):
        self.bookstore.availability_in_store_by_book_titles = {"hell": 1, "heaven": 1}
        expected = 2
        actual = len(self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(expected, actual)

    def test_receive_book_no_space(self):
        with self.assertRaises(Exception) as error:
            self.bookstore.receive_book("heaven", 3)
        self.assertEqual(str(error.exception), "Books limit is reached. Cannot receive more books!")

    def test_receive_book_enough_space(self):
        actual_return = self.bookstore.receive_book("heaven", 1)
        expected_return = f"1 copies of heaven are available in the bookstore."
        expected = {"heaven": 1}
        actual = self.bookstore.availability_in_store_by_book_titles
        self.assertEqual(expected, actual)
        self.assertEqual(expected_return, actual_return)

    def test_sell_book_not_available(self):
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book("hell", 1)
        self.assertEqual(str(error.exception), "Book hell doesn't exist!")

    def test_sell_book_not_enough(self):
        self.bookstore.receive_book("hell", 1)
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book("hell", 2)
        self.assertEqual(str(error.exception), "hell has not enough copies to sell. Left: 1")

    def test_sell_book_successfully(self):
        self.bookstore.receive_book("heaven", 1)
        expected_return = "Sold 1 copies of heaven"
        actual_return = self.bookstore.sell_book("heaven", 1)
        self.assertEqual(expected_return, actual_return)
        expected_sold = 1
        actual_sold = self.bookstore.total_sold_books
        self.assertEqual(expected_sold, actual_sold)
        expected_availability = {"heaven": 0}
        actual_availability = self.bookstore.availability_in_store_by_book_titles
        self.assertEqual(expected_availability, actual_availability)

    def test_str(self):
        self.bookstore.receive_book("heaven", 1)
        expected = ("Total sold books: 0\n"
                    "Current availability: 1\n"
                    " - heaven: 1 copies")
        actual = self.bookstore.__str__()
        self.assertEqual(actual, expected)
