from project.booths.booth import Booth


class OpenBooth(Booth):
    PRICE = 2.50

    def reserve(self, number_of_people: int):
        price_for_reservation = OpenBooth.PRICE * number_of_people
        self.price_for_reservation = price_for_reservation
        self.is_reserved = True
