from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak
from project.peaks.arctic_peak import ArcticPeak


class SummitQuestManagerApp:
    def __init__(self):
        self.climbers: List[BaseClimber] = []
        self.peaks: List[BasePeak] = []

    def register_climber(self, climber_type: str, climber_name: str):
        searched_climber = next((x for x in self.climbers if x.name == climber_name), None)
        if searched_climber:
            return f"{climber_name} has been already registered."
        if climber_type == "ArcticClimber" or climber_type == "SummitClimber":
            self.climbers.append(eval(climber_type)(climber_name))
            return f"{climber_name} is successfully registered as a {climber_type}."
        return f"{climber_type} doesn't exist in our register."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type == "ArcticPeak" or peak_type == "SummitPeak":
            self.peaks.append(eval(peak_type)(peak_name, peak_elevation))
            return f"{peak_name} is successfully added to the wish list as a {peak_type}."
        return f"{peak_type} is an unknown type of peak."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        current_peak = next(peak for peak in self.peaks if peak.name == peak_name)
        current_climber = next(climber for climber in self.climbers if climber.name == climber_name)
        current_peak_gear = current_peak.get_recommended_gear()
        if set(current_peak_gear).issubset(set(gear)):
            return f"{climber_name} is prepared to climb {peak_name}."
        current_climber.is_prepared = False
        missing_gear = [el for el in current_peak_gear if el not in gear]
        return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted(missing_gear))}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        current_climber = next((climber for climber in self.climbers if climber.name == climber_name), None)
        if not current_climber:
            return f"Climber {climber_name} is not registered yet."
        current_peak = next((peak for peak in self.peaks if peak.name == peak_name), None)
        if not current_peak:
            return f"Peak {peak_name} is not part of the wish list."
        if current_climber.is_prepared and current_climber.can_climb():
            current_climber.climb(current_peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {current_peak.difficulty_level}."
        elif not current_climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        current_climber.rest()
        return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        successful_climbers = [climber for climber in self.climbers if climber.conquered_peaks]
        sorted_climbers = sorted(successful_climbers, key=lambda x: (-len(x.conquered_peaks), x.name))
        total_peaks = []
        for obj in sorted_climbers:
            obj.conquered_peaks = sorted(obj.conquered_peaks)
            total_peaks += obj.conquered_peaks

        result = f"Total climbed peaks: {len(set(total_peaks))}\n**Climber's statistics:**"
        for climber in sorted_climbers:
            result += "\n" + climber.__str__()
        return result
