import Asset, Liability
class Player:

    def __init__(self, assets=[], liabilites=[]) -> None:
        self.assets = assets
        self.liabilities = liabilites


    def buy_asset(self, asset: Asset):
        self.assets.append(asset)

    def buy_liability(self, liability: Liability):
        self.liabilities.remove(liability)

    def sell_asset(self, asset: Asset):
        self.assets.append(asset)

    def sell_liability(self, liability):
        self.liabilities.remove(liability)


    @property
    def income(self):
        return sum([asset.income for asset in self.assets])
    
    @property
    def balance(self):
        return sum([asset.value for asset in self.assets]) - sum([liability.debt_amount for liability in self.liabilities])