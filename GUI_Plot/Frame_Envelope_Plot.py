import os
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox as msgbox


def helpButtonFunc():
    msgbox.showinfo(title="INFO", message="Plot options: \nChoose the type of light gaseous envelope on top of planet cores (made up of different compositions: Fe/metals, silicates, or ices). \nThe corresponding mass-radius theoretical models will be plotted, with the different specific entropy S (eV/1000K/atom) contours that are based on the definition of the integral parameter z, as detailed in Eq. 17 of Zeng et al. (2021).")


class Frame_Envelope_Plot:
    gui = None
    frame_envelope_plot = None
    img = None
    label = None
    envelope_btn = None
    label_envelope = None
    choose_cmap = None
    choose_cmap_var = None
    help_button = None

    def __init__(self, window, gui):
        self.gui = gui
        self.frame_envelope_plot = tk.Frame(window, highlightbackground="black", highlightthickness=1, padx=5, pady=2)
        self.label = tk.Label(master=self.frame_envelope_plot, text=' Envelope: ', fg="blue", font=('Sans', '9', 'bold'))
        self.label.grid(column=0, row=0)
        self.envelope_btn = tk.Button(master=self.frame_envelope_plot, text=" Change envelope ", command=self.changeEnvelope, bg="#669999", font=('Sans', '9', 'bold'))
        self.envelope_btn.grid(column=1, row=0)
        self.label_envelope = tk.Label(master=self.frame_envelope_plot, text='None', fg="#ff6600", font=('Sans', '9', 'bold'), borderwidth=2, relief="ridge")
        self.label_envelope.grid(column=2, row=0)
        self.img = ImageTk.PhotoImage(Image.open("Image" + os.sep + "Integral_Symbol.PNG"))
        self.label = tk.Label(master=self.frame_envelope_plot, text=' CMAP:', fg="blue", font=('Sans', '9', 'bold'))
        self.label.grid(column=4, row=0)
        options_list = ["inferno", "viridis", "plasma", "magma", "cividis", "Greys", "Purples", "Blues", "Greens", "Oranges", "Reds", "YlOrBr", "YlOrRd", "OrRd", "PuRd", "RdPu", "BuPu", "GnBu", "PuBu", "YlGnBu", "PuBuGn", "BuGn", "YlGn", "brg", "gist_rainbow", "rainbow", "jet", "terrain", "turbo", "nipy_spectral", "gist_ncar"]
        self.choose_cmap_var = tk.StringVar()
        self.choose_cmap = tk.OptionMenu(self.frame_envelope_plot, self.choose_cmap_var, *options_list)
        self.choose_cmap.grid(column=5, row=0)
        self.choose_cmap_var.set("inferno")
        self.help_button = tk.Button(master=self.frame_envelope_plot, text="?", command=helpButtonFunc, bg="black", fg="yellow", font=('Sans', '10', 'bold'))
        self.help_button.grid(column=6, row=0)
        self.label = tk.Label(master=self.frame_envelope_plot, image=self.img)
        self.label.grid(column=0, row=1, columnspan=7)
        self.frame_envelope_plot.pack(padx=3, pady=3)

    def changeEnvelope(self):
        if self.label_envelope["text"] == "None":
            self.label_envelope["text"] = "H20"
        elif self.label_envelope["text"] == "H20":
            self.label_envelope["text"] = "Silicates"
        elif self.label_envelope["text"] == "Silicates":
            self.label_envelope["text"] = "Fe"
        else:
            self.label_envelope["text"] = "None"
