import tkinter as tk

import pandas as pd


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
    mass_np = None
    mass_sn_np = None
    mass_sp_np = None
    radius_np = None
    radius_sn_np = None
    radius_sp_np = None
    age_host_np = None
    tstar_np = None
    mstar_np = None
    rstar_np = None
    tplanet_np = None
    fe_h_np = None
    ecc_np = None
    p_orb_np = None
    a_orb_np = None
    add_planet_btn = None
    delete_planet_btn = None
    list_planet_btn = None
    name_np = None
    input_list = None

    def __init__(self, window, gui, check_age_host, check_ecc, check_FeH, check_tstar, check_p_orb, check_a_orb, check_teq, check_mass_star, check_radius_star):
        self.gui = gui
        self.frame_new_planet = tk.Frame(window, highlightbackground="black", highlightthickness=1, padx=5, pady=2)
        self.add_new_planet_check_var = tk.IntVar()
        self.add_new_planet_check = tk.Checkbutton(master=self.frame_new_planet, text="Add new planet(s)?", variable=self.add_new_planet_check_var, fg="#cc3300", font=('Sans', '9', 'bold'))
        self.add_new_planet_check.grid(column=0, row=0, columnspan=3)
        self.filter_new_planet_check_var = tk.IntVar()
        self.filter_new_planet_check = tk.Checkbutton(master=self.frame_new_planet, text="Filter new planet(s) by T_eq?", variable=self.filter_new_planet_check_var, fg="#cc3300", font=('Sans', '9', 'bold'))
        self.filter_new_planet_check.grid(column=3, row=0, columnspan=3)
        if not check_teq:
            self.filter_new_planet_check.configure(state="disable")
        self.label_new_planet_check_var = tk.IntVar()
        self.label_new_planet_check = tk.Checkbutton(master=self.frame_new_planet, text="Show label(s)?", variable=self.label_new_planet_check_var, fg="#cc3300", font=('Sans', '9', 'bold'))
        self.label_new_planet_check.grid(column=6, row=0, columnspan=3)

        self.label = tk.Label(master=self.frame_new_planet, text='Mass P:', fg="blue", font=('Sans', '9', 'bold'))
        self.label.grid(column=0, row=1)
        self.mass_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.mass_np.grid(column=1, row=1)
        self.mass_np.insert(tk.END, "0")

        self.label = tk.Label(master=self.frame_new_planet, text='Mass \u03C3- P:', fg="blue", font=('Sans', '9', 'bold'))
        self.label.grid(column=2, row=1)
        self.mass_sn_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.mass_sn_np.grid(column=3, row=1)
        self.mass_sn_np.insert(tk.END, "0")

        self.label = tk.Label(master=self.frame_new_planet, text='Mass \u03C3+ P:', fg="blue", font=('Sans', '9', 'bold'))
        self.label.grid(column=4, row=1)
        self.mass_sp_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.mass_sp_np.grid(column=5, row=1)
        self.mass_sp_np.insert(tk.END, "0")

        self.label = tk.Label(master=self.frame_new_planet, text='Radius P:', fg="blue", font=('Sans', '9', 'bold'))
        self.label.grid(column=6, row=1)
        self.radius_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.radius_np.grid(column=7, row=1)
        self.radius_np.insert(tk.END, "0")

        self.label = tk.Label(master=self.frame_new_planet, text='Radius \u03C3- P:', fg="blue",
                              font=('Sans', '9', 'bold'))
        self.label.grid(column=8, row=1)
        self.radius_sn_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.radius_sn_np.grid(column=9, row=1)
        self.radius_sn_np.insert(tk.END, "0")

        self.label = tk.Label(master=self.frame_new_planet, text='Radius \u03C3+ P:', fg="blue",
                              font=('Sans', '9', 'bold'))
        self.label.grid(column=0, row=2)
        self.radius_sp_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.radius_sp_np.grid(column=1, row=2)
        self.radius_sp_np.insert(tk.END, "0")

        self.label = tk.Label(master=self.frame_new_planet, text='Age:', fg="blue", font=('Sans', '9', 'bold'))
        self.label.grid(column=2, row=2)
        self.age_host_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.age_host_np.grid(column=3, row=2)
        self.age_host_np.insert(tk.END, "0")
        if not check_age_host:
            self.age_host_np.configure(state="disable")

        self.label = tk.Label(master=self.frame_new_planet, text='T Star:', fg="blue", font=('Sans', '9', 'bold'))
        self.label.grid(column=4, row=2)
        self.tstar_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.tstar_np.grid(column=5, row=2)
        self.tstar_np.insert(tk.END, "0")
        if not check_tstar:
            self.tstar_np.configure(state="disable")

        self.label = tk.Label(master=self.frame_new_planet, text='M Star:', fg="blue", font=('Sans', '9', 'bold'))
        self.label.grid(column=6, row=2)
        self.mstar_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.mstar_np.grid(column=7, row=2)
        self.mstar_np.insert(tk.END, "0")
        if not check_mass_star:
            self.mstar_np.configure(state="disable")

        self.label = tk.Label(master=self.frame_new_planet, text='R Star:', fg="blue", font=('Sans', '9', 'bold'))
        self.label.grid(column=8, row=2)
        self.rstar_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.rstar_np.grid(column=9, row=2)
        self.rstar_np.insert(tk.END, "0")
        if not check_radius_star:
            self.rstar_np.configure(state="disable")

        self.label = tk.Label(master=self.frame_new_planet, text='P orb:', fg="blue", font=('Sans', '9', 'bold'))
        self.label.grid(column=0, row=3)
        self.p_orb_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.p_orb_np.grid(column=1, row=3)
        self.p_orb_np.insert(tk.END, "0")
        if not check_p_orb:
            self.p_orb_np.configure(state="disable")

        self.label = tk.Label(master=self.frame_new_planet, text='a orb:', fg="blue", font=('Sans', '9', 'bold'))
        self.label.grid(column=2, row=3)
        self.a_orb_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.a_orb_np.grid(column=3, row=3)
        self.a_orb_np.insert(tk.END, "0")
        if not check_a_orb:
            self.a_orb_np.configure(state="disable")

        self.label = tk.Label(master=self.frame_new_planet, text='[Fe/H]:', fg="blue", font=('Sans', '9', 'bold'))
        self.label.grid(column=4, row=3)
        self.fe_h_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.fe_h_np.grid(column=5, row=3)
        self.fe_h_np.insert(tk.END, "0")
        if not check_FeH:
            self.fe_h_np.configure(state="disable")

        self.label = tk.Label(master=self.frame_new_planet, text='Temp P:', fg="blue", font=('Sans', '9', 'bold'))
        self.label.grid(column=6, row=3)
        self.tplanet_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.tplanet_np.grid(column=7, row=3)
        self.tplanet_np.insert(tk.END, "0")
        if not check_teq:
            self.tplanet_np.configure(state="disable")

        self.label = tk.Label(master=self.frame_new_planet, text='Ecc:', fg="blue", font=('Sans', '9', 'bold'))
        self.label.grid(column=8, row=3)
        self.ecc_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.ecc_np.grid(column=9, row=3)
        self.ecc_np.insert(tk.END, "0")
        if not check_ecc:
            self.ecc_np.configure(state="disable")

        self.label = tk.Label(master=self.frame_new_planet, text='Name:', fg="blue", font=('Sans', '9', 'bold'))
        self.label.grid(column=0, row=4)
        self.name_np = tk.Entry(master=self.frame_new_planet, width=10)
        self.name_np.grid(column=1, row=4)
        self.name_np.insert(tk.END, "Name")

        self.add_planet_btn = tk.Button(master=self.frame_new_planet, text="Add Planet to list", command=self.addPlanet, bg="#00ff00", font=('Sans', '9', 'bold'))
        self.add_planet_btn.grid(column=2, row=4, columnspan=3)

        options_list = [""]
        self.list_planet_var = tk.StringVar()
        self.list_planet = tk.OptionMenu(self.frame_new_planet, self.list_planet_var, *options_list)
        self.list_planet.grid(column=5, row=4)
        self.list_planet_var = ""

        self.delete_planet_btn = tk.Button(master=self.frame_new_planet, text="Delete Planet from list", command=self.deletePlanet, bg="red", font=('Sans', '9', 'bold'))
        self.delete_planet_btn.grid(column=6, row=4, columnspan=3)

        self.input_list = pd.DataFrame()

        # self.label_input = tk.Label(master=self.frame_new_planet, text='Input example: [\"planet-name\", Mass, \u03C3m+, \u03C3m-, Radius, \u03C3r+, \u03C3r-, T_eq(K), Age]%[...]', fg="blue", font=('Sans', '9', 'bold'))
        # self.label_input.grid(column=0, row=1, columnspan=3)
        # self.text_input = tk.Text(master=self.frame_new_planet, height=7)
        # self.text_input.grid(column=0, row=2, columnspan=3)
        # self.text_input.insert(tk.END, "[\"TOI-1710 b\", 29, 5, 5, 5.3, 0.1, 0.1, 700, 0.14]")
        self.frame_new_planet.pack(padx=3, pady=3)

    def deletePlanet(self):
        self.input_list[self.name_np.get()] = {"Name": self.name_np.get()}

    def addPlanet(self):
        print("ciao")
