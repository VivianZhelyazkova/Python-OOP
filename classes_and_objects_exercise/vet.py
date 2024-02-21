class Vet:
    animals = []
    space = 5

    def __init__(self, name):
        self.name = name
        self.animals = []

    def register_animal(self, animal_name):
        if not Vet.space:
            return f"Not enough space"
        Vet.animals.append(animal_name)
        self.animals.append(animal_name)
        Vet.space -= 1
        return f"{animal_name} registered in the clinic"

    def unregister_animal(self, animal_name):
        if animal_name not in Vet.animals:
            return f"{animal_name} not in the clinic"
        Vet.animals.remove(animal_name)
        self.animals.remove(animal_name)
        Vet.space += 1
        return f"{animal_name} unregistered successfully"

    def info(self):
        return f"{self.name} has {len(self.animals)} animals. {Vet.space} space left in clinic"

