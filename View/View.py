import tkinter as tk
from PIL import Image, ImageTk

import math

# constants
WINDOW_SIZE = (900, 600)
POPUP_SIZE = (300, 200)
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
    "",
    " K",
    " M",
    " B",
    " T",
    " Qd",
    " Qn"
]
STARTING_YEAR = 3000
TAB_BACKGROUNDS = {
    "stats_tab" : "../View/backgrounds/unicorn space.jpg",
    "assets_tab" : "../View/backgrounds/assets.jpg",
    "liabilities_tab" : "../View/backgrounds/Liabilities.jpg",
    "asset_market_tab" : "../View/backgrounds/markets.jpg",
    "taxes_tab" : "../View/backgrounds/tax.jpg",
    "career_tab" : "../View/backgrounds/careers.jpg",
}

# class
class View:
    def __init__(self, window: tk.Tk, control):
        self.control = control

        # configuring window
        self.window = window
        self.window.title("Space Finance Simulator")
        self.window.geometry(str(WINDOW_SIZE[0]) + "x" + str(WINDOW_SIZE[1]))

        # properties
        self.bg_photo = None
        self.bg_label = None
        self.current_menu = ""
        self.current_tab = "stats_tab"
        self.current_popup = None

        # stats
        self.balance = tk.StringVar(self.window, "Balance: $0")
        self.date = tk.StringVar(self.window, "Date: January 3000")

        self.credit_score = tk.StringVar(self.window, "Credit Score: 0")
        self.income = tk.StringVar(self.window, "Income: $0/month")
        self.net_worth = tk.StringVar(self.window, "Net Worth: $0")
        self.occupation = tk.StringVar(self.window, "Occupation: Unemployed")

        self.assets = tk.StringVar(self.window, "Assets: 0")
        self.liabilities = tk.StringVar(self.window, "Liabilities: 0")
        self.ra = tk.StringVar(self.window, "Risk Adversion: 0")

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
    
    def input_popup(self, prompt: str, callback):
        """
        Creates a popup display with an input, and returns the value that is inputted.
        """

        # setting properties / values
        self.current_popup = lambda :self.input_popup(prompt)
        entry_text = tk.StringVar(self.window)

        # creating popup frame
        frame = tk.Frame(self.window, **self.frame_styling, width=POPUP_SIZE[0], height=POPUP_SIZE[1])
        frame.place(anchor="center", x=int(WINDOW_SIZE[0]/2), y=int(WINDOW_SIZE[1]/2))

        label = tk.Label(frame, bg=PRIM_COLOR, text=prompt, font=self.small_font, wraplength=POPUP_SIZE[0])
        entry = tk.Entry(frame, textvariable=entry_text, font=self.small_font)
        confirm = tk.Button(frame, bg=GREEN, text="Confirm", width=10, font=self.small_font)

        label.grid(column=0, row=0, **self.padding_10)
        entry.grid(column=0, row=1, **self.padding_10)
        confirm.grid(column=0, row=2, **self.padding_10)

        # return function
        def on_confirm():

            # running callback
            callback(entry_text.get())

            # destroying popup
            label.destroy()
            entry.destroy()
            frame.destroy()
            self.current_popup = None
        
        # close button
        confirm.config(command=on_confirm)
    
    def popup_display(self, message: str, destroy_callback=None, button_text="OK"):
        """
        Creates a popup display and returns a function that removes that popup display upon calling.
        """

        self.current_popup = lambda :self.popup_display(message, destroy_callback, button_text)

        # creating popup frame
        frame = tk.Frame(self.window, **self.frame_styling, width=POPUP_SIZE[0], height=POPUP_SIZE[1])
        frame.place(anchor="center", x=int(WINDOW_SIZE[0]/2), y=int(WINDOW_SIZE[1]/2))

        label = tk.Label(frame, bg=PRIM_COLOR, text=message, font=self.small_font, wraplength=POPUP_SIZE[0])
        ok_button = tk.Button(frame, bg=GREEN, text=button_text, width=10, font=self.small_font)

        label.grid(column=0, row=0, **self.padding_10)
        ok_button.grid(column=0, row=1, **self.padding_10)

        # return function
        def remove():

            # destroying popup
            label.destroy()
            frame.destroy()
            self.current_popup = None

            # destroy callback
            if destroy_callback != None:
                destroy_callback()
        
        # close button
        ok_button.config(command=remove)

        return remove
    
    def tax_popup(self, destroy_callback=None):
        """
        Creates a popup display for paying taxes with various information.
        """

        self.current_popup = lambda :self.tax_popup(destroy_callback)

        # getting tax strings
        player = self.control.player

        income_tax = View.format_number(player.tax.income_tax_owed)
        capital_tax = View.format_number(player.tax.capital_gains_tax_owed)
        property_tax = View.format_number(player.tax.property_tax_owed)
        business_tax = View.format_number(player.tax.business_tax_owed)
        total_tax = View.format_number(player.tax.taxes_owed)

        # creating popup frame
        frame = tk.Frame(self.window, **self.frame_styling, width=POPUP_SIZE[0], height=POPUP_SIZE[1])
        frame.place(anchor="center", x=int(WINDOW_SIZE[0]/2), y=int(WINDOW_SIZE[1]/2))

        label = tk.Label(frame, bg=PRIM_COLOR, font=self.medium_font, wraplength=POPUP_SIZE[0], text="Your taxes are due!")
        income = tk.Label(frame, bg=PRIM_COLOR, font=self.small_font, wraplength=POPUP_SIZE[0], text="Income Tax: $" + income_tax)
        capital = tk.Label(frame, bg=PRIM_COLOR, font=self.small_font, wraplength=POPUP_SIZE[0], text="Capital Gains Tax: $" + capital_tax)
        property = tk.Label(frame, bg=PRIM_COLOR, font=self.small_font, wraplength=POPUP_SIZE[0], text="Property Tax: $" + property_tax)
        business = tk.Label(frame, bg=PRIM_COLOR, font=self.small_font, wraplength=POPUP_SIZE[0], text="Business Tax: $" + business_tax)
        total = tk.Label(frame, bg=PRIM_COLOR, font=self.small_font, wraplength=POPUP_SIZE[0], text="Total: $" + total_tax)
        ok_button = tk.Button(frame, bg=GREEN, text="Pay", width=10, font=self.small_font)

        label.grid(column=0, row=0, **self.padding_10)
        income.grid(column=0, row=1, **self.padding_5)
        capital.grid(column=0, row=2, **self.padding_5)
        property.grid(column=0, row=3, **self.padding_5)
        business.grid(column=0, row=4, **self.padding_5)
        total.grid(column=0, row=5, **self.padding_5)
        ok_button.grid(column=0, row=6, **self.padding_10)

        # return function
        def remove():

            # destroying popup
            label.destroy()
            frame.destroy()
            self.current_popup = None

            # destroy callback
            if destroy_callback != None:
                destroy_callback()
        
        # close button
        ok_button.config(command=remove)

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
            self.assets.set("Assets: $" + str(View.format_number(stats_dict["assets"])))
        if "liabilities" in stats_dict:
            self.liabilities.set("Liabilities: $" + str(View.format_number(stats_dict["liabilities"])))
        if "ra" in stats_dict:
            self.ra.set("Risk Adversion: " + str(stats_dict["ra"]))
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

        # refreshing and setting new menu
        self.clear_window()
        self.current_menu = menu_name
        getattr(self, menu_name)(*args)

        # adding popup again
        if self.current_popup != None:
            self.current_popup()
        
    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def in_game(self, current_tab: str = None, background=None):

        # managing background
        if current_tab == None:
            current_tab = self.current_tab

        if background == None:
            background = TAB_BACKGROUNDS[current_tab]
            
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
        asset_market_tab = tk.Button(tabs_frame, text="Asset markets", bg=PRIM_COLOR, font=self.small_font)
        taxes_tab = tk.Button(tabs_frame, text="Taxes", bg=PRIM_COLOR, font=self.small_font)
        career_tab = tk.Button(tabs_frame, text="Career", bg=PRIM_COLOR, font=self.small_font)

        stats_tab.grid(column=0, row=0)
        assets_tab.grid(column=1, row=0)
        liabilities_tab.grid(column=2, row=0)
        asset_market_tab.grid(column=3, row=0)
        taxes_tab.grid(column=4, row=0)
        career_tab.grid(column=5, row=0)

        # coloring selected tab
        self.current_tab = current_tab

        if current_tab == "stats_tab":
            stats_tab.config(bg=SELECTED_COLOR)
        elif current_tab == "assets_tab":
            assets_tab.config(bg=SELECTED_COLOR)
        elif current_tab == "liabilities_tab":
            liabilities_tab.config(bg=SELECTED_COLOR)
        elif current_tab == "asset_market_tab":
            asset_market_tab.config(bg=SELECTED_COLOR)
        elif current_tab == "taxes_tab":
            taxes_tab.config(bg=SELECTED_COLOR)
        elif current_tab == "career_tab":
            career_tab.config(bg=SELECTED_COLOR)

        # connecting buttons
        def switch_tab(new_tab: str):
            self.set_menu("in_game", new_tab)

        def on_next_button():
            print('next button')
            if self.control.game.tax_lock == False:
                print('unlocked')
                self.control.monthly_update()

        stats_tab.config(command=lambda :switch_tab("stats_tab"))
        assets_tab.config(command=lambda :switch_tab("assets_tab"))
        liabilities_tab.config(command=lambda :switch_tab("liabilities_tab"))
        asset_market_tab.config(command=lambda :switch_tab("asset_market_tab"))
        taxes_tab.config(command=lambda :switch_tab("taxes_tab"))
        career_tab.config(command=lambda :switch_tab("career_tab"))

        next_button.config(command=on_next_button)

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
        ra = tk.Label(bottom_frame, textvariable=self.ra, font=self.small_font, bg=PRIM_COLOR)
        # adding to display
        credit_score.grid(column=0, row=0, sticky="W", padx=(5,25), pady=5)
        income.grid(column=0, row=1, sticky="W", padx=(5,25), pady=5)
        net_worth.grid(column=0, row=2, sticky="W", padx=(5,25), pady=5)
        occupation.grid(column=0, row=3, sticky="W", padx=(5,25), pady=5)

        assets.grid(column=1, row=0, sticky="W", **self.padding_5)
        liabilities.grid(column=1, row=1, sticky="W", **self.padding_5)
        ra.grid(column=1, row=2, sticky="W", **self.padding_5)

    def assets_tab(self, bottom_frame: tk.Frame):

        # creating items
        scrollbar = tk.Scrollbar(bottom_frame, orient="vertical")
        listbox = tk.Listbox(bottom_frame, **self.frame_styling, yscrollcommand=scrollbar.set, font=self.small_font)
        data_frame = tk.Frame(bottom_frame, **self.frame_styling)

        scrollbar.config(command=listbox.yview)

        value = tk.Label(data_frame, font=self.small_font, bg=PRIM_COLOR)
        cash_flow = tk.Label(data_frame, font=self.small_font, bg=PRIM_COLOR)
        mean_apr = tk.Label(data_frame, font=self.small_font, bg=PRIM_COLOR)
        std_apr = tk.Label(data_frame, font=self.small_font, bg=PRIM_COLOR)
        liability = tk.Label(data_frame, font=self.small_font, bg=PRIM_COLOR)
        sell = tk.Button(data_frame, text="Sell", bg=PRIM_COLOR, font=self.small_font)

        # adding to display
        bottom_frame.columnconfigure(0, weight=1)
        bottom_frame.columnconfigure(1, weight=0)
        bottom_frame.columnconfigure(2, weight=50)
        bottom_frame.rowconfigure(0, weight=1)

        listbox.grid(column=0, row=0, padx=(10, 0), pady=10, sticky="NESW")
        scrollbar.grid(column=1, row=0, padx=(0, 10), pady=10, sticky="NSW")
        data_frame.grid(column=2, row=0, **self.padding_10, sticky="NESW")

        # getting data
        assets: list = self.control.player.assets

        # adding assets
        for asset in assets:
            listbox.insert(tk.END, asset.name)

        # configuring listbox
        def listbox_select(event: tk.Event):
            if len(assets) == 0:
                return

            # finding asset based on selection
            selected = event.widget.curselection()
            asset_name = listbox.get(selected[0])
            asset = None

            for other_asset in assets:
                if other_asset.name == asset_name:
                    asset = other_asset
                    break

            # updating information
            value.config(text="Value: $" + str(View.format_number(asset.value)))
            cash_flow.config(text="Cash Flow: $" + str(View.format_number(asset.income)) + "/month")
            mean_apr.config(text="Mean Return: " + str(asset.apr_mean * 100) + "%")
            std_apr.config(text="STD Return: " + str(asset.apr_std * 100) + "%")
            if asset.liability != None:
                liability.config(text="Liability: " + asset.liability.name)

            # configuring sell button
            sell.config(command=lambda : self.control.sell_asset(asset_name))
            
            # adding items
            value.grid(column=0, row=0, padx=(5, 15), pady=5, stick="W")
            cash_flow.grid(column=0, row=1, padx=(5, 15), pady=5, stick="W")
            mean_apr.grid(column=0, row=2, padx=(5, 15), pady=5, stick="W")
            std_apr.grid(column=1, row=0, padx=(5, 15), pady=5, stick="W")
            liability.grid(column=1, row=1, padx=(5, 15), pady=5, stick="W")
            sell.grid(column=2, row=0, padx=(5, 15), pady=5, sticky="EW")
            if asset.liability == None:
                liability.grid_forget()

        listbox.bind("<<ListboxSelect>>", listbox_select)

    def liabilities_tab(self, bottom_frame: tk.Frame):

        # creating items
        scrollbar = tk.Scrollbar(bottom_frame, orient="vertical")
        listbox = tk.Listbox(bottom_frame, **self.frame_styling, yscrollcommand=scrollbar.set, font=self.small_font)
        data_frame = tk.Frame(bottom_frame, **self.frame_styling)

        scrollbar.config(command=listbox.yview)

        balance = tk.Label(data_frame, font=self.small_font, text="Balance: $0", bg=PRIM_COLOR)
        interest_rate = tk.Label(data_frame, font=self.small_font, text="Interest Rate: 5%", bg=PRIM_COLOR)
        months_to_pay = tk.Label(data_frame, font=self.small_font, text="Months to Pay: 0", bg=PRIM_COLOR)

        # adding to display
        bottom_frame.columnconfigure(0, weight=1)
        bottom_frame.columnconfigure(1, weight=0)
        bottom_frame.columnconfigure(2, weight=50)
        bottom_frame.rowconfigure(0, weight=1)

        listbox.grid(column=0, row=0, padx=(10, 0), pady=10, sticky="NESW")
        scrollbar.grid(column=1, row=0, padx=(0, 10), pady=10, sticky="NSW")
        data_frame.grid(column=2, row=0, **self.padding_10, sticky="NESW")

        # getting data
        liabilities: list = self.control.player.liabilities

        # adding assets
        for liability in liabilities:
            listbox.insert(tk.END, liability.name)

        # configuring listbox
        def listbox_select(event: tk.Event):
            selected = event.widget.curselection()
            if len(selected) < 1:
                return
            
            liability_name = listbox.get(selected[0])
            liability = None

            for other_liability in liabilities:
                if other_liability.name == liability_name:
                    liability = other_liability
                    break

            # updating information
            balance.config(text="Balance: $" + str(View.format_number(liability.debt_amount)))
            interest_rate.config(text="Interest Rate: " + str(liability.interest_rate * 100) + "%")
            months_to_pay.config(text="Months to Pay: " + str(liability.months_left))

            # adding items
            balance.grid(column=0, row=0, padx=(5, 15), pady=5, stick="W")
            interest_rate.grid(column=0, row=1, padx=(5, 15), pady=5, stick="W")
            months_to_pay.grid(column=0, row=2, padx=(5, 15), pady=5, stick="W")

        listbox.bind("<<ListboxSelect>>", listbox_select)

    def asset_market_tab(self, bottom_frame: tk.Frame):

        # buy/sell assets and liabilities
        scrollbar = tk.Scrollbar(bottom_frame, orient="vertical")
        listbox = tk.Listbox(bottom_frame, **self.frame_styling, yscrollcommand=scrollbar.set, font=self.small_font)
        data_frame = tk.Frame(bottom_frame, **self.frame_styling)

        scrollbar.config(command=listbox.yview)

        value = tk.Label(data_frame, font=self.small_font, bg=PRIM_COLOR)
        cash_flow = tk.Label(data_frame, font=self.small_font, bg=PRIM_COLOR)
        mean_apr = tk.Label(data_frame, font=self.small_font, bg=PRIM_COLOR)
        std_apr = tk.Label(data_frame, font=self.small_font, bg=PRIM_COLOR)
        liability = tk.Label(data_frame, font=self.small_font, bg=PRIM_COLOR)
        buy = tk.Button(data_frame, text="Buy", bg=PRIM_COLOR, font=self.small_font)

        # adding to display
        bottom_frame.columnconfigure(0, weight=1)
        bottom_frame.columnconfigure(1, weight=0)
        bottom_frame.columnconfigure(2, weight=50)
        bottom_frame.rowconfigure(0, weight=1)

        listbox.grid(column=0, row=0, padx=(10, 0), pady=10, sticky="NESW")
        scrollbar.grid(column=1, row=0, padx=(0, 10), pady=10, sticky="NSW")
        data_frame.grid(column=2, row=0, **self.padding_10, sticky="NESW")

        # getting data
        assets: list = self.control.data[self.control.game.level][0]
        

        # adding assets
        for asset in assets:
            listbox.insert(tk.END, asset.name)

        # configuring listbox
        def listbox_select(event: tk.Event):
            selected = event.widget.curselection()
            asset_name = listbox.get(selected[0])
            asset = None

            for other_asset in assets:
                if other_asset.name == asset_name:
                    asset = other_asset
                    break

            # updating information
            value.config(text="Value: $" + str(View.format_number(asset.value)))
            cash_flow.config(text="Cash Flow: $" + str(View.format_number(asset.income)) + "/month")
            mean_apr.config(text="Mean Return: " + str(asset.apr_mean * 100) + "%")
            std_apr.config(text="STD Return: " + str(asset.apr_std * 100) + "%")
            if asset.liability != None:
                liability.config(text="Liability: " + asset.liability.name)

            buy.config(command=lambda :self.control.buy_asset(asset_name))

            value.grid(column=0, row=0, padx=(5, 15), pady=5, stick="W")
            cash_flow.grid(column=0, row=1, padx=(5, 15), pady=5, stick="W")
            mean_apr.grid(column=0, row=2, padx=(5, 15), pady=5, stick="W")
            std_apr.grid(column=1, row=0, padx=(5, 15), pady=5, stick="W")
            liability.grid(column=1, row=1, padx=(5, 15), pady=5, stick="W")
            buy.grid(column=2, row=0, padx=(5, 15), pady=5, sticky="EW")

        listbox.bind("<<ListboxSelect>>", listbox_select)

    def taxes_tab(self, bottom_frame: tk.Frame):

        # taxes tab
        data_frame = tk.Frame(bottom_frame, **self.frame_styling)
        liability = tk.Label(data_frame, font=self.small_font, bg=PRIM_COLOR)
        buy = tk.Button(data_frame, text="Pay", bg=PRIM_COLOR, font=self.small_font)
        data_frame.grid(column=0, row=0, **self.padding_10, sticky="NESW")

        tax_amount_str = View.format_number(self.control.player.tax.taxes_owed)
        liability.config(text="Liability: $" + tax_amount_str)
        buy.config(command=lambda : self.control.pay_all_taxes())

        liability.grid(column=0, row=0, padx=(5, 15), pady=5, stick="W")
        buy.grid(column=1, row=0, padx=(5, 15), pady=5, sticky="EW")

    def career_tab(self, bottom_frame: tk.Frame):

        # buy/sell assets and liabilities
        scrollbar = tk.Scrollbar(bottom_frame, orient="vertical")
        listbox = tk.Listbox(bottom_frame, **self.frame_styling, yscrollcommand=scrollbar.set, font=self.small_font)
        data_frame = tk.Frame(bottom_frame, **self.frame_styling)

        scrollbar.config(command=listbox.yview)

        income = tk.Label(data_frame, font=self.small_font, bg=PRIM_COLOR)
     
        buy = tk.Button(data_frame, text="Work", bg=PRIM_COLOR, font=self.small_font)

        # adding to display
        bottom_frame.columnconfigure(0, weight=1)
        bottom_frame.columnconfigure(1, weight=0)
        bottom_frame.columnconfigure(2, weight=50)
        bottom_frame.rowconfigure(0, weight=1)

        listbox.grid(column=0, row=0, padx=(10, 0), pady=10, sticky="NESW")
        scrollbar.grid(column=1, row=0, padx=(0, 10), pady=10, sticky="NSW")
        data_frame.grid(column=2, row=0, **self.padding_10, sticky="NESW")

        # getting data
        careers: list = self.control.data[self.control.game.level][1]

        # adding assets
        for career in careers:
            listbox.insert(tk.END, career.title)

        # configuring listbox
        def listbox_select(event: tk.Event):
            selected = event.widget.curselection()
            career_name = listbox.get(selected[0])
            career = None

            for other_career in careers:
                if other_career.title == career_name:
                    career = other_career
                    break

            # updating information
            income.config(text="Income: $" + str(View.format_number(career.income)))
       

            buy.config(command=lambda :self.control.buy_career(career_name))

            income.grid(column=0, row=0, padx=(5, 15), pady=5, stick="W")

            buy.grid(column=1, row=0, padx=(5, 15), pady=5, sticky="EW")

        listbox.bind("<<ListboxSelect>>", listbox_select)