from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):

    def get_recommended_gear(self):
        return ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    def calculate_difficulty_level(self):
        if 3000 >= self.elevation >= 2000:
            return "Advanced"
        elif self.elevation > 3000:
            return "Extreme"

