import abc
from project.user import User


class Movie(abc.ABC):
    def __init__(self, title: str, owner: object, year: int, age_restriction: int):
        self.__title = title
        self.__year = year
        self.__owner = owner
        self._age_restriction = age_restriction
        self.likes = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if value == "":
            raise ValueError("The title cannot be empty string!")
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value == 1888:
            raise ValueError("Movies weren't made before 1888!")

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, User):
            raise ValueError("The owner must be an object of type User!")
        self.__owner = value

    @property
    def age_restriction(self):
        return self._age_restriction

    @age_restriction.setter
    @abc.abstractmethod
    def age_restriction(self, value):
        pass

    @abc.abstractmethod
    def details(self):
        pass

    def update(self, some_dict):
        for key, value in some_dict.items():
            setattr(self, key, value)
