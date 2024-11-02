import tkinter as tk
from PIL import Image, ImageTk

# constants
WINDOW_SIZE = (600, 600)

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

        label = tk.Label(self.window, text="Hello world")
        label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = View(root)
    root.mainloop()