class Player:
    _unique_names = set()

    def __init__(self, name: str, age: int, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina
        self.__need_sustenance = stamina < 100

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name not valid!")
        if value in Player._unique_names:
            raise ValueError(F"Name {value} is already used!")
        self.__name = value
        Player._unique_names.add(self.name)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < 0 or value > 100:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.stamina < 100

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
