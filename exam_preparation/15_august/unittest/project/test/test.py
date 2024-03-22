from project.trip import Trip
import unittest


class TestTrip(unittest.TestCase):
    def setUp(self):
        self.trip = Trip(1000, 2, True)

    def test_init(self):
        expected = [1000, 2, True, {}]
        actual = [self.trip.budget, self.trip.travelers, self.trip.is_family,
                  self.trip.booked_destinations_paid_amounts]
        self.assertEqual(expected, actual)

    def test_travelers_setter_raises(self):
        with self.assertRaises(ValueError) as error:
            self.trip.travelers = 0
        self.assertEqual(str(error.exception), 'At least one traveler is required!')

    def test_travelers_setter(self):
        self.trip.travelers = 4
        expected = 4
        actual = self.trip.travelers
        self.assertEqual(expected, actual)

    def test_is_family_setter_false(self):
        self.trip.travelers = 1
        self.trip.is_family = True
        expected = False
        actual = self.trip.is_family
        self.assertEqual(expected, actual)

    def test_is_family_true(self):
        self.trip.travelers = 3
        self.trip.is_family = True
        expected = True
        actual = self.trip.is_family
        self.assertEqual(expected, actual)

    def test_book_a_trip_unknown_destination(self):
        actual = self.trip.book_a_trip("htetghe")
        expected = 'This destination is not in our offers, please choose a new one!'
        self.assertEqual(expected, actual)

    def test_book_a_trip_not_enough_money(self):
        actual = self.trip.book_a_trip("Australia")
        expected = 'Your budget is not enough!'
        self.assertEqual(expected, actual)

    def test_book_a_trip_enough_money(self):
        actual_return = self.trip.book_a_trip("Bulgaria")
        expected_return = 'Successfully booked destination Bulgaria! Your budget left is 100.00'
        expected = [{"Bulgaria": 900}, 100]
        actual = [self.trip.booked_destinations_paid_amounts, self.trip.budget]
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected, actual)

    def test_booking_status_no_bookings(self):
        expected = 'No bookings yet. Budget: 1000.00'
        actual = self.trip.booking_status()
        self.assertEqual(expected, actual)

    def test_booking_status(self):
        self.trip.book_a_trip("Bulgaria")
        expected = """Booked Destination: Bulgaria
Paid Amount: 900.00"""
        expected += """\nNumber of Travelers: 2
Budget Left: 100.00"""
        actual = self.trip.booking_status()
        self.assertEqual(expected, actual)
