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
            if any(car.model == model for car in self.cars):
                raise ValueError(f"Car {model} is already created!")
            car = Controller.AVAILABLE_CAR_TYPES[car_type](model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if any(driver.name == driver_name for driver in self.drivers):
            raise ValueError(f"Driver {driver_name} is already created!")
        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if any(race.name == race_name for race in self.races):
            raise ValueError(f"Race {race_name} is already created!")
        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = next((driver for driver in self.drivers if driver.name == driver_name), None)
        if not driver:
            raise ValueError(f"Driver {driver_name} could not be found!")

        car = next((car for car in self.cars if
                    isinstance(car, Controller.AVAILABLE_CAR_TYPES[car_type]) and not car.is_taken), None)
        if not car:
            raise ValueError(f"No available {car_type} found for {driver_name}!")

        if driver.car:
            driver.car.is_taken = False
        car.is_taken = True
        driver.car = car
        return f"Driver {driver_name} chose the {car_type} {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = next((race for race in self.races if race.name == race_name), None)
        if not race:
            raise ValueError(f"Race {race_name} could not be found!")

        driver = next((driver for driver in self.drivers if driver.name == driver_name), None)
        if not driver:
            raise ValueError(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise ValueError(f"Driver {driver_name} does not have a car to participate in {race_name}!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added to {race_name} race."

    def start_race(self, race_name: str):
        race = next((race for race in self.races if race.name == race_name), None)
        if not race:
            raise ValueError(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise ValueError(f"Race {race_name} cannot start with less than 3 participants!")

        race_results = sorted(race.drivers, key=lambda driver: -driver.car.speed_limit)[:3]
        for position, driver in enumerate(race_results, start=1):
            driver.number_of_wins += 1
            result = f"{position}st" if position == 1 else f"{position}nd" if position == 2 else f"{position}rd"
            result += f" place: Driver {driver.name} with car {driver.car.model} at {driver.car.speed_limit} speed."
            race_results[position - 1] = result
        return "\n".join(race_results)
