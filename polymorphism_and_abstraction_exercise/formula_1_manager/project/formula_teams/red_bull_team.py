from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    expenses = 250000

    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        sponsorship1 = 0
        sponsorship2 = 0
        if race_pos == 1:
            sponsorship1 = 1500000
        elif race_pos == 2:
            sponsorship1 = 800000
        if race_pos <= 8:
            sponsorship2 = 20000
        elif race_pos <= 10:
            sponsorship2 = 10000
        total_sponsorship = sponsorship1 + sponsorship2
        revenue = total_sponsorship - RedBullTeam.expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
