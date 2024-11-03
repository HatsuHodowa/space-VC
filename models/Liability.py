
class Liability:

    def __init__(self, name, debt_amount, interest_rate, months_left=12) -> None:
        self.name = name
        self.debt_amount = debt_amount
        self.interest_rate = interest_rate
        self.months_left = months_left

    def to_dict(self):
        return {
            "name": self.name,
            "debt_amount": self.debt_amount,
            "interest_rate": self.interest_rate,
            "months_left": self.months_left
        }
    
    def pay_loan(self, amount):
        self.debt_amount -= amount
        return self.debt_amount
    
    def calculate_interest(self):
        self.debt_amount += self.debt_amount * self.interest_rate
        return self.debt_amount
            
    @property
    def monthly_payment(self):
        return self.debt_amount / self.months_left
    
    # TO-DO: Check the autopay functionality in the game controller.

    # TO-DO: Change the payoff date from an integer to timedelta and use datetime objects.

    

        

