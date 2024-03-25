from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, SecondaryService.CAPACITY)

    def details(self):
        if self.robots:
            robots = " ".join([robot.name for robot in self.robots])
        else:
            robots = "none"
        result = f"{self.name} Secondary Service:\nRobots: {robots}"
        return result
