class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.__age = age

    def __validate_name(self, name: str):
        if len(name) < 3:
            raise ValueError("name must be at least 3 characters")

    def __validate_age(self, age: int):
        if age < 18:
            raise ValueError("Age must be over 18")

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self, name: str):
        self.__validate_name(name)
        self.__name = name

    @age.setter
    def age(self, age: int):
        self.__validate_age(age)
        self.__age = age


person = Person("e", 54)
print(person.name)
print(person.age)
