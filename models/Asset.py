from numpy import random

class Asset:
    def __init__(self, name, value, income, apr_mean, apr_std, liability=None) -> None:
        self.name = name
        self.value = value
        self.income = income
        self.apr_mean = apr_mean
        self.apr_std = apr_std
        self.liability = liability

    def to_dict(self):
            return {
                "name": self.name,
                "value": self.value,
                "income": self.income,
                "apr_mean": self.apr_mean,
                "apr_std": self.apr_std,
                "liability": self.liability.to_dict() if self.liability else None
            }

    def appreciate(self):
        #first calculate appreciation
        apr = random.gauss(self.apr_mean, self.apr_std)
        self.value += self.value * (1 + apr)
        return (self.value, apr)
    