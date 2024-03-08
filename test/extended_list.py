import unittest


class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


class IntegerListTests(unittest.TestCase):

    def test_add_element_and_returns_list(self):
        some_list = IntegerList(1, 2, 3)
        result = some_list.add(4)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_add_element_raise_error(self):
        some_list = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError) as error:
            some_list.add("a")
        self.assertEqual(str(error.exception), "Element is not Integer")

    def test_remove_index_and_returns_it(self):
        some_list = IntegerList(1, 2, 3)
        removed_element = some_list.remove_index(0)
        self.assertEqual(removed_element, 1)
        result = some_list.get_data()
        self.assertEqual(result, [2, 3])

    def test_remove_index_out_of_range_error(self):
        some_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as error:
            some_list.remove_index(4)
        self.assertEqual(str(error.exception), "Index is out of range")

    def test_init_takes_only_ints_and_stores_them(self):
        some_list = IntegerList(1, 2, 3, "foo", "bar")
        result = some_list.get_data()
        self.assertEqual(result, [1, 2, 3])

    def test_get_returns_specified_element(self):
        some_list = IntegerList(1, 2, 3)
        result = some_list.get(0)
        self.assertEqual(result, 1)

    def test_get_raises_error_when_out_of_range(self):
        some_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as error:
            some_list.get(4)
        self.assertEqual(str(error.exception), "Index is out of range")

    def test_insert_element_on_given_index(self):
        some_list = IntegerList(1, 2, 3)
        some_list.insert(0, 0)
        result = some_list.get_data()
        self.assertEqual(result, [0, 1, 2, 3])

    def test_insert_raises_error_when_out_of_range(self):
        some_list = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as error:
            some_list.insert(6, 6)
        self.assertEqual(str(error.exception), "Index is out of range")

    def test_insert_raises_error_when_element_not_int(self):
        some_list = IntegerList(1, 2, 3)
        with self.assertRaises(ValueError) as error:
            some_list.insert(2, "foo")
        self.assertEqual(str(error.exception), "Element is not Integer")

    def test_get_biggest(self):
        some_list = IntegerList(1, 2, 3)
        result = some_list.get_biggest()
        self.assertEqual(result, 3)

    def test_get_index(self):
        some_list = IntegerList(1, 2, 3)
        result = some_list.get_index(1)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
