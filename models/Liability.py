class Liability:

    def __init__(self, name, debt_amount, interest_rate, payoff_date=12) -> None:
        self.name = name
        self.debt_amount = debt_amount
        self.interest_rate = interest_rate
        self.payoff_date = payoff_date

    def to_dict(self):
        return {
            "name": self.name,
            "debt_amount": self.debt_amount,
            "interest_rate": self.interest_rate,
            "payoff_date": self.payoff_date
        }
    
    def pay_loan(self, amount):
        self.debt_amount -= amount
        return self.debt_amount
    
    def calculate_interest(self):
        self.debt_amount += self.debt_amount * self.interest_rate
        return self.debt_amount
    
    def monthly_update(self, payment_amount):
        """Monthly update to check if a loan payment was made. If not,
        then the user will get penalized for missing their payment."""
        self.pay_loan(payment_amount)
        self.payoff_date -= 1
        self.calculate_interest()
            
    @property
    def monthly_payment(self):
        return self.debt_amount / 12
    
    # TO-DO: Check the autopay functionality in the game controller.

    

        

