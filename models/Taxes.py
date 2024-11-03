from models.Asset import Asset
class Taxes:
    def __init__(self) -> None:
        self.taxable_income = 0
        self.profits = 0
        self.property_tax = 0
        self.business_tax = 0
        self.income_tax_owed = 0
        self.capitals_gains_tax_owed = 0
        self.property_tax_owed = 0
        self.business_tax_owed = 0
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
        self.property_tax_brackets = {
            "Earth": 0.05,
            "Moon": 0.10,
            "Venus": 0.15,
            "Mars": 0.20,
            "Mercury": 0.22,
            "Jupiter": 0.24,
            "Saturn": 0.26,
            "Uranus": 0.28,
            "Neptune": 0.3
        }

    def report_income(self, income):
        self.taxable_income += income
    
    def report_profits(self, profits):
        self.profits += profits
    
    def report_property(self, property):
        self.property_tax +=  property.value

    def report_business(self, business):
        self.business_tax += business.value

    def calculate_income_tax(self):
        income_tax = 0
        prev = 0
        for bracket, rate in self.brackets.items():
            if self.taxable_income > bracket:
                income_tax += (bracket - prev) * rate
            else:
                income_tax += (self.taxable_income - prev) * rate
                break
            prev = bracket
        self.income_tax_owed += income_tax

    def calculate_income_business_tax(self):
        business_tax = 0
        prev = 0
        for bracket, rate in self.brackets.items():
            if self.taxable_income > bracket:
                business_tax += (bracket - prev) * rate
            else:
                business_tax += (self.taxable_income - prev) * rate
                break
            prev = bracket
        self.business_tax_owed += business_tax
            
    def calculate_capital_gains_tax(self):
        self.capitals_gains_tax_owed += 0.15 * self.profits

    def calculate_property_tax(self, property: Asset, planet):
        rate = self.property_tax_brackets[planet]
        self.property_tax_owed += rate * property.value