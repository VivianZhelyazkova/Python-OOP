from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    INITIAL_OXYGEN = 50

    def __init__(self, name: str):
        super().__init__(name, Geodesist.INITIAL_OXYGEN)

    def breathe(self):
        super().breathe()
