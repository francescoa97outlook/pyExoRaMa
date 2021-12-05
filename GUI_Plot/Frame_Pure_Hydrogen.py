import tkinter as tk
from tkinter import messagebox as msgbox


def helpButtonFunc():
    msgbox.showinfo(title="INFO", message="Plot options: \nSelecting this options will plot mass-radius curves of different specific entropy S which are especially interesting for comparing exoplanet gas giants.")


class Frame_Pure_Hydrogen:
    gui = None
    frame_pure_hydrogen = None
    mass_radius_check = None
    mass_radius_check_var = None
    central_density_check = None
    central_density_check_var = None
    help_button = None

    def __init__(self, window, gui):
        self.gui = gui
        self.frame_pure_hydrogen = tk.Frame(window, highlightbackground="black", highlightthickness=1, padx=5, pady=2)
        self.mass_radius_check_var = tk.IntVar()
        self.mass_radius_check = tk.Checkbutton(master=self.frame_pure_hydrogen, text="Show pure-Hydrogen mass-radius?", variable=self.mass_radius_check_var, fg="#cc3300", font=('Sans', '9', 'bold'))
        self.mass_radius_check.grid(column=0, row=0)
        self.central_density_check_var = tk.IntVar()
        self.central_density_check = tk.Checkbutton(master=self.frame_pure_hydrogen, text="Show pure-Hydrogen central density?", variable=self.central_density_check_var, fg="#cc3300", font=('Sans', '9', 'bold'))
        self.central_density_check.grid(column=1, row=0)
        self.help_button = tk.Button(master=self.frame_pure_hydrogen, text="?", command=helpButtonFunc, bg="black", fg="yellow", font=('Sans', '10', 'bold'))
        self.help_button.grid(column=2, row=0)
        self.frame_pure_hydrogen.pack(padx=3, pady=3)
