from typing import List

from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    MUSICIANS = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ConcertTrackerApp.MUSICIANS:
            raise ValueError("Invalid musician type!")
        searched_musician = next((musician for musician in self.musicians if musician.name == name), None)
        if searched_musician:
            raise Exception(f"{name} is already a musician!")
        musician = ConcertTrackerApp.MUSICIANS[musician_type](name, age)
        self.musicians.append(musician)
        return f"{musician.name} is now a {musician_type}."

    def create_band(self, name: str):
        searched_band = next((band for band in self.bands if band.name == name), None)
        if searched_band:
            raise Exception(f"{name} band is already created!")
        band = Band(name)
        self.bands.append(band)
        return f"{band.name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        searched_concert = next((con for con in self.concerts if con.place == place), None)
        if searched_concert:
            raise Exception(f"{place} is already registered for {searched_concert.genre} concert!")
        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{concert.genre} concert in {concert.place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = next((musician for musician in self.musicians if musician.name == musician_name), None)
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")
        band = next((band for band in self.bands if band.name == band_name), None)
        if not band:
            raise Exception(f"{band_name} isn't a band!")
        band.members.append(musician)
        band.musicians[musician.__class__.__name__] += 1
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = next((band for band in self.bands if band.name == band_name), None)
        if not band:
            raise Exception(f"{band_name} isn't a band!")
        musician = next((musician for musician in band.members if musician.name == musician_name), None)
        if not musician:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):

