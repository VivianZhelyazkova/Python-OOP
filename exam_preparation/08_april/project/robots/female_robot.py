from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    INITIAL_WEIGHT = 7
    WEIGHT_GAIN = 1

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, FemaleRobot.INITIAL_WEIGHT)
        self.available_service = "SecondaryService"

    def eating(self):
        self.weight += FemaleRobot.WEIGHT_GAIN
