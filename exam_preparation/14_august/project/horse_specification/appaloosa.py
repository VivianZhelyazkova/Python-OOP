from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120

    def __init__(self, name: str, speed: int):
        if speed > Appaloosa.MAX_SPEED:
            raise ValueError("Horse speed is too high!")
        super().__init__(name, speed)

    def train(self):
        self.speed += 2
        if self.speed > Appaloosa.MAX_SPEED:
            self.speed = Appaloosa.MAX_SPEED

