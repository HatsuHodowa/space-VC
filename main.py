from models.Asset import Asset, AssetType
from models.Liability import Liability
from models.Game import Game

game = Game()
liability = Liability("Car", 25000, 0.06, 12)
asset2 = Asset("Risk", 50000, 30000, 0, 0.04, AssetType.PROPERTY, 5)

game.player.buy_asset(asset2)
print(game.game_status())
game.monthly_update()
print(game.game_status())
