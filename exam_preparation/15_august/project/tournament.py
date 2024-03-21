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
        if not all(char.isalnum() or char.isspace() for char in value):
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
