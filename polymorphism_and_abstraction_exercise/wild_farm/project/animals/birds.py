from project.animals.animal import Bird
from project.food import Food


class Owl(Bird):
    weight_gain_per_food = 0.25

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food: Food):
        if food.__class__.__name__ == "Meat":
            self.weight += Owl.weight_gain_per_food * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Hen(Bird):
    weight_gain_per_food = 0.35

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food: Food):
        self.food_eaten += food.quantity
        self.weight += Hen.weight_gain_per_food * food.quantity
