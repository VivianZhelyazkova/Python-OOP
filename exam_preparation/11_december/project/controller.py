from typing import List

from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    AVAILABLE_CAR_TYPES = {
        "MuscleCar": MuscleCar,
        "SportsCar": SportsCar
    }

    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type in Controller.AVAILABLE_CAR_TYPES:
            searched_car = next((car for car in self.cars if car.model == model), None)
            if searched_car:
                raise Exception(f"Car {model} is already created!")
            car = Controller.AVAILABLE_CAR_TYPES[car_type](model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        searched_driver = next((driver for driver in self.drivers if driver_name == driver.name), None)
        if searched_driver:
            raise Exception(f"Driver {driver_name} is already created!")
        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        searched_race = next((race for race in self.races if race_name == race.name), None)
        if searched_race:
            raise Exception(f"Race {race_name} is already created!")
        race = Race(race_name)
        self.races.append(race)
        return f"Driver {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        car = next((car for car in self.cars if car.__class__.__name__ == car_type and not car.is_taken), None)
        driver = next((driver for driver in self.drivers if driver_name == driver.name), None)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        if not car:
            raise Exception(f"Car {car_type} could not be found!")
        car = [car for car in self.cars if car.__class__.__name__ == car_type and not car.is_taken][-1]
        if driver.car:
            driver.car.is_taken = False
            old_model = driver.car.model
            driver.car = car
            car.is_taken = True
            return f"Driver {driver.name} changed his car from {old_model} to {car.model}."
        car.is_taken = True
        driver.car = car
        return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        driver = next((driver for driver in self.drivers if driver_name == driver.name), None)
        race = next((race for race in self.races if race_name == race.name), None)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = next((race for race in self.races if race_name == race.name), None)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        winners = sorted(race.drivers, key=lambda driver: -driver.car.speed_limit)
        first = winners[0]
        second = winners[1]
        third = winners[2]
        first.number_of_wins += 1
        second.number_of_wins += 1
        third.number_of_wins += 1
        result = f"Driver {first.name} wins the {race_name} race with a speed of {first.car.speed_limit}."
        result += f"\nDriver {second.name} wins the {race_name} race with a speed of {second.car.speed_limit}."
        result += f"\nDriver {third.name} wins the {race_name} race with a speed of {third.car.speed_limit}."
        return result
