class Taxes:
    def __init__(self) -> None:
        self.taxable_income = 0
        self.profits = 0
        self.property_tax = 0
        self.business_tax = 0
        self.brackets = {
            10**3: 0.1,
            10**5: 0.12,
            10**7: 0.22,
            10**9: 0.24,
            10**11: 0.32,
            10**13: 0.35,
            10**15: 0.37,
            10**17: 0.43
        }

    def pay_tax(self, income_payment, capital_gains_payment, property_payment, business_payment):
        self.taxable_income -= income_payment
        self.profits -= capital_gains_payment
        self.property_tax -= property_payment
        self.business_tax -= business_payment
    
    def report_income(self, income):
        self.taxable_income += income
    
    def report_profits(self, profits):
        self.profits += profits
    
    def report_property(self, property):
        self.property_tax +=  property.value

    def report_business(self, business):
        self.business_tax += business.value

    def calculate_income_tax(self):
        income_brackets = {
            0: 0.1,
            1: 0.12,
            2: 0.22,
            3: 0.24,
            4: 0.32,
            5: 0.35,
            6: 0.37,
            7: 0.43
        }

    
        