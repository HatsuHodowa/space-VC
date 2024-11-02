from models.Asset import Asset 
from models.Liability import Liability
from models.Player import Player

player = Player()
asset1 = Asset("House", 100000, 0, 0.05, 0.01)
player.buy_asset(asset1)
liability = Liability("Car", 25000, 0.06)
player.buy_liability(liability)

print(player.balance)