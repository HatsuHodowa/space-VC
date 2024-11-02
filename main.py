from models.Asset import Asset 
from models.Liability import Liability
from models.Player import Player

player = Player()
asset1 = Asset("House", 100000, 0, 0.05, 0.01)
player.buy_asset(asset1)
liability = Liability("Car", 25000, 0.06, 12)
player.buy_liability(liability)

player.monthly_update(500, liability)
player.monthly_update(0, liability)
player.monthly_update(23000, liability)
print(player.liabilities[0].debt_amount)
print(player.credit_score)
