import tkinter as tk
from PIL import Image, ImageTk

# constants
WINDOW_SIZE = (600, 600)
PRIM_COLOR = "#e8e8e8"
SEC_COLOR = "#ababab"
WHITE = "#ffffff"
BLACK = "#000000"

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

        # styling defaults
        self.frame_styling = {"bg":PRIM_COLOR, "highlightbackground":SEC_COLOR, "highlightthickness":5}
        self.medium_font = ("Roboto", 20)

        # opening game
        self.set_menu("in_game")

    def set_background(self, path: str):
        bg_image = Image.open("View/back.jpg")
        bg_image = bg_image.resize((800, 600), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        self.bg_label = tk.Label(self.window, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    def set_menu(self, menu_name: str):
        self.clear_window()
        getattr(self, menu_name)()
        
    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()

    def in_game(self): # Load background image
        self.set_background("View/back.jpg")

        # top bar
        top_bar = tk.Frame(self.window, **self.frame_styling)
        top_bar.place(x=0, y=0, width=WINDOW_SIZE[0], height=60)

        # items in top bar
        top_bar.columnconfigure(0, weight=1)
        top_bar.columnconfigure(1, weight=1)
        top_bar.rowconfigure(0, weight=1)

        balance = tk.Label(top_bar, text="Balance: $0", bg=PRIM_COLOR, font=self.medium_font)
        date = tk.Label(top_bar, text="Date: January 3000", bg=PRIM_COLOR, font=self.medium_font)
        balance.grid(column=0, row=0)
        date.grid(column=1, row=0)

        # next button

        # bottom section
        bottom_frame = tk.Frame(self.window, **self.frame_styling)
        bottom_frame.place(x=0, y=WINDOW_SIZE[1], anchor="sw", width=WINDOW_SIZE[0], height=200)

if __name__ == "__main__":
    root = tk.Tk()
    app = View(root)
    root.mainloop()