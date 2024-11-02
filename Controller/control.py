import tkinter as tk
import sys

sys.path.append("..")
sys.path.append("View")
sys.path.append("..")
sys.path.append("models")
from View import View
from models import Player


class SpaceVC:
    def __init__(self) -> None:
        self.player = Player.Player()
        root = tk.Tk()
        self.view = View.View(root)
        
        root.mainloop()


    def update_ui(self):
        stats_dict = {
            "income": self.player.income(),
            "balance": self.player.balance(),
            "assets": len(self.player.assets),
            "liabilities": len(self.player.liabilities),
            "credit_score": self.player.credit_score
        }
        self.view.update_stats( stats_dict)

    def update_model(self):
        # TODO: Update player model based on user actions
        pass 



if __name__ == "__main__":
    SpaceVC()