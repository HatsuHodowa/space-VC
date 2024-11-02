class Liability:

    def __init__(self, name, debt_amount, interest_rate) -> None:
        self.name = name
        self.debt_amount = debt_amount
        self.interest_rate = interest_rate
    
    def pay_loan(self, amount):
        self.debt_amount -= amount
        return self.debt_amount
    
    def calculate_interest(self):
        self.debt_amount += self.debt_amount * self.interest_rate
        return self.debt_amount
    
