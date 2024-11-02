

import tkinter as tk
from PIL import Image, ImageTk
class SpaceFinanceView:
    def __init__(self, master):
        self.master = master
        self.master.title("Space Finance Simulator")
        self.master.geometry("800x600")

        # Load background image
        bg_image = Image.open("View/back.jpg")
        bg_image = bg_image.resize((800, 600), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        self.bg_label = tk.Label(self.master, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create main frame
        #self.main_frame = ttk.Frame(self.master, padding="10")
        #self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Balance display
        #ttk.Label(self.main_frame, text="Current Balance:").grid(row=0, column=0, sticky=tk.W, pady=5)
        #self.balance_var = tk.StringVar(value="$1,000,000")
        #ttk.Label(self.main_frame, textvariable=self.balance_var, font=("Arial", 14, "bold")).grid(row=0, column=1, sticky=tk.W, pady=5)

      



if __name__ == "__main__":
    root = tk.Tk()
    app = SpaceFinanceView(root)
    root.mainloop()