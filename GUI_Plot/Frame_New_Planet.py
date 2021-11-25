import tkinter as tk


class Frame_New_Planet:
    gui = None
    frame_new_planet = None
    add_new_planet_check = None
    filter_new_planet_check = None
    label_new_planet_check = None
    add_new_planet_check_var = None
    filter_new_planet_check_var = None
    label_new_planet_check_var = None
    label_input = None
    text_input = None

    def __init__(self, window, gui, check_teq):
        self.gui = gui
        self.frame_new_planet = tk.Frame(window, highlightbackground="black", highlightthickness=1, padx=5, pady=2)
        self.add_new_planet_check_var = tk.IntVar()
        self.add_new_planet_check = tk.Checkbutton(master=self.frame_new_planet, text="Add new planet(s)?", variable=self.add_new_planet_check_var, fg="#cc3300", font=('Sans', '8', 'bold'))
        self.add_new_planet_check.grid(column=0, row=0)
        self.filter_new_planet_check_var = tk.IntVar()
        self.filter_new_planet_check = tk.Checkbutton(master=self.frame_new_planet, text="Filter new planet(s) by T_eq?", variable=self.filter_new_planet_check_var, fg="#cc3300", font=('Sans', '8', 'bold'))
        self.filter_new_planet_check.grid(column=1, row=0)
        if not check_teq:
            self.filter_new_planet_check.configure(state="disable")
        self.label_new_planet_check_var = tk.IntVar()
        self.label_new_planet_check = tk.Checkbutton(master=self.frame_new_planet, text="Show label(s)?", variable=self.label_new_planet_check_var, fg="#cc3300", font=('Sans', '8', 'bold'))
        self.label_new_planet_check.grid(column=2, row=0)
        self.label_input = tk.Label(master=self.frame_new_planet, text='Input example: [\"planet-name\", m(M⊕), \u03C3m+, \u03C3m-, r(R⊕), \u03C3r+, \u03C3r-, T_eq(K)]%[...]', fg="blue", font=('Sans', '8', 'bold'))
        self.label_input.grid(column=0, row=1, columnspan=3)
        self.text_input = tk.Text(master=self.frame_new_planet, height=10)
        self.text_input.grid(column=0, row=2, columnspan=3)
        self.text_input.insert(tk.END, "[\"TOI-1710 b\", 29, 5, 5, 5.3, 0.1, 0.1, 700]")
        self.frame_new_planet.pack(padx=3, pady=3)
