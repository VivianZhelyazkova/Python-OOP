from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    expenses = 200000

    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        sponsorship1 = 0
        sponsorship2 = 0
        if race_pos == 1:
            sponsorship1 = 1000000
        elif race_pos <= 3:
            sponsorship1 = 500000
        if race_pos <= 5:
            sponsorship2 = 100000
        elif race_pos <= 7:
            sponsorship2 = 50000
        total_sponsorship = sponsorship1 + sponsorship2
        revenue = total_sponsorship - MercedesTeam.expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
