from typing import List

from project.booths.booth import Booth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    DELICACIES = {
        "Gingerbread": Gingerbread,
        "Stolen": Stolen,
    }

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        if type_delicacy not in ChristmasPastryShopApp.DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        search_delicacy = next(
            (delicacy for delicacy in self.delicacies if delicacy.__class__.__name__ == type_delicacy), None)
        if search_delicacy:
            raise Exception(f"{type_delicacy} already exists!")
        delicacy = ChristmasPastryShopApp.DELICACIES[type_delicacy](name, price)
        self.delicacies.append(delicacy)
        return f"Added delicacy {delicacy.name} - {type_delicacy} to the pastry shop."
