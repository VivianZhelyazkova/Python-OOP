from project.supply.supply import Supply


class Food(Supply):
    ENERGY = 25

    def __init__(self, name: str):
        super().__init__(name, Food.ENERGY)

    def details(self):
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"
