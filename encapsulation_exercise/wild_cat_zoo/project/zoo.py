class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__budget < price and self.__animal_capacity > len(self.animals):
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = 0
        for worker in self.workers:
            total_salaries += worker.salary
        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_care_money = 0
        for animal in self.animals:
            total_care_money += animal.money_for_care
        if self.__budget >= total_care_money:
            self.__budget -= total_care_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        lions = list(filter(lambda x: x.__class__.__name__ == "Lion", self.animals))
        tigers = list(filter(lambda x: x.__class__.__name__ == "Tiger", self.animals))
        cheetahs = list(filter(lambda x: x.__class__.__name__ == "Cheetah", self.animals))
        result += f"----- {len(lions)} Lions:"
        for lion in lions:
            result += "\n" + lion.__repr__()
        result += f"\n----- {len(tigers)} Tigers:"
        for tiger in tigers:
            result += "\n" + tiger.__repr__()
        result += f"\n----- {len(cheetahs)} Cheetahs:"
        for cheetah in cheetahs:
            result += "\n" + cheetah.__repr__()
        return result
    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        keepers = list(filter(lambda x: x.__class__.__name__ == "Keeper", self.workers))
        caretakers = list(filter(lambda x: x.__class__.__name__ == "Caretaker", self.workers))
        vets = list(filter(lambda x: x.__class__.__name__ == "Vet", self.workers))
        result += f"----- {len(keepers)} Keepers:"
        for keeper in keepers:
            result += "\n" + keeper.__repr__()
        result += f"\n----- {len(caretakers)} Caretakers:"
        for caretaker in caretakers:
            result += "\n" + caretaker.__repr__()
        result += f"\n----- {len(vets)} Vets:"
        for vet in vets:
            result += "\n" + vet.__repr__()
        return result