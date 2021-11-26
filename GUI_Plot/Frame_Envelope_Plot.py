import os
import tkinter as tk
from PIL import ImageTk, Image


class Frame_Envelope_Plot:
    gui = None
    frame_envelope_plot = None
    img = None
    label = None
    envelope_btn = None
    label_envelope = None
    choose_cmap = None
    choose_cmap_var = None

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
        self.label = tk.Label(master=self.frame_envelope_plot, image=self.img)
        self.label.grid(column=0, row=1, columnspan=6)
        self.label = tk.Label(master=self.frame_envelope_plot, text=' CMAP:', fg="blue", font=('Sans', '9', 'bold'))
        self.label.grid(column=4, row=0)
        options_list = ["inferno", "viridis", "plasma", "magma", "cividis", "Greys", "Purples", "Blues", "Greens", "Oranges", "Reds", "YlOrBr", "YlOrRd", "OrRd", "PuRd", "RdPu", "BuPu", "GnBu", "PuBu", "YlGnBu", "PuBuGn", "BuGn", "YlGn", "brg", "gist_rainbow", "rainbow", "jet", "terrain", "turbo", "nipy_spectral", "gist_ncar"]
        self.choose_cmap_var = tk.StringVar()
        self.choose_cmap = tk.OptionMenu(self.frame_envelope_plot, self.choose_cmap_var, *options_list)
        self.choose_cmap.grid(column=5, row=0)
        self.choose_cmap_var.set("inferno")
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
