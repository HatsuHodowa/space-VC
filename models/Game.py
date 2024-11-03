from models.Player import Player
from models.Asset import AssetType
from View.View import View

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
            job_income = self.player.job.income / 12
            self.player.cash += job_income
            self.player.tax.report_job_income(job_income)

        # appreciate assets
        for asset in self.player.assets:
            asset.appreciate()
            self.player.cash += asset.income

            if (asset.asset_type == AssetType.BUSINESS):
                self.player.tax.report_business_income(asset.income)
            if (asset.asset_type == AssetType.SECURITY):
                self.player.tax.report_job_income(asset.income)

        for liability in self.player.liabilities:
            monthly_payment = liability.monthly_payment
            self.player.pay_loan(min(monthly_payment, self.player.cash), liability)
            if liability.months_left == 0 and liability.debt_amount > 0:
                self.player.collections_remove_liability(liability)
            liability.calculate_interest()
            liability.months_left -= 1
        
    def sell_each_asset(self):
        for asset in self.player.assets:
            self.player.sell_asset(asset)
    
    def level_up(self):
        self.sell_each_asset()
        if self.level == "Earth":
            self.level = "Moon"
        elif self.level == "Moon":
            self.level = "Venus"
        elif self.level == "Venus":
            self.level = "Mars"
        elif self.level == "Mars":
            self.level = "Mercury"
        elif self.level == "Mercury":
            self.level = "Jupiter"
        elif self.level == "Jupiter":
            self.level = "Saturn"
        elif self.level == "Saturn":
            self.level = "Uranus"
        elif self.level == "Uranus":
            self.level = "Neptune"
        elif self.level == "Neptune":
            self.level = "END"