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

        # opening game
        self.set_menu("in_game")

    def set_background(self, path: str):
        image = Image.open("View/back.jpg")
        image = image.resize(WINDOW_SIZE, Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self.window, image=photo)
        label.place(x=0, y=0, relwidth=1, relheight=1)

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