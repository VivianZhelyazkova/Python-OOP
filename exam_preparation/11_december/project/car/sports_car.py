from project.car.car import Car


class SportsCar(Car):
    MAX = 600
    MIN = 400

    def __init__(self, model: str, speed_limit: int):
        if speed_limit not in range(SportsCar.MIN, SportsCar.MAX + 1):
            raise ValueError(f"Invalid speed limit! Must be between {SportsCar.MIN} and {SportsCar.MAX}!")
        self.speed_limit = speed_limit
        super().__init__(model, speed_limit)
