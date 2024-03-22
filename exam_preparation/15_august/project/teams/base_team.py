import abc
from typing import List

from project.equipment.base_equipment import BaseEquipment


class BaseTeam(abc.ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment: List[BaseEquipment] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Team name cannot be empty!")
        self.__name = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value.strip()

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @abc.abstractmethod
    def win(self):
        pass

    def get_statistics(self):
        total_price_of_team_equipment = sum([x.price for x in self.equipment])
        if self.equipment:
            avg_team_protection = sum([x.protection for x in self.equipment]) / len(self.equipment)
        else:
            avg_team_protection = 0
        result = (f"Name: {self.name}\n"
                  f"Country: {self.country}\n"
                  f"Advantage: {self.advantage} points\n"
                  f"Budget: {self.budget:.2f}EUR\n"
                  f"Wins: {self.wins}\n"
                  f"Total Equipment Price: {total_price_of_team_equipment:.2f}\n"
                  f"Average Protection: {int(avg_team_protection)}")
        return result


