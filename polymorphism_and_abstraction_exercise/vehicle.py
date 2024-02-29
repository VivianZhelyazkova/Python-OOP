import abc


class Vehicle(abc.ABC):

    @abc.abstractmethod
    def drive(self, distance):
        pass

    @abc.abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        fuel_needed_to_drive = distance * (self.fuel_consumption + 0.9)
        if self.fuel_quantity >= fuel_needed_to_drive:
            self.fuel_quantity -= fuel_needed_to_drive

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        fuel_needed_to_drive = distance * (self.fuel_consumption + 1.6)
        if self.fuel_quantity >= fuel_needed_to_drive:
            self.fuel_quantity -= fuel_needed_to_drive

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95
