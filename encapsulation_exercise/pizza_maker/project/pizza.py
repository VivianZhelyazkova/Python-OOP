from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, max_number_of_toppings: int):
        self.validate_name(name)
        self.validate_dough(dough)
        self.validate_max_toppings(max_number_of_toppings)

        self.name = name
        self.dough = dough
        self.max_number_of_toppings = max_number_of_toppings
        self.toppings = {}
        self.topping_counter = 0

    def validate_name(self, name):
        if name == "":
            raise ValueError("The name cannot be an empty string")

    def validate_dough(self, dough):
        if not dough:
            raise ValueError("You should add dough to the pizza")

    def validate_max_toppings(self, max_num_of_toppings):
        if max_num_of_toppings <= 0:
            raise ValueError("The maximum number of toppings cannot be less or equal to zero")

    def add_topping(self, topping: Topping):
        if self.max_number_of_toppings <= self.topping_counter:
            raise ValueError("Not enough space for another topping")
        else:
            if topping.topping_type in self.toppings:
                self.toppings[topping.topping_type] += topping.weight
            else:
                self.toppings[topping.topping_type] = topping.weight
        self.topping_counter += 1

    def calculate_total_weight(self):
        return sum(self.toppings.values()) + self.dough.weight
