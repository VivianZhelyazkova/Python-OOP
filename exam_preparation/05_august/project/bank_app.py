from typing import List

from project.clients.base_client import BaseClient
from project.loans.base_loan import BaseLoan
from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan
from project.clients.student import Student
from project.clients.adult import Adult


class BankApp:
    VALID_LOAN_TYPES = ["StudentLoan", "MortgageLoan"]
    VALID_CLIENT_TYPES = ["Student", "Adult"]

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):
        if loan_type not in BankApp.VALID_LOAN_TYPES:
            raise Exception("Invalid loan type!")
        loan = eval(loan_type)()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in BankApp.VALID_CLIENT_TYPES:
            raise Exception("Invalid client type!")
        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."
        client = eval(client_type)(client_name, client_id, income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        loan = next((loan for loan in self.loans if loan.__class__.__name__ == loan_type), None)
        client = next((client for client in self.clients if client.client_id == client_id), None)
        if loan.__class__.__name__ == "StudentLoan" and client.__class__.__name__ == "Student":
            return self.adding_loan_to_client(loan, client, loan_type, client_id)
        elif loan.__class__.__name__ == "MortgageLoan" and client.__class__.__name__ == "Adult":
            return self.adding_loan_to_client(loan, client, loan_type, client_id)
        else:
            raise Exception("Inappropriate loan type!")

    def adding_loan_to_client(self, loan, client, loan_type, client_id):
        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = next((client for client in self.clients if client.client_id == client_id), None)
        if not client:
            raise Exception("No such client!")
        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        counter = 0
        filtered_loans = [loan for loan in self.loans if loan.__class__.__name__ == loan_type]
        for loan in filtered_loans:
            loan.increase_interest_rate()
            counter += 1
        return f"Successfully changed {counter} loans."

    def increase_clients_interest(self, min_rate: float):
        counter = 0
        filtered_clients = [client for client in self.clients if client.interest < min_rate]
        for client in filtered_clients:
            client.increase_clients_interest()
            counter += 1
        return f"Number of clients affected: {counter}."

    def get_statistics(self):
        total_income = sum(x.income for x in self.clients)
        granted_loans = 0
        granted_sum = 0
        not_granted_sum = sum(x.amount for x in self.loans)
        for client in self.clients:
            for loan in client.loans:
                granted_loans += 1
                granted_sum += loan.amount
        result = (f"Active Clients: {len(self.clients)}\n"
                  f"Total Income: {total_income:.2f}\n"
                  f"Granted Loans: {granted_loans}, Total Sum: {granted_sum:.2f}\n"
                  f"Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}")
        if not self.clients:
            result += f"\nAverage Client Interest Rate: 0.00"
        else:
            avg_client_interest_rate = sum(x.interest for x in self.clients) / len(self.clients)
            result += f"\nAverage Client Interest Rate: {avg_client_interest_rate:.2f}"
        return result
