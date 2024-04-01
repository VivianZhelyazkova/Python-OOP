from typing import List

from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.horse import Horse
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    HORSE_TYPES = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred,
    }
    HORSE_RACES = {"Winter": 0,
                   "Spring": 0,
                   "Autumn": 0,
                   "Summer": 0
                   }

    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in HorseRaceApp.HORSE_TYPES:
            return
        existing_horse = next((horse for horse in self.horses if horse.name == horse_name), None)
        if existing_horse:
            raise Exception(f"Horse {horse_name} has been already added!")
        horse = HorseRaceApp.HORSE_TYPES[horse_type](horse_name, horse_speed)
        self.horses.append(horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        existing_jockey = next((jockey for jockey in self.jockeys if jockey.name == jockey_name), None)
        if existing_jockey:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        if HorseRaceApp.HORSE_RACES[race_type]:
            raise Exception(f"Race {race_type} has been already created!")
        race = HorseRace(race_type)
        HorseRaceApp.HORSE_RACES[race_type] = 1
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = next((jockey for jockey in self.jockeys if jockey.name == jockey_name), None)
        available_horses = [horse for horse in self.horses if
                            horse.__class__.__name__ == horse_type and not horse.is_taken]
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if not available_horses:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."
        horse = available_horses.pop()
        horse.is_taken = True
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        horse_race = next((race for race in self.horse_races if race_type == race.race_type), None)
        jockey = next((jockey for jockey in self.jockeys if jockey.name == jockey_name), None)
        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        horse_race = next((race for race in self.horse_races if race_type == race.race_type), None)
        if not horse_race:
            raise Exception(f"Race {race_type} could not be found!")
        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")
        winner = list(sorted(horse_race.jockeys, key=lambda j: j.horse.speed))[-1]
        return f"The winner of the {race_type} race, with a speed of {winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."
