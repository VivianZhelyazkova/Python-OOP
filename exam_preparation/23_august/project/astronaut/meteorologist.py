from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    INITIAL_OXYGEN = 90
    ADDITIONAL_OXYGEN_CONSUMPTION = 15

    def __init__(self, name: str):
        super().__init__(name, Meteorologist.INITIAL_OXYGEN)

    def breathe(self):
        super().breathe()
        self.oxygen -= Meteorologist.ADDITIONAL_OXYGEN_CONSUMPTION
