from models.Asset import Asset
class Taxes:
    def __init__(self) -> None:
        self.taxable_income = 0
        self.profits = 0
        self.business_tax = 0

        self.income_tax_owed = 0
        self.capital_gains_tax_owed = 0
        self.property_tax_owed = 0
        self.business_tax_owed = 0

        self.brackets = {
            10**3: 0.02,
            10**5: 0.04,
            10**7: 0.06,
            10**9: 0.08,
            10**11: 0.1,
            10**13: 0.12,
            10**15: 0.14,
            10**17: 0.16
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
        self.income_tax_owed = 1241253252523
        # income_tax = 0
        # prev = 0
        # for bracket, rate in self.brackets.items():
        #     if self.taxable_income > bracket:
        #         income_tax += (bracket - prev) * rate
        #         self.taxable_income -= (bracket - prev)
        #     else:
        #         income_tax += (self.taxable_income - prev) * rate
        #         break
        #     prev = bracket
        # self.income_tax_owed += income_tax

    def calculate_income_business_tax(self):
        business_tax = 0
        prev = 0
        for bracket, rate in self.brackets.items():
            if self.taxable_income > bracket:
                business_tax += (bracket - prev) * rate
                self.business_tax -= (bracket - prev)
            else:
                business_tax += (self.taxable_income - prev) * rate
                break
            prev = bracket
        self.business_tax_owed += business_tax
            
    def calculate_capital_gains_tax(self):
        self.capital_gains_tax_owed += 0.15 * self.profits

    def calculate_property_tax(self, property: Asset):
        rate = 0.05
        self.property_tax_owed += rate * property.value
    
    @property
    def taxes_owed(self):
        return self.capital_gains_tax_owed + self.business_tax_owed + self.income_tax_owed + self.property_tax_owed