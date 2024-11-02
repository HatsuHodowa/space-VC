from numpy import random

class Asset:
    def __init__(self, name, value, income, apr_mean, apr_std) -> None:
        self.name = name
        self.value = value
        self.income = income
        self.apr_mean = apr_mean
        self.apr_std = apr_std

    def appreciate(self):
        #first calculate appreciation
        apr = random.gauss(self.apr_mean, self.apr_std)
        self.value += self.value * (1 + apr)
        return (self.value, apr)
    