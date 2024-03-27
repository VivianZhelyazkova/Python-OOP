from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    VALID_ASTRONAUTS = {
        "Biologist": Biologist,
        "Geodesist": Geodesist,
        "Meteorologist": Meteorologist
    }

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.number_of_successful_missions = 0
        self.number_of_not_completed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in SpaceStation.VALID_ASTRONAUTS:
            raise Exception("Astronaut type is not valid!")
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut:
            return f"{name} is already added."
        astronaut = SpaceStation.VALID_ASTRONAUTS[astronaut_type](name)
        self.astronaut_repository.add(astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        planet = self.planet_repository.find_by_name(name)
        if planet:
            return f"{name} is already added."
        planet = Planet(name)
        planet.items += items.split(", ")
        self.planet_repository.add(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception("Astronaut {astronaut_name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise "Invalid planet name!"
        suitable = [astronaut for astronaut in self.astronaut_repository.astronauts if astronaut.oxygen > 30]
        if not suitable:
            raise Exception("You need at least one astronaut to explore the planet!")
        suitable = sorted(suitable, key=lambda x: -x.oxygen)
        if len(suitable) > 5:
            suitable = suitable[:5]
        count = 0
        while suitable and planet.items:
            count += 1
            current_astronaut = suitable.pop()
            while planet.items:
                current_item = planet.items.pop()
                current_astronaut.breathe()
                current_astronaut.backpack.append(current_item)
                if current_astronaut.oxygen <= 0:
                    break
        if planet.items:
            self.number_of_not_completed_missions += 1
            return "Mission is not completed."
        self.number_of_successful_missions += 1
        return f"Planet: {planet_name} was explored. {count} astronauts participated in collecting items."

    def report(self):
        result = (f"{self.number_of_successful_missions} successful missions!\n"
                  f"{self.number_of_not_completed_missions} missions were not completed!\n"
                  f"Astronauts' info:\n")
        for astronaut in self.astronaut_repository.astronauts:
            result += (f"Name: {astronaut.name}\n"
                       f"Oxygen: {astronaut.oxygen}\n"
                       f"Backpack items: {', '.join(astronaut.backpack) if astronaut.backpack else 'none'}\n")
        return result
