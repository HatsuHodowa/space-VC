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
        if asset.liability:
            if self.credit_score < 500:
                return "Not enough credit!"
            down_payment = asset.value - asset.liability.debt_amount
            self.cash -= down_payment
            self.buy_liability(asset.liability)
        else:
            if self.cash < asset.value:
                return "Insufficient funds!"
            self.cash -= asset.value
        asset.purchase_price = asset.value
        self.assets.append(asset)
        return "Successful purchase!"

    def buy_liability(self, liability: Liability):
        self.liabilities.append(liability)

    def sell_asset(self, asset: Asset):
        self.assets.remove(asset)
        if asset.liability:
            self.sell_liability(asset.liability)
            self.cash += (asset.value - asset.liability.debt_amount)
        else:
            self.cash += asset.value

    def sell_liability(self, liability):
        self.liabilities.remove(liability)

    def get_job(self, job: Job):
        self.job = job

    def update_credit_score(self, adjustment):
        self.credit_score = min(850, self.credit_score * adjustment)

    def pay_loan(self, payment_amount, liability: Liability):
        amount_owed = liability.debt_amount / liability.months_left
        if payment_amount < amount_owed:
            penalty = (amount_owed - payment_amount) / amount_owed
            self.update_credit_score(1 - 0.1 * penalty)
        else:
            penalty = 1 - (amount_owed - payment_amount) / amount_owed
            self.update_credit_score(1 + 0.1 * penalty)
        remaining_balance = liability.pay_loan(payment_amount)
        if remaining_balance == 0:
            self.sell_liability(liability)
            

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
    
    @property
    def risk_aversion(self):
        """Computes Risk aversion. The weight of an asset if the dollar value of a security divided by the total value of the portfolio"""
        total = 0
        sum_of_values = sum([asset.value for asset in self.assets])
        for asset in self.assets:
            weight = asset.value / sum_of_values
            if asset.apr_std == 0: #edge case, make it really small
                total += weight * 2 / (0.00001 ** 2) * (asset.apr_mean - 0.03)
            risk = 2 / (asset.apr_std ** 2) * (asset.apr_mean - 0.03)
            total += weight * risk
        return total
        
        