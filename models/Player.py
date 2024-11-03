from models.Asset import Asset
from models.Liability import Liability
from models.Job import Job
from models.Taxes import Taxes

import copy

class Player:
    def __init__(self, assets=[], liabilites=[], credit_score=750, cash=0, job: Job=None) -> None:
        self.assets = assets
        self.liabilities = liabilites
        self.credit_score = credit_score
        self.cash = cash
        self.job = job
        self.tax = Taxes()

    def buy_asset(self, sample_asset: Asset):
        # buying asset
        new_liability = None
        if sample_asset.liability:
            if self.credit_score < 500:
                return None, "Not enough credit! Need 500."
            down_payment = sample_asset.value - sample_asset.liability.debt_amount
            if self.cash < down_payment:
                return None, "Insufficient funds!"
            self.cash -= down_payment
            new_liability = self.buy_liability(sample_asset.liability)
        else:
            if self.cash < sample_asset.value:
                return None, "Insufficient funds!"
            self.cash -= sample_asset.value

        # purchasing asset
        sample_asset.purchase_price = sample_asset.value
        asset = copy.deepcopy(sample_asset)
        if new_liability != None:
            asset.liability = new_liability
        self.assets.append(asset)

        # returning
        return asset, "Successful purchase!"

    def buy_liability(self, sample_liability: Liability) -> Liability:
        liability = copy.deepcopy(sample_liability)
        self.liabilities.append(liability)
        return liability

    def sell_asset(self, asset: Asset):
        self.assets.remove(asset)
        if asset.liability:
            self.sell_liability(asset.liability)
            self.cash += (asset.value - asset.liability.debt_amount)
        else:
            self.cash += asset.value
        self.tax.profits += (asset.value - asset.purchase_price)

    def sell_liability(self, liability):
        if liability in self.liabilities:
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
        return sum([asset.income for asset in self.assets]) + self.job.income /12 if self.job else 0
    
    @property
    def balance(self):
        return self.cash + sum([asset.value for asset in self.assets]) - sum([liability.debt_amount for liability in self.liabilities])
    
    @property
    def risk_aversion(self):
        """Computes Risk aversion. The weight of an asset if the dollar value of a security divided by the total value of the portfolio"""
        total = 0
        tw = 0
        #sum_of_values = sum([asset.value for asset in self.assets])
        for asset in self.assets:
            weight = asset.value 
            if asset.apr_mean <= 0.03:
                weight = 0
            if asset.apr_std < 0.00001 : #edge case, make it really small
                total += weight * 2 / (0.00001 ** 2) * (asset.apr_mean - 0.03)
            else:
                risk = 2 / (asset.apr_std ** 2) * (asset.apr_mean - 0.03)
                total += weight * risk
                tw += weight
        if tw ==0:
            tw =1
        return total/tw
    

    def calculate_all_taxes(self):
        self.tax.calculate_capital_gains_tax()
        self.tax.calculate_income_tax()
        self.tax.calculate_income_business_tax()
        return self.tax.taxes_owed
    
    def pay_all_taxes(self) -> int:
        """
        Function for paying all taxes
        
        Return states:
        0 - Taxes paid successfully
        1 - Need to sell to pay
        2 - Taxes greater than net worth, trigger game over
        """

        if self.balance < self.tax.taxes_owed:
            return 2
        elif self.cash < self.tax.taxes_owed:
            return 1
        else:
            self.cash -= self.tax.taxes_owed

            self.tax.taxable_income = 0
            self.tax.profits = 0
            self.tax.business_tax = 0
            self.tax.income_tax_owed = 0
            self.tax.capital_gains_tax_owed = 0
            self.tax.property_tax_owed = 0
            self.tax.business_tax_owed = 0

            return 0