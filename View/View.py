import tkinter as tk
from PIL import Image, ImageTk

import math

# constants
WINDOW_SIZE = (900, 600)
PRIM_COLOR = "#e8e8e8"
SEC_COLOR = "#ababab"
SELECTED_COLOR = "#a0e6eb"
GREEN = "#00ff00"
WHITE = "#ffffff"
BLACK = "#000000"

MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
NUMBER_SUFFIXES = [
    " K",
    " M",
    " B",
    " T",
    " Qd",
    " Qn"
]
STARTING_YEAR = 3000

# class
class View:
    def __init__(self, window: tk.Tk):

        # configuring window
        self.window = window
        self.window.title("Space Finance Simulator")
        self.window.geometry(str(WINDOW_SIZE[0]) + "x" + str(WINDOW_SIZE[1]))

        # properties
        self.bg_photo = None
        self.bg_label = None
        self.current_menu = ""

        # stats
        self.balance = tk.StringVar(self.window, "Balance: $0")
        self.date = tk.StringVar(self.window, "Date: January 3000")

        self.credit_score = tk.StringVar(self.window, "Credit Score: 0")
        self.income = tk.StringVar(self.window, "Income: $0/month")
        self.net_worth = tk.StringVar(self.window, "Net Worth: $0")
        self.occupation = tk.StringVar(self.window, "Occupation: Unemployed")

        self.assets = tk.StringVar(self.window, "Assets: 0")
        self.liabilities = tk.StringVar(self.window, "Liabilities: 0")

        # styling defaults
        self.frame_styling = {"bg":PRIM_COLOR, "highlightbackground":SEC_COLOR, "highlightthickness":5}
        self.medium_font = ("Roboto", 20)
        self.small_font = ("Roboto", 14)
        self.padding_10 = {"padx":10, "pady":10}
        self.padding_5 = {"padx":5, "pady":5}

        # opening game
        self.set_menu("in_game")

    def format_number(number: int) -> str:
        if number <= 0:
            return str(number)
        
        suffix_index = math.floor(math.log10(number) / 3)
        formatted = str(round(number / (10 ** (suffix_index * 3)), 2)) + NUMBER_SUFFIXES[suffix_index]
        return formatted

    def update_stats(self, stats_dict: dict):
        """
        stats_dict keys:
            balance: number
            month: number

            credit_score: number
            income: number
            net_worth: number
            occupation: str
            assets: number
            liabilities: number
        """

        # top data
        if "balance" in stats_dict:
            self.balance.set("Balance: $" + str(View.format_number(stats_dict["balance"])))
        if "month" in stats_dict:
            month = stats_dict["month"]
            year = month // 12 + STARTING_YEAR
            month = month % 12
            self.date.set("Date: " + MONTHS[month] + " " + str(year))

        # updating string values
        if "credit_score" in stats_dict:
            self.credit_score.set("Credit Score: " + str(stats_dict["credit_score"]))
        if "income" in stats_dict:
            self.income.set("Income: $" + str(View.format_number(stats_dict["income"])) + "/month")
        if "net_worth" in stats_dict:
            self.net_worth.set("Net Worth: $" + str(View.format_number(stats_dict["net_worth"])))
        if "occupation" in stats_dict:
            self.occupation.set("Occupation: " + stats_dict["occupation"])
        if "assets" in stats_dict:
            self.assets.set("Assets: " + str(stats_dict["assets"]))
        if "liabilities" in stats_dict:
            self.liabilities.set("Liabilities: " + str(stats_dict["liabilities"]))

        # reloading menu
        if self.current_menu == "in_game":
            self.set_menu(self.current_menu)

    def set_background(self, path: str):
        bg_image = Image.open(path)
        aspect_ratio = bg_image.width / bg_image.height
        bg_image = bg_image.resize((WINDOW_SIZE[0], int(WINDOW_SIZE[0] / aspect_ratio)), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        self.bg_label = tk.Label(self.window, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def set_menu(self, menu_name: str, *args):
        self.clear_window()
        self.current_menu = menu_name
        getattr(self, menu_name)(*args)
        
    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def in_game(self, current_tab: str = "stats_tab", background="../View/backgrounds/unicorn space.jpg"):
        self.set_background(background)

        # top bar
        top_bar = tk.Frame(self.window, **self.frame_styling)
        top_bar.place(x=0, y=0, width=WINDOW_SIZE[0], height=60)

        # items in top bar
        top_bar.columnconfigure(0, weight=1)
        top_bar.columnconfigure(1, weight=1)
        top_bar.rowconfigure(0, weight=1)

        balance = tk.Label(top_bar, textvariable=self.balance, bg=PRIM_COLOR, font=self.small_font)
        date = tk.Label(top_bar, textvariable=self.date, bg=PRIM_COLOR, font=self.small_font)
        balance.grid(column=0, row=0, sticky="W", **self.padding_10)
        date.grid(column=1, row=0, sticky="W", **self.padding_10)

        # next button
        next_button = tk.Button(self.window, text="Next Month", bg=GREEN, font=self.small_font)
        next_button.place(x=WINDOW_SIZE[0] - 20, y=WINDOW_SIZE[1] - 230, anchor="se")

        # bottom section
        bottom_frame = tk.Frame(self.window, **self.frame_styling)
        bottom_frame.place(x=0, y=WINDOW_SIZE[1], anchor="sw", width=WINDOW_SIZE[0], height=170)

        # tab buttons
        tabs_frame = tk.Frame(self.window, **self.frame_styling)
        tabs_frame.place(x=0, y=WINDOW_SIZE[1] - 170, anchor="sw", width=WINDOW_SIZE[0], height=50)

        stats_tab = tk.Button(tabs_frame, text="Stats", bg=PRIM_COLOR, font=self.small_font)
        assets_tab = tk.Button(tabs_frame, text="Assets", bg=PRIM_COLOR, font=self.small_font)
        liabilities_tab = tk.Button(tabs_frame, text="Liabilities", bg=PRIM_COLOR, font=self.small_font)
        stocks_tab = tk.Button(tabs_frame, text="Stocks", bg=PRIM_COLOR, font=self.small_font)
        taxes_tab = tk.Button(tabs_frame, text="Taxes", bg=PRIM_COLOR, font=self.small_font)

        stats_tab.grid(column=0, row=0)
        assets_tab.grid(column=1, row=0)
        liabilities_tab.grid(column=2, row=0)
        stocks_tab.grid(column=3, row=0)
        taxes_tab.grid(column=4, row=0)

        # coloring selected tab
        if current_tab == "stats_tab":
            stats_tab.config(bg=SELECTED_COLOR)
        elif current_tab == "assets_tab":
            assets_tab.config(bg=SELECTED_COLOR)
        elif current_tab == "liabilities_tab":
            liabilities_tab.config(bg=SELECTED_COLOR)
        elif current_tab == "stocks_tab":
            stocks_tab.config(bg=SELECTED_COLOR)
        elif current_tab == "taxes_tab":
            taxes_tab.config(bg=SELECTED_COLOR)

        # connecting buttons
        def switch_tab(new_tab: str):
            self.set_menu("in_game", new_tab)

        stats_tab.config(command=lambda :switch_tab("stats_tab"))
        assets_tab.config(command=lambda :switch_tab("assets_tab"))
        liabilities_tab.config(command=lambda :switch_tab("liabilities_tab"))
        stocks_tab.config(command=lambda :switch_tab("stocks_tab"))
        taxes_tab.config(command=lambda :switch_tab("taxes_tab"))

        # adding tab content for current tab
        if current_tab != None:
            getattr(self, current_tab)(bottom_frame)

    def stats_tab(self, bottom_frame: tk.Frame):

        # creating text labels
        credit_score = tk.Label(bottom_frame, textvariable=self.credit_score, font=self.small_font, bg=PRIM_COLOR)
        income = tk.Label(bottom_frame, textvariable=self.income, font=self.small_font, bg=PRIM_COLOR)
        net_worth = tk.Label(bottom_frame, textvariable=self.net_worth, font=self.small_font, bg=PRIM_COLOR)
        occupation = tk.Label(bottom_frame, textvariable=self.occupation, font=self.small_font, bg=PRIM_COLOR)

        assets = tk.Label(bottom_frame, textvariable=self.assets, font=self.small_font, bg=PRIM_COLOR)
        liabilities = tk.Label(bottom_frame, textvariable=self.liabilities, font=self.small_font, bg=PRIM_COLOR)

        # adding to display
        credit_score.grid(column=0, row=0, sticky="W", padx=(5,25), pady=5)
        income.grid(column=0, row=1, sticky="W", padx=(5,25), pady=5)
        net_worth.grid(column=0, row=2, sticky="W", padx=(5,25), pady=5)
        occupation.grid(column=0, row=3, sticky="W", padx=(5,25), pady=5)

        assets.grid(column=1, row=0, sticky="W", **self.padding_5)
        liabilities.grid(column=1, row=1, sticky="W", **self.padding_5)

    def assets_tab(self, bottom_frame: tk.Frame):

        # creating items
        scrollbar = tk.Scrollbar(bottom_frame, orient="vertical")
        listbox = tk.Listbox(bottom_frame, **self.frame_styling, yscrollcommand=scrollbar.set, font=self.small_font)
        data_frame = tk.Frame(bottom_frame, **self.frame_styling)

        scrollbar.config(command=listbox.yview)

        value = tk.Label(data_frame, font=self.small_font, text="Value: $0", bg=PRIM_COLOR)
        cash_flow = tk.Label(data_frame, font=self.small_font, text="Cash Flow: $0/month", bg=PRIM_COLOR)
        mean_apr = tk.Label(data_frame, font=self.small_font, text="Mean Return Rate: $0", bg=PRIM_COLOR)
        std_apr = tk.Label(data_frame, font=self.small_font, text="Std Return Rate: $0", bg=PRIM_COLOR)
        liability = tk.Label(data_frame, font=self.small_font, text="Liability: None", bg=PRIM_COLOR)

        # adding to display
        bottom_frame.columnconfigure(0, weight=1)
        bottom_frame.columnconfigure(1, weight=0)
        bottom_frame.columnconfigure(2, weight=50)
        bottom_frame.rowconfigure(0, weight=1)

        listbox.grid(column=0, row=0, padx=(10, 0), pady=10, sticky="NESW")
        scrollbar.grid(column=1, row=0, padx=(0, 10), pady=10, sticky="NSW")
        data_frame.grid(column=2, row=0, **self.padding_10, sticky="NESW")

        # adding assets
        for i in range(10):
            listbox.insert(0, "Hello world " + str(i))

        # configuring listbox
        def listbox_select(event: tk.Event):
            selected = event.widget.curselection()

            # updating information
            
            # adding items
            value.grid(column=0, row=0, padx=(5, 15), pady=5, stick="W")
            cash_flow.grid(column=0, row=1, padx=(5, 15), pady=5, stick="W")
            mean_apr.grid(column=0, row=2, padx=(5, 15), pady=5, stick="W")
            std_apr.grid(column=1, row=0, padx=(5, 15), pady=5, stick="W")
            liability.grid(column=1, row=1, padx=(5, 15), pady=5, stick="W")

        listbox.bind("<<ListboxSelect>>", listbox_select)
        
        # list all current assets
        # buying assets
        # selling assets

        """
        for each asset
            value: number
            income: number
            average return rate: number
            STD return rate: number
            liability: str
        """
        pass

    def liabilities_tab(self, bottom_frame: tk.Frame):
        # list all current liabilities
        # getting loans
        # paying off loans

        """
        for each liability
            balance: number
            interest_rate: number
            months_to_pay: number
        """
        pass

    def stocks_tab(self, bottom_frame: tk.Frame):
        pass

    def taxes_tab(self, bottom_frame: tk.Frame):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = View(root)
    root.mainloop()