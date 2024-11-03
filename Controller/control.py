import json
import json
import tkinter as tk
import sys




sys.path.append("..")
sys.path.append("View")
sys.path.append("..")
sys.path.append("models")
from models import Asset
from View import View
from models import Player
from models import Liability
from models import Job
from models import Game
import market_levels


class SpaceVC:
    def __init__(self) -> None:
        self.game = Game.Game()
        self.player = self.game.player
        
        self.level= "Earth"
        #create data

        # load data

        with open("../game_data.json", "r") as file:
            self.data = json.load(file)

        def convert_to_list(data):
            if isinstance(data, dict):
                li = []
                
                for k, v in data.items():
                    #print(k, v)

                    if k == "assets":
                        li = li + [[ Asset.Asset(**g) for g in v]]
                    if k == "liabilities":
                        li = li + [[Liability.Liability(**g) for g in v]]
                        #li.append( Liability.Liability(**v))
                    if k == "careers":
                        li = li + [[Job.Job(**g) for g in v]]
                        #li.append( Job.Job(**v))
                
                if len(li) >0:
                    return li
                return {k: convert_to_list(v) for k, v in data.items()}
            elif isinstance(data, list):
                return [convert_to_list(item) for item in data]
            else:
                return data
        #convert json data to python data structure

        self.data = convert_to_list(self.data)
        self.levels = list(self.data.keys())
        print(self.levels)

        # testing
        self.player.cash += 500000

        root = tk.Tk()
        self.view = View.View(root, self)
        self.update_ui()
        root.mainloop()
        


    def update_ui(self):
        stats_dict = {
            "income": self.player.income,
            "balance": self.player.cash,
            "net_worth": self.player.balance,
            "assets": sum([asset.value for asset in self.player.assets]),
            "liabilities": sum([asset["debt_amount"] for asset in self.player.liabilities]),
            "credit_score": self.player.credit_score,
            "occupation": self.player.job.title if self.player.job else "Unemployed",
            "month": self.game.months
        }
        self.view.update_stats(stats_dict)

    def buy_asset(self, asset_name):
        for a in self.data[self.level][0]:
            if a.name == asset_name:
                response = self.player.buy_asset(a)
                break
        self.update_ui()
        self.view.popup_display(response)
        
    def sell_asset(self, asset_name):
        for a in self.player.assets:
            if a.name == asset_name:
                self.player.sell_asset(a)
                break
        self.update_ui()

    def buy_liability(self, liability_name):
        for l in self.data[self.level][2]:
            if l.name == liability_name:
                self.player.buy_liability(l)
                break
        self.update_ui()

    def sell_liability(self, liability_name):
        for l in self.data[self.level][2]:
            if l.name == liability_name:
                self.player.sell_liability(l)
                break
        self.update_ui()

    def get_job(self, job_name):
        for j in self.data[self.level][1]:
            if j.title == job_name:
                self.player.get_job(j)
                break
        self.update_ui()

    def monthly_update(self):
        if self.game.months % 12 == 3 and self.player.calculated_taxes() >0:
            return "Taxes due " + str(self.player.calculated_taxes())
        self.game.monthly_update()
        self.update_ui()

    def update_model(self):
        # TODO: Update player model based on user actions
        pass 

if __name__ == "__main__":
    SpaceVC()