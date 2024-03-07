# from abc import ABC, abstractmethod
#
#
# class Animal(ABC):
#     def __init__(self, species):
#         self.species = species
#
#     def get_species(self):
#         return self.species
#
#     @abstractmethod
#     def animal_sound(self, ):
#         pass
#
#
# class Dog(Animal):
#
#     def animal_sound(self):
#         return "Woof"
#
#
# class Cat(Animal):
#
#     def animal_sound(self):
#         return "Meow"
#
#
# class Chicken(Animal):
#     def animal_sound(self):
#         return "Cluck"
#
#
# # animals = [Animal('cat'), Animal('dog')]
# # animal_sound(animals)
#
# ## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
# ## при добавяне на нови животни
# animals = [Cat('cat'), Dog('dog'), Chicken('chicken')]
#
# for animal in animals:
#     print(animal.animal_sound())


class Animal:
    def __init__(self, species, sound: str):
        self.species = species
        self.sound = sound

    def get_species(self):
        return self.species


def animal_sound(animals: list):
    for animal in animals:
        print(animal.sound)


animals = [Animal('cat', "meow"), Animal('dog', "woof")]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
