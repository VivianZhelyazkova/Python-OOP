from project.booths.booth import Booth


class PrivateBooth(Booth):
    PRICE = 3.50

    def reserve(self, number_of_people: int):
        price_for_reservation = PrivateBooth.PRICE * number_of_people
        self.price_for_reservation = price_for_reservation
        self.is_reserved = True
