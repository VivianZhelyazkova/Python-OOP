from typing import List

from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply


class Controller:
    VALID_SUSTENANCE_TYPES = {
        "Food": Food,
        "Drink": Drink,
    }

    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *args):
        added_names = []
        for player in args:
            if player not in self.players:
                self.players.append(player)
                added_names.append(player.name)
        return f"Successfully added: {', '.join(added_names)}"

    def add_supply(self, *args):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        player = next((player for player in self.players if player_name == player.name), None)
        if not player:
            return
        if not player.need_sustenance:
            return f"{player_name} have enough stamina."
        if sustenance_type not in Controller.VALID_SUSTENANCE_TYPES:
            return
        needed_supplies = [supply for supply in self.supplies if sustenance_type == supply.__class__.__name__]
        if not needed_supplies:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")
        supply = needed_supplies.pop()
        reversed_supps = list(reversed(self.supplies))
        reversed_supps.remove(supply)
        self.supplies = list(reversed(reversed_supps))
        player.stamina += supply.energy
        if player.stamina > 100:
            player.stamina = 100
        return f"{player_name} sustained successfully with {supply.name}."

    def check_winner(self, player1, player2):
        if player1.stamina <= 0:
            winner = player2
            player1.stamina = 0
            return f"Winner: {winner.name}"

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = next(player for player in self.players if player.name == first_player_name)
        player2 = next(player for player in self.players if player.name == second_player_name)
        result = ""
        if player1.stamina == 0:
            result += f"Player {player1.name} does not have enough stamina.\n"
        if player2.stamina == 0:
            result += f"Player {player2.name} does not have enough stamina."
        if result:
            return result.strip()
        first = player1 if player1.stamina < player2.stamina else player2
        second = player1 if player1.stamina > player2.stamina else player2
        second.stamina -= first.stamina / 2
        result = self.check_winner(second, first)
        if result:
            return result
        first.stamina -= second.stamina / 2
        result = self.check_winner(first, second)
        if result:
            return result
        winner = player1 if player1.stamina > player2.stamina else player2
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - player.age * 2 < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = [player.__str__() for player in self.players]
        result += [supply.details() for supply in self.supplies]
        return "\n".join(result)
