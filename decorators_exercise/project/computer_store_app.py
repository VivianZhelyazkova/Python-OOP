from typing import List
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop

from project.computer_types.computer import Computer


def validate_computer_type(func):
    def wrapper(*args, **kwargs):
        _, type_comp, manufacturer, model, processor, ram = args
        if type_comp != "Desktop Computer" and type_comp != "Laptop":
            raise ValueError(f"{type_comp} is not a valid type computer!")
        if type_comp == "Desktop Computer":
            type_comp = "DesktopComputer"
        return func(_, type_comp, manufacturer, model, processor, ram)

    return wrapper


class ComputerStoreApp:
    def __init__(self):
        self.warehouse: List[Computer] = []
        self.profits = 0

    @validate_computer_type
    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        comp = eval(type_computer)(manufacturer, model)
        result = comp.configure_computer(processor, ram)
        self.warehouse.append(comp)
        return result

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        price_filter = list(filter(lambda x: x.price <= client_budget, self.warehouse))
        processor_filter = list(filter(lambda x: x.processor == wanted_processor, price_filter))
        ram_filter = list(filter(lambda x: x.ram >= wanted_ram, processor_filter))
        if not ram_filter:
            raise Exception("Sorry, we don't have a computer for you.")
        comp_for_sale = ram_filter[0]
        self.profits += client_budget - comp_for_sale.price
        self.warehouse.remove(comp_for_sale)
        return f"{comp_for_sale} sold for {client_budget}$."
