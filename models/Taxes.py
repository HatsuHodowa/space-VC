class Taxes:
    def __init__(self) -> None:
        self.taxable_income = 0
        self.profits = 0
        self.property_tax = 0
        self.business_tax = 0

    def pay_tax(self, income_payment, capital_gains_payment, property_payment, business_payment):
        self.taxable_income -= income_payment
        self.profits -= capital_gains_payment
        self.property_tax -= property_payment
        self.business_tax -= business_payment
    
    def report_income(self):
        #based off bracket
        return
    
    def report_profits(self, profits):
        self.profits += profits
    
    def report_property(self, asset):
        self.property_tax += asset.value * () # Get the property tax percentage for each planet.

