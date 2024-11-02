from models.Asset import Asset
from models.Liability import Liability
from models.Job import Job

class Player:

    def __init__(self, assets=[], liabilites=[], credit_score=750, cash=0, job: Job=None) -> None:
        self.assets = assets
        self.liabilities = liabilites
        self.credit_score = credit_score
        self.cash = cash
        self.job = job

    def buy_asset(self, asset: Asset):
        self.assets.append(asset)
        self.cash -= asset.value

    def buy_liability(self, liability: Liability):
        self.liabilities.append(liability)

    def sell_asset(self, asset: Asset):
        self.assets.remove(asset)
        self.cash += asset.value

    def sell_liability(self, liability):
        self.liabilities.remove(liability)

    def get_job(self, job: Job):
        self.job = job

    def update_credit_score(self, adjustment):
        self.credit_score = min(850, self.credit_score * adjustment)

    def monthly_update(self, payment_amount, liability: Liability):
        if liability.payoff_date == 0:
            self.collections_remove_liability(liability)
            return
        amount_owed = liability.debt_amount / liability.payoff_date
        if payment_amount < amount_owed:
            penalty = (amount_owed - payment_amount) / amount_owed
            self.update_credit_score(1 - 0.1 * penalty)
        else:
            penalty = 1 - (amount_owed - payment_amount) / amount_owed
            self.update_credit_score(1 + 0.1 * penalty)
        liability.monthly_update(payment_amount)
            

    def collections_remove_liability(self, liability: Liability):
        self.liabilities.remove(liability)
        min_diff, closest_asset = 1_000_000, None
        for asset in self.assets:
            if abs(liability.debt_amount - asset.value) < min_diff:
                min_diff = abs(liability.debt_amount - asset.value)
                closest_asset = asset
        self.assets.remove(closest_asset)
        self.update_credit_score(0.83)

    @property
    def income(self):
        return sum([asset.income for asset in self.assets])
    
    @property
    def balance(self):
        return self.cash + sum([asset.value for asset in self.assets]) - sum([liability.debt_amount for liability in self.liabilities])
    