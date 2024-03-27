from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    INITIAL_OXYGEN = 70
    ADDITIONAL_OXYGEN_CONSUMPTION = 5

    def __init__(self, name: str):
        super().__init__(name, Biologist.INITIAL_OXYGEN)

    def breathe(self):
        super().breathe()
        self.oxygen -= Biologist.ADDITIONAL_OXYGEN_CONSUMPTION
