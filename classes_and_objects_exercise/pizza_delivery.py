class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        self.ingredients[ingredient] = self.ingredients.get(ingredient, 0) + quantity
        self.price += price_per_quantity * quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if not self.ingredients.get(ingredient):
            return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
        elif quantity > self.ingredients[ingredient]:
            return f"Please check again the desired quantity of {ingredient}!"
        self.ingredients[ingredient] -= quantity
        self.price -= quantity * price_per_quantity

    def make_order(self):
        self.ordered = True
        result = ""
        result += f"You've ordered pizza {self.name} prepared with "
        for ingredient, quantity in self.ingredients.items():
            result += f"{ingredient}: {quantity}, "
        result = result.rstrip(", ")
        result += f" and the price will be {self.price}lv."
        return result
