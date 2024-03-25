from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name: str):
        super().__init__(name, MainService.CAPACITY)

    def details(self):
        if self.robots:
            robots = " ".join([robot.name for robot in self.robots])
        else:
            robots = "none"
        result = f"{self.name} Main Service:\nRobots: {robots}"
        return result
