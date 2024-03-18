from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    MINIMUM_STRENGTH_REQUIRED = 75
    INITIAL_STRENGTH = 150

    def __init__(self, name: str):
        super().__init__(name, SummitClimber.INITIAL_STRENGTH)

    def can_climb(self):
        return self.strength >= SummitClimber.MINIMUM_STRENGTH_REQUIRED

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Extreme":
            self.strength -= 2.5 * 30
        elif peak.difficulty_level == "Advanced":
            self.strength -= 1.3 * 30
        self.conquered_peaks.append(peak.name)
