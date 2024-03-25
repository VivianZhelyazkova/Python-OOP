from project.car.car import Car


class MuscleCar(Car):
    MAX = 450
    MIN = 250

    def __init__(self, model: str, speed_limit: int):
        if speed_limit not in range(MuscleCar.MIN, MuscleCar.MAX + 1):
            raise ValueError(f"Invalid speed limit! Must be between {MuscleCar.MIN} and {MuscleCar.MAX}!")
        self.speed_limit = speed_limit
        super().__init__(model, speed_limit)



