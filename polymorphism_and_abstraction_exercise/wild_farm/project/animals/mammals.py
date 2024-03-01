from project.animals.animal import Mammal
from project.food import Food


class Mouse(Mammal):
    weight_gain_per_food = 0.10

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food: Food):
        if food.__class__.__name__ == "Vegetable" or food.__class__.__name__ == "Fruit":
            self.weight += Mouse.weight_gain_per_food * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Dog(Mammal):
    weight_gain_per_food = 0.40

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food: Food):
        if food.__class__.__name__ == "Meat":
            self.weight += Dog.weight_gain_per_food * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Cat(Mammal):
    weight_gain_per_food = 0.30

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food: Food):
        if food.__class__.__name__ == "Meat" or food.__class__.__name__ == "Vegetable":
            self.weight += Cat.weight_gain_per_food * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Tiger(Mammal):
    weight_gain_per_food = 1.00

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food: Food):
        if food.__class__.__name__ == "Meat":
            self.weight += Tiger.weight_gain_per_food * food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
