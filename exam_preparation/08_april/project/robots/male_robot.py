from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    INITIAL_WEIGHT = 9
    WEIGHT_GAIN = 3

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, MaleRobot.INITIAL_WEIGHT)
        self.available_service = "MainService"

    def eating(self):
        self.weight += MaleRobot.WEIGHT_GAIN
