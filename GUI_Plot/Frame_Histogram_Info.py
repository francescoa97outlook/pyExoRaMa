import tkinter as tk


class Frame_Histogram_Info:
    gui = None
    frame_histogram_info = None
    label = None
    mass_bin = None
    radius_bin = None
    zeta_bin = None
    mass_btn = None
    radius_btn = None
    mass_label_plot = None
    radius_label_plot = None
    mass_bin_var = None
    radius_bin_var = None
    zeta_bin_var = None

    def __init__(self, window, gui):
        self.gui = gui
        self.frame_histogram_info = tk.Frame(window, highlightbackground="black", highlightthickness=1, padx=5, pady=2)
        self.label = tk.Label(master=self.frame_histogram_info, text='Histogram: mass bin ', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(column=0, row=0)
        numbers = [i for i in range(0, 25)]
        numbers.extend([30, 40, 50, 60, 70, 80, 90, 100])
        self.mass_bin_var = tk.IntVar()
        self.mass_bin = tk.OptionMenu(self.frame_histogram_info, self.mass_bin_var, *numbers)
        self.mass_bin.grid(column=1, row=0)
        self.mass_bin_var.set(13)
        self.label = tk.Label(master=self.frame_histogram_info, text=' radius bin ', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(column=2, row=0)
        self.radius_bin_var = tk.IntVar()
        self.radius_bin = tk.OptionMenu(self.frame_histogram_info, self.radius_bin_var, *numbers)
        self.radius_bin.grid(column=3, row=0)
        self.radius_bin_var.set(24)
        self.label = tk.Label(master=self.frame_histogram_info, text=' ζ bin ', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(column=4, row=0)
        self.zeta_bin_var = tk.IntVar()
        self.zeta_bin = tk.OptionMenu(self.frame_histogram_info, self.zeta_bin_var, *numbers)
        self.zeta_bin.grid(column=5, row=0)
        self.zeta_bin_var.set(4)
        self.mass_btn = tk.Button(master=self.frame_histogram_info, text=" Change scale Mass ", command=self.mass_change_Scale, bg="#669999", font=('Sans', '8', 'bold'))
        self.mass_btn.grid(column=0, row=1, columnspan=2)
        self.mass_label_plot = tk.Label(master=self.frame_histogram_info, text='Count', fg="#ff6600", font=('Sans', '8', 'bold'), borderwidth=2, relief="ridge")
        self.mass_label_plot.grid(column=2, row=1)
        self.radius_btn = tk.Button(master=self.frame_histogram_info, text=" Change scale Radius ", command=self.radius_change_Scale, bg="#669999", font=('Sans', '8', 'bold'))
        self.radius_btn.grid(column=3, row=1, columnspan=2)
        self.radius_label_plot = tk.Label(master=self.frame_histogram_info, text='Count', fg="#ff6600", font=('Sans', '8', 'bold'), borderwidth=2, relief="ridge")
        self.radius_label_plot.grid(column=5, row=1)
        self.frame_histogram_info.pack(padx=3, pady=3)

    def mass_change_Scale(self):
        if self.mass_label_plot["text"] == "Count":
            self.mass_label_plot["text"] = "Log Count"
        else:
            self.mass_label_plot["text"] = "Count"

    def radius_change_Scale(self):
        if self.radius_label_plot["text"] == "Count":
            self.radius_label_plot["text"] = "Log Count"
        else:
            self.radius_label_plot["text"] = "Count"
