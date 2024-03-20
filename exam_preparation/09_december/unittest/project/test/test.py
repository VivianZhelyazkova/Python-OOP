from collections import deque

from project.railway_station import RailwayStation
import unittest


class TestRailwayStation(unittest.TestCase):
    def setUp(self):
        self.station = RailwayStation("Neshto")

    def test_init(self):
        expected = ["Neshto", deque([]), deque([])]
        actual = [self.station.name, self.station.arrival_trains, self.station.departure_trains]
        self.assertEqual(expected, actual)

    def test_init_raises(self):
        with self.assertRaises(ValueError) as error:
            RailwayStation("N")
        self.assertEqual(str(error.exception), "Name should be more than 3 symbols!")

    def test_name_setter_raises(self):
        with self.assertRaises(ValueError) as error:
            self.station.name = "N"
        self.assertEqual(str(error.exception), "Name should be more than 3 symbols!")

    def test_name_setter(self):
        self.station.name = "Pesho"
        expected = "Pesho"
        actual = self.station.name
        self.assertEqual(expected, actual)

    def test_new_arrival(self):
        self.station.new_arrival_on_board("some info")
        expected = deque(["some info"])
        actual = self.station.arrival_trains
        self.assertEqual(expected, actual)

    def test_train_arrived_not_first_in_que(self):
        self.station.new_arrival_on_board("some info")
        self.station.new_arrival_on_board("Other info")
        actual = self.station.train_has_arrived("Other info")
        expected = f"There are other trains to arrive before Other info."
        self.assertEqual(expected, actual)

    def test_train_arrived_first_in_que(self):
        self.station.new_arrival_on_board("Other info")
        actual_return = self.station.train_has_arrived("Other info")
        expected_return = f"Other info is on the platform and will leave in 5 minutes."
        expected = deque(["Other info"])
        actual = self.station.departure_trains
        self.assertEqual(expected, actual)
        self.assertEqual(expected_return, actual_return)

    def test_train_has_left_true(self):
        self.station.new_arrival_on_board("Other info")
        self.station.train_has_arrived("Other info")
        actual_return = self.station.train_has_left("Other info")
        expected_return = True
        expected = deque([])
        actual = self.station.departure_trains
        self.assertEqual(expected, actual)
        self.assertEqual(expected_return, actual_return)

    def test_train_has_left_false(self):
        self.station.new_arrival_on_board("Other info")
        self.station.train_has_arrived("Other info")
        actual_return = self.station.train_has_left(" info")
        expected_return = False
        expected = deque(["Other info"])
        actual = self.station.departure_trains
        self.assertEqual(expected, actual)
        self.assertEqual(expected_return, actual_return)



