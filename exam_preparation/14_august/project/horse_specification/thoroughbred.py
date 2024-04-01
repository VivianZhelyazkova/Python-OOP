from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140

    def __init__(self, name: str, speed: int):
        if speed > Thoroughbred.MAX_SPEED:
            raise ValueError("Horse speed is too high!")
        super().__init__(name, speed)

    def train(self):
        self.speed += 3
        if self.speed > Thoroughbred.MAX_SPEED:
            self.speed = Thoroughbred.MAX_SPEED

