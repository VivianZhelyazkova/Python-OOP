from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    PROTECTION = 120
    PRICE = 15.0

    def __init__(self):
        super().__init__(KneePad.PROTECTION, KneePad.PRICE)

    def increase_price(self):
        self.price *= 1.20

