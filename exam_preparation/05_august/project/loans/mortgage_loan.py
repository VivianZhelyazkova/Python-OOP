from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    INTEREST_RATE = 3.5
    AMOUNT = 50000.0

    def __init__(self):
        super().__init__(MortgageLoan.INTEREST_RATE, MortgageLoan.AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.5
