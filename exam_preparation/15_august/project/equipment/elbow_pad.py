from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    PROTECTION = 90
    PRICE = 25.0

    def __init__(self):
        super().__init__(ElbowPad.PROTECTION, ElbowPad.PRICE)

    def increase_price(self):
        self.price *= 1.10



