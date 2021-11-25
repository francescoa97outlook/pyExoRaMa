import tkinter as tk


class Frame_Scale_Plot:
    gui = None
    frame_scale_plot = None
    label = None
    mass_button_scale = None
    mass_label_scale = None
    mass_min = None
    mass_max = None
    radius_button_scale = None
    radius_label_scale = None
    radius_min = None
    radius_max = None

    def __init__(self, window, gui):
        self.gui = gui
        self.frame_scale_plot = tk.Frame(window, highlightbackground="black", highlightthickness=1, padx=5, pady=2)
        self.label = tk.Label(master=self.frame_scale_plot, text='M scale: ', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(column=0, row=0)
        self.mass_button_scale = tk.Button(master=self.frame_scale_plot, text=" Change scale ", bg="#669999", font=('Sans', '9', 'bold'), command=self.mass_change_Scale)
        self.mass_button_scale.grid(column=1, row=0)
        self.mass_label_scale = tk.Label(master=self.frame_scale_plot, text='Log', fg="#ff6600", font=('Sans', '8', 'bold'), borderwidth=2, relief="ridge")
        self.mass_label_scale.grid(column=2, row=0)
        self.label = tk.Label(master=self.frame_scale_plot, text=' M⊕ min: ', fg="red", font=('Sans', '9', 'bold'))
        self.label.grid(column=3, row=0)
        self.mass_min = tk.Entry(master=self.frame_scale_plot, width=10)
        self.mass_min.grid(column=4, row=0)
        self.mass_min.insert(-1, "1")
        self.label = tk.Label(master=self.frame_scale_plot, text=' M⊕ max: ', fg="red", font=('Sans', '9', 'bold'))
        self.label.grid(column=5, row=0)
        self.mass_max = tk.Entry(master=self.frame_scale_plot, width=10)
        self.mass_max.grid(column=6, row=0)
        self.mass_max.insert(-1, "3000")
        self.label = tk.Label(master=self.frame_scale_plot, text='R scale: ', fg="blue", font=('Sans', '9', 'bold'))
        self.label.grid(column=0, row=1)
        self.radius_button_scale = tk.Button(master=self.frame_scale_plot, text=" Change scale ", bg="#669999", font=('Sans', '8', 'bold'), command=self.radius_change_Scale)
        self.radius_button_scale.grid(column=1, row=1)
        self.radius_label_scale = tk.Label(master=self.frame_scale_plot, text='Log', fg="#ff6600", font=('Sans', '8', 'bold'), borderwidth=2, relief="ridge")
        self.radius_label_scale.grid(column=2, row=1)
        self.label = tk.Label(master=self.frame_scale_plot, text=' R⊕ min: ', fg="red", font=('Sans', '8', 'bold'))
        self.label.grid(column=3, row=1)
        self.radius_min = tk.Entry(master=self.frame_scale_plot, width=10)
        self.radius_min.grid(column=4, row=1)
        self.radius_min.insert(-1, "1")
        self.label = tk.Label(master=self.frame_scale_plot, text=' R⊕ max: ',  fg="red", font=('Sans', '8', 'bold'))
        self.label.grid(column=5, row=1)
        self.radius_max = tk.Entry(master=self.frame_scale_plot, width=10)
        self.radius_max.grid(column=6, row=1)
        self.radius_max.insert(-1, "25")
        self.frame_scale_plot.pack(padx=3, pady=3)

    def mass_change_Scale(self):
        if self.mass_label_scale["text"] == "Linear":
            self.mass_label_scale["text"] = "Log"
        else:
            self.mass_label_scale["text"] = "Linear"

    def radius_change_Scale(self):
        if self.radius_label_scale["text"] == "Linear":
            self.radius_label_scale["text"] = "Log"
        else:
            self.radius_label_scale["text"] = "Linear"
