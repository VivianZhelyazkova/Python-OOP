from typing import List

from project.equipment.base_equipment import BaseEquipment
from project.teams.base_team import BaseTeam
from project.equipment.knee_pad import KneePad
from project.equipment.elbow_pad import ElbowPad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type != "KneePad" and equipment_type != "ElbowPad":
            raise Exception("Invalid equipment type!")
        eq = eval(equipment_type)()
        self.equipment.append(eq)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type != "OutdoorTeam" and team_type != "IndoorTeam":
            raise Exception("Invalid team type!")
        if self.capacity == len(self.teams):
            return "Not enough tournament capacity."
        team = eval(team_type)(team_name, country, advantage)
        self.teams.append(team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        equipment_list = [obj for obj in self.equipment if obj.__class__.__name__ == equipment_type]
        equipment = equipment_list[-1]
        team = next((obj for obj in self.teams if obj.name == team_name), None)
        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")
        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = next((obj for obj in self.teams if obj.name == team_name), None)
        if not team:
            raise Exception("No such team!")
        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        count = 0
        for item in self.equipment:
            if item.__class__.__name__ == equipment_type:
                item.increase_price()
                count += 1
        return f"Successfully changed {count}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        first = next((obj for obj in self.teams if obj.name == team_name1), None)
        second = next((obj for obj in self.teams if obj.name == team_name2), None)
        if first.__class__.__name__ != second.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")
        first_score = sum(x.protection for x in first.equipment) + first.advantage
        second_score = sum(x.protection for x in second.equipment) + second.advantage
        if first_score > second_score:
            first.win()
            return f"The winner is {team_name1}."
        elif first_score < second_score:
            second.win()
            return f"The winner is {team_name2}."
        else:
            return "No winner in this game."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda x: -x.wins)
        result = f"Tournament: {self.name}\nNumber of Teams: {len(self.teams)}\nTeams:"
        for team in sorted_teams:
            result += "\n" + team.get_statistics()
        return result
