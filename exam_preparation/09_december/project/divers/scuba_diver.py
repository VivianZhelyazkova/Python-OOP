from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    OXYGEN_LEVEL = 540

    def __init__(self, name: str):
        super().__init__(name, ScubaDiver.OXYGEN_LEVEL)

    def miss(self, time_to_catch: int):
        if round(self.oxygen_level - (time_to_catch * 0.3)) < 0:
            self.oxygen_level = 0
        else:
            self.oxygen_level = round(self.oxygen_level - (time_to_catch * 0.3))

    def renew_oxy(self):
        self.oxygen_level = ScubaDiver.OXYGEN_LEVEL
