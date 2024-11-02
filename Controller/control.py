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
        stats_dict = None # TODO
        self.view.update_stats(self, stats_dict)

    def update_model(self):
        # TODO: Update player model based on user actions
        pass 



if __name__ == "__main__":
    SpaceVC()