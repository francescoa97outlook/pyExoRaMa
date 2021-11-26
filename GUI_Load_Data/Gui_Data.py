import tkinter as tk

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
        self.window.geometry("1600x775+100+100")
        self.window.title("Manipulate Planet Code")
        self.window.resizable(False, False)
        # Planet Inputs
        self.frame_load_data = Frame_Load_Data.Frame_Load_Data(self.window, self)
        # Decide constrains
        self.frame_constrains = Frame_Constrains.Frame_Constrains(self.window, self)
