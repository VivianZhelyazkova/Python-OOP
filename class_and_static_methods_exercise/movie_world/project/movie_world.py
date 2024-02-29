from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = next((x for x in self.customers if x.id == customer_id), None)
        dvd = next((x for x in self.dvds if x.id == dvd_id), None)
        customer_dvd = next((x for x in customer.rented_dvds if x.id == dvd_id), None)
        if customer_dvd:
            return f"{customer.name} has already rented {dvd.name}"
        else:
            if dvd.is_rented:
                return "DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = next((x for x in self.customers if x.id == customer_id), None)
        dvd = next((x for x in self.dvds if x.id == dvd_id), None)
        customer_dvd = next((x for x in customer.rented_dvds if x.id == dvd_id), None)
        if customer_dvd:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ""
        for customer in self.customers:
            result += customer.__repr__() + "\n"
        for dvd in self.dvds:
            result += dvd.__repr__() + "\n"
        return result.rstrip()
