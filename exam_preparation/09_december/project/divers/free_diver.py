from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    OXYGEN_LEVEL = 120

    def __init__(self, name: str):
        super().__init__(name, FreeDiver.OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        if round(self.oxygen_level - (time_to_catch * 0.6)) < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level = round(self.oxygen_level - (time_to_catch * 0.6))


    def renew_oxy(self):
        self.oxygen_level = FreeDiver.OXYGEN_LEVEL


