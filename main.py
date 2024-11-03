from models.Asset import Asset, AssetType
from models.Liability import Liability
from models.Game import Game
from models.Job import Job

game = Game()
liability = Liability("Car", 25000, 0.06, 12)
asset2 = Asset("House", 500000, 0, 0.05, 0.01, 500000, AssetType.PROPERTY)
job = Job("Software Engineer", 1000000)

game.player.get_job(job)
game.monthly_update()
game.monthly_update()
game.monthly_update()
print(game.player.buy_asset(asset2))
game.monthly_update()
game.monthly_update()
game.monthly_update()
game.player.calculate_all_taxes()
game.game_status()