import abc
from abc import ABC


class Animal(ABC):
    def __init__(self, name: str, age: int, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

    @abc.abstractmethod
    def make_sound(self):
        pass

    @abc.abstractmethod
    def __repr__(self):
        pass
