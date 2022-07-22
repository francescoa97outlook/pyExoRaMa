import tkinter as tk
import os
from GUI_Load_Data import Frame_Load_Data
from GUI_Load_Data import Frame_Constrains


class GUI_Data:
    # Window
    window = None
    # Input
    frame_load_data = None
    # Decide constrains
    frame_constrains = None

    def __init__(self):
        # Window
        self.window = tk.Tk()
        if "nt" == os.name:
            self.window.wm_iconbitmap(bitmap="pyExoRaMa-logos.ico")
        else:
            self.window.wm_iconbitmap(bitmap="@pyExoRaMa-logos.xbm")
        self.window.geometry("1600x670+100+100")
        self.window.title("Import Catalogue Helper")
        self.window.resizable(False, False)
        # Planet Inputs
        self.frame_load_data = Frame_Load_Data.Frame_Load_Data(self.window, self)
        # Decide constrains
        self.frame_constrains = Frame_Constrains.Frame_Constrains(self.window, self)
