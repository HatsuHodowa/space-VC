from models.Player import Player
from models.Asset import AssetType

class Game:
    def __init__(self) -> None:
        self.player = Player()
        self.months = 0
        self.level = "Earth"
        self.tax_lock = False

    def monthly_update(self):
        self.months += 1

        #process salary
        if self.player.job:
            self.player.cash += self.player.job.income / 12
            self.player.tax.taxable_income += self.player.job.income / 12

        #appreciate assets
        for asset in self.player.assets:
            asset.appreciate()
            self.player.cash += asset.income
            if (asset.asset_type == AssetType.BUSINESS):
                self.player.tax.business_tax += asset.income
            if (asset.asset_type == AssetType.PROPERTY):
                self.player.tax.calculate_property_tax(asset)


        for liability in self.player.liabilities:
            monthly_payment = liability.monthly_payment
            self.player.pay_loan(min(monthly_payment, self.player.cash), liability)
            if liability.months_left == 0 and liability.debt_amount > 0:
                self.player.collections_remove_liability(liability)
            liability.calculate_interest()
            liability.months_left -= 1
    
    def level_up(self):
        if self.level == "Earth":
            self.level = "Moon"
        if self.level == "Moon":
            self.level = "Venus"
        if self.level == "Venus":
            self.level = "Mars"
        if self.level == "Mars":
            self.level = "Mercury"
        if self.level == "Mercury":
            self.level = "Jupiter"
        if self.level == "Jupiter":
            self.level = "Saturn"
        if self.level == "Saturn":
            self.level = "Uranus"
        if self.level == "Uranus":
            self.level = "Neptune"
        if self.level == "Neptune":
            self.level = "END"