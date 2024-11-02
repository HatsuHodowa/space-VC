from models.Player import Player
class Game:
    def __init__(self) -> None:
        self.player = Player()
        self.months = 0

    def monthly_update(self):
        self.months += 1

        #appreciate assets
        for asset in self.player.assets:
            asset.appreciate()
        for liability in self.player.liabilities:
            #calculate interest and decrement months left for payment
            liability.calculate_interest()
            liability.months_left -= 1
        #implement tax updates here
    
    def game_status(self):
        print("months ", self.months)
        print("balance ", self.player.balance)