import abc


class BaseEquipment(abc.ABC):
    def __init__(self, protection: int, price: float):
        self.protection = protection
        self.price = price

    @abc.abstractmethod
    def increase_price(self):
        pass
