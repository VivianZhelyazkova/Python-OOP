class Customer:
    def __init__(self, name: str, age: int, _id: int):
        self.name = name
        self.age = age
        self.id = _id
        self.rented_dvds = []

    def __repr__(self):
        result = ""
        for dvd in self.rented_dvds:
            result += dvd.name + ", "
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ({result.rstrip(', ')})"
