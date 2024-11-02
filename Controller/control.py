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



if __name__ == "__main__":
    SpaceVC()