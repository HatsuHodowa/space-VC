from enum import Enum
from numpy import random
from models.Liability import Liability

class AssetType(Enum):
    PROPERTY = 1,
    SECURITY = 2,
    BUSINESS = 3

class Asset:
    def __init__(self, name, value, income, apr_mean, apr_std, purchase_price, asset_type, liability=None) -> None:
        self.name = name
        self.value = value
        self.purchase_price = purchase_price
        self.income = income
        self.apr_mean = apr_mean
        self.apr_std = apr_std
        self.asset_type = asset_type
        self.liability = liability

        # converting liability to object
        if type(self.liability) == dict:
            self.liability = Liability(**self.liability)

    def to_dict(self):
        return {
            "name": self.name,
            "value": self.value,
            "purchase_price": self.purchase_price,
            "income": self.income,
            "apr_mean": self.apr_mean,
            "apr_std": self.apr_std,
            "asset_type": self.asset_type.name,  # Convert enum to string
            "liability": self.liability.to_dict() if self.liability else None
        }

    def appreciate(self):
        #first calculate appreciation
        apr = random.normal(self.apr_mean, self.apr_std) / 12
        print(apr)
        self.value += self.value * apr
        print(self.value)
        return (self.value, apr)
    