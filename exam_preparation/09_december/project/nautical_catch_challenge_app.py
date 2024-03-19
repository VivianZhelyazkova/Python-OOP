from typing import List
from project.divers.scuba_diver import ScubaDiver
from project.divers.free_diver import FreeDiver
from project.divers.base_diver import BaseDiver
from project.fish.base_fish import BaseFish
from project.fish.predatory_fish import PredatoryFish
from project.fish.deep_sea_fish import DeepSeaFish


class NauticalCatchChallengeApp:
    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        searched_diver = next((diver for diver in self.divers if diver.name == diver_name), None)
        if searched_diver:
            return f"{diver_name} is already a participant."

        if diver_type == "FreeDiver" or diver_type == "ScubaDiver":
            self.divers.append(eval(diver_type)(diver_name))
            return f"{diver_name} is successfully registered for the competition as a {diver_type}."

        return f"{diver_type} is not allowed in our competition."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        searched_fish = next((fish for fish in self.fish_list if fish_name == fish.name), None)
        if searched_fish:
            return f"{fish_name} is already permitted."
        if fish_type == "PredatoryFish" or fish_type == "DeepSeaFish":
            self.fish_list.append(eval(fish_type)(fish_name, points))
            return f"{fish_name} is allowed for chasing as a {fish_type}."

        return f"{fish_type} is forbidden for chasing in our competition."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = next((diver for diver in self.divers if diver.name == diver_name), None)
        fish = next((fish for fish in self.fish_list if fish_name == fish.name), None)

        if not diver:
            return f"{diver_name} is not registered for the competition."
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.has_health_issue = True
            return f"{diver_name} missed a good {fish_name}."
        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                if diver.oxygen_level == 0:
                    diver.has_health_issue = True
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                if diver.oxygen_level == 0:
                    diver.has_health_issue = True
                return f"{diver_name} missed a good {fish_name}."
        diver.hit(fish)
        return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        divers_recovered = 0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.has_health_issue = False
                diver.renew_oxy()
                divers_recovered += 1
        return f"Divers recovered: {divers_recovered}"

    def diver_catch_report(self, diver_name: str):
        diver = next((diver for diver in self.divers if diver.name == diver_name), None)
        result = f"**{diver_name} Catch Report**"
        for fish in diver.catch:
            result += "\n" + fish.fish_details()
        return result

    def competition_statistics(self):
        good_health_divers = [diver for diver in self.divers if not diver.has_health_issue]
        sorted_divers = sorted(good_health_divers, key=lambda x: (-x.competition_points, -len(x.catch), x.name))
        result = f"**Nautical Catch Challenge Statistics**"
        for diver in sorted_divers:
            result += "\n" + diver.__str__()
        return result
