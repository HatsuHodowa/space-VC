from models.Asset import Asset
from models.Asset import AssetType

PROPERTY_TAX_RATE = 0.05
CAPITAL_GAINS_RATE = 0.15

class Taxes:
    def __init__(self) -> None:
        self.job_income = 0
        self.capital_gains = 0
        self.business_income = 0

        self.income_tax_owed = 0
        self.capital_gains_tax_owed = 0
        self.property_tax_owed = 0
        self.business_tax_owed = 0

        self.brackets = [
            (10**3, 0.02),
            (10**5, 0.04),
            (10**7, 0.06),
            (10**9, 0.08),
            (10**11, 0.1),
            (10**13, 0.12),
            (10**15, 0.14),
            (10**17, 0.16),
        ]

    def report_job_income(self, income):
        self.job_income += income

    def report_capital_income(self, income):
        self.capital_gains += income

    def report_business_income(self, income):
        self.business_income += income

    def calculate_income_tax(self):
        income = self.job_income
        tax = 0

        for item in self.brackets:
            bracket = item[0]
            percentage = item[1]

            if income > bracket:
                tax += bracket * percentage
                income -= bracket
            else:
                tax += income * percentage
                income -= income
        
        self.income_tax_owed = tax

    def calculate_income_business_tax(self):
        income = self.business_income
        tax = 0

        for item in self.brackets:
            bracket = item[0]
            percentage = item[1]
            
            if income > bracket:
                tax += bracket * percentage
                income -= bracket
            else:
                tax += income * percentage
                income -= income

        self.business_tax_owed = tax
            
    def calculate_capital_gains_tax(self):
        self.capital_gains_tax_owed = CAPITAL_GAINS_RATE * self.capital_gains

    def calculate_property_tax(self, player):
        tax = 0

        for asset in player.assets:
            if asset.asset_type == AssetType.PROPERTY:
                tax += asset.value * PROPERTY_TAX_RATE

        self.property_tax_owed = tax

    def reset_taxes(self):
        self.job_income = 0
        self.capital_gains = 0
        self.business_income = 0

        self.income_tax_owed = 0
        self.capital_gains_tax_owed = 0
        self.property_tax_owed = 0
        self.business_tax_owed = 0
    
    @property
    def taxes_owed(self):
        return self.capital_gains_tax_owed + self.business_tax_owed + self.income_tax_owed + self.property_tax_owed