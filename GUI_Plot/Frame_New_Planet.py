import tkinter as tk
from tkinter import messagebox as msgbox

import pandas as pd


def helpButtonFunc():
    msgbox.showinfo(title="INFO", message="Plot options: \nSingle/new planets can be included and highlighted in the mass-radius diagram. \nThe 'Add Planet to the list' button will allow the user to build a list of planets to be included in the mass-radius diagram. \nThe list of added planets will appear in the drop down menu on the right. \nBy pushing the 'Delete Planet to the list' will remove the planet appearing in the drop down menu from the list of planets to be plotted. \nThe user can select the option 'filter new planet(s)' to plot the newly added planets on the diagram only if all the planet and star parameters are within the ranges initially defined. \nBy deselecting this option, the newly added planet is included in the plot regardless of the user-defined constraints on the parameters.\nNB: the measurement units used for Masses and Radius are the same selected during the catalog import process.\n1 MJup = 317.8 M⊕\n1 RJup = 11.2 R⊕")


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
    list_planet_om = None
    name_np = None
    input_list = None
    check_ecc = None
    check_FeH = None
    check_tstar = None
    check_p_orb = None
    check_a_orb = None
    check_teq = None
    check_mass_star = None
    check_radius_star = None
    check_age_host = None
    options_list = None
    help_button = None
    name_from_duplicate = None

    def __init__(self, window, gui, mass_coeff, radius_coeff, age_coeff, check_age_host, check_ecc, check_FeH, check_tstar, check_p_orb, check_a_orb, check_teq, check_mass_star, check_radius_star):
        self.gui = gui
        self.name_from_duplicate = False
        self.check_age_host = check_age_host
        self.check_ecc = check_ecc
        self.check_FeH = check_FeH
        self.check_tstar = check_tstar
        self.check_p_orb = check_p_orb
        self.check_a_orb = check_a_orb
        self.check_teq = check_teq
        self.check_mass_star = check_mass_star
        self.check_radius_star = check_radius_star
        self.frame_new_planet = tk.Frame(window, highlightbackground="black", highlightthickness=1, padx=5, pady=2)
        self.add_new_planet_check_var = tk.IntVar()
        self.add_new_planet_check = tk.Checkbutton(master=self.frame_new_planet, text="Add new planet(s)?", variable=self.add_new_planet_check_var, fg="#cc3300", font=('Sans', '9', 'bold'))
        self.add_new_planet_check.grid(column=0, row=0, columnspan=3)
        self.filter_new_planet_check_var = tk.IntVar()
        self.filter_new_planet_check = tk.Checkbutton(master=self.frame_new_planet, text="Filter new planet(s)?", variable=self.filter_new_planet_check_var, fg="#cc3300", font=('Sans', '9', 'bold'))
        self.filter_new_planet_check.grid(column=3, row=0, columnspan=3)
        self.label_new_planet_check_var = tk.IntVar()
        self.label_new_planet_check = tk.Checkbutton(master=self.frame_new_planet, text="Show label(s)?", variable=self.label_new_planet_check_var, fg="#cc3300", font=('Sans', '9', 'bold'))
        self.label_new_planet_check.grid(column=6, row=0, columnspan=3)

        self.help_button = tk.Button(master=self.frame_new_planet, text="?", command=helpButtonFunc, bg="black", fg="yellow", font=('Sans', '10', 'bold'))
        self.help_button.grid(column=9, row=0)

        if mass_coeff == 1:
            mass = "⊕"
        else:
            mass = "Jup"

        self.label = tk.Label(master=self.frame_new_planet, text='M Pl [' + mass + ']:', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(column=0, row=1)
        self.mass_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.mass_np.grid(column=1, row=1)
        self.mass_np.insert(tk.END, str(round(7.72 / mass_coeff, 3)))

        self.label = tk.Label(master=self.frame_new_planet, text='M \u03C3- Pl [' + mass + ']:', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(column=2, row=1)
        self.mass_sn_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.mass_sn_np.grid(column=3, row=1)
        self.mass_sn_np.insert(tk.END, str(round(0.38 / mass_coeff, 3)))

        self.label = tk.Label(master=self.frame_new_planet, text='M \u03C3+ Pl [' + mass + ']:', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(column=4, row=1)
        self.mass_sp_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.mass_sp_np.grid(column=5, row=1)
        self.mass_sp_np.insert(tk.END, str(round(0.286 / mass_coeff, 3)))

        if radius_coeff == 1:
            rad = "⊕"
        else:
            rad = "Jup"

        self.label = tk.Label(master=self.frame_new_planet, text='R Pl [' + rad + ']:', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(column=6, row=1)
        self.radius_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.radius_np.grid(column=7, row=1)
        self.radius_np.insert(tk.END, str(round(1.89 / radius_coeff, 3)))

        self.label = tk.Label(master=self.frame_new_planet, text='R \u03C3- Pl [' + rad + ']:', fg="blue",
                              font=('Sans', '8', 'bold'))
        self.label.grid(column=8, row=1)
        self.radius_sn_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.radius_sn_np.grid(column=9, row=1)
        self.radius_sn_np.insert(tk.END, str(round(0.0437 / radius_coeff, 3)))

        self.label = tk.Label(master=self.frame_new_planet, text='R \u03C3+ Pl [' + rad + ']:', fg="blue",
                              font=('Sans', '8', 'bold'))
        self.label.grid(column=0, row=2)
        self.radius_sp_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.radius_sp_np.grid(column=1, row=2)
        self.radius_sp_np.insert(tk.END, str(round(0.00459 / radius_coeff, 3)))

        if age_coeff == 1000:
            age = "Myr"
        else:
            age = "Gyr"
        self.label = tk.Label(master=self.frame_new_planet, text='Age [' + age + ']:', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(column=2, row=2)
        self.age_host_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.age_host_np.grid(column=3, row=2)
        self.age_host_np.insert(tk.END, "0")
        if not check_age_host:
            self.age_host_np.configure(state="disable")

        self.label = tk.Label(master=self.frame_new_planet, text='T Star [K]:', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(column=4, row=2)
        self.tstar_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.tstar_np.grid(column=5, row=2)
        self.tstar_np.insert(tk.END, "5172")
        if not check_tstar:
            self.tstar_np.configure(state="disable")

        self.label = tk.Label(master=self.frame_new_planet, text='M Star [☉]:', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(column=6, row=2)
        self.mstar_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.mstar_np.grid(column=7, row=2)
        self.mstar_np.insert(tk.END, "0.873")
        if not check_mass_star:
            self.mstar_np.configure(state="disable")

        self.label = tk.Label(master=self.frame_new_planet, text='R Star [☉]:', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(column=8, row=2)
        self.rstar_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.rstar_np.grid(column=9, row=2)
        self.rstar_np.insert(tk.END, "0.954")
        if not check_radius_star:
            self.rstar_np.configure(state="disable")

        self.label = tk.Label(master=self.frame_new_planet, text='P orb [days]:', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(column=0, row=3)
        self.p_orb_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.p_orb_np.grid(column=1, row=3)
        self.p_orb_np.insert(tk.END, "0.737")
        if not check_p_orb:
            self.p_orb_np.configure(state="disable")

        self.label = tk.Label(master=self.frame_new_planet, text='a orb [AU]:', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(column=2, row=3)
        self.a_orb_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.a_orb_np.grid(column=3, row=3)
        self.a_orb_np.insert(tk.END, "0.0154")
        if not check_a_orb:
            self.a_orb_np.configure(state="disable")

        self.label = tk.Label(master=self.frame_new_planet, text='[Fe/H]:', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(column=4, row=3)
        self.fe_h_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.fe_h_np.grid(column=5, row=3)
        self.fe_h_np.insert(tk.END, "0.35")
        if not check_FeH:
            self.fe_h_np.configure(state="disable")

        self.label = tk.Label(master=self.frame_new_planet, text='T Pl [K]:', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(column=6, row=3)
        self.tplanet_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.tplanet_np.grid(column=7, row=3)
        self.tplanet_np.insert(tk.END, "2349")
        if not check_teq:
            self.tplanet_np.configure(state="disable")

        self.label = tk.Label(master=self.frame_new_planet, text='Ecc:', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(column=8, row=3)
        self.ecc_np = tk.Entry(master=self.frame_new_planet, width=6)
        self.ecc_np.grid(column=9, row=3)
        self.ecc_np.insert(tk.END, "0.05")
        if not check_ecc:
            self.ecc_np.configure(state="disable")

        self.label = tk.Label(master=self.frame_new_planet, text='Name:', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(column=0, row=4)
        self.name_np = tk.Entry(master=self.frame_new_planet, width=10)
        self.name_np.grid(column=1, row=4)
        self.name_np.insert(tk.END, "55_Cnc_e")

        self.add_planet_btn = tk.Button(master=self.frame_new_planet, text="Add Planet to list", command=self.addPlanet, bg="#00ff00", font=('Sans', '9', 'bold'))
        self.add_planet_btn.grid(column=2, row=4, columnspan=3)

        self.options_list = ["None"]
        self.list_planet_var = tk.StringVar(value="None")
        self.list_planet_var.trace('w', lambda *args: self.update_planets_info())
        self.list_planet_om = tk.OptionMenu(self.frame_new_planet, self.list_planet_var, "None")
        self.list_planet_om.grid(column=5, row=4, columnspan=2)

        self.delete_planet_btn = tk.Button(master=self.frame_new_planet, text="Delete Planet from list", command=self.deletePlanet, bg="red", font=('Sans', '9', 'bold'))
        self.delete_planet_btn.grid(column=7, row=4, columnspan=3)

        self.input_list = pd.DataFrame()
        self.frame_new_planet.pack(padx=3, pady=3)

    def deletePlanet(self):
        if self.name_from_duplicate:
            name = self.name_np.get()
        else:
            name = self.list_planet_var.get()
        if self.list_planet_var.get() == "None":
            return
        self.input_list = self.input_list[self.input_list.Name != name]
        self.options_list = [value for value in self.options_list if value != name]
        self.update_menu()

    def addPlanet(self):
        if self.name_np.get() == "None":
            msgbox.showerror(title="None is not a valid name", message="None")
            return
        if self.name_np.get() in self.options_list:
            risp = msgbox.askyesno(title="Update Values", message="The planet is already present in the list. Do you want to update it with the current values?")
            if risp:
                self.name_from_duplicate = True
                self.deletePlanet()
                self.name_from_duplicate = False
            else:
                return
        new_row = {"Name": self.name_np.get(), "Mass_p": float(self.mass_np.get()), "Mass_sn_p": float(self.mass_sn_np.get()),
                   "Mass_sp_p": float(self.mass_sp_np.get()), "Radius_p": float(self.radius_np.get()), "Radius_sn_p": float(self.radius_sn_np.get()),
                   "Radius_sp_p": float(self.radius_sp_np.get())}
        if self.check_age_host:
            new_row["Age"] = float(self.age_host_np.get())
        if self.check_tstar:
            new_row["Tstar"] = float(self.tstar_np.get())
        if self.check_mass_star:
            new_row["Mstar"] = float(self.mstar_np.get())
        if self.check_radius_star:
            new_row["Rstar"] = float(self.rstar_np.get())
        if self.check_p_orb:
            new_row["p_orb"] = float(self.p_orb_np.get())
        if self.check_a_orb:
            new_row["a_orb"] = float(self.a_orb_np.get())
        if self.check_ecc:
            new_row["Ecc"] = float(self.ecc_np.get())
        if self.check_teq:
            new_row["tPlanet"] = float(self.tplanet_np.get())
        if self.check_FeH:
            new_row["[Fe/H]"] = float(self.fe_h_np.get())
        self.input_list = self.input_list.append(new_row, ignore_index=True)
        self.options_list.append(self.name_np.get())
        self.update_menu()

    def update_menu(self):
        menu = self.list_planet_om["menu"]
        menu.delete(0, "end")
        for string in self.options_list:
            menu.add_command(label=string,
                             command=lambda value=string: self.list_planet_var.set(value))

    # noinspection PyArgumentList
    def update_planets_info(self):
        if self.input_list is None:
            return
        if self.list_planet_var.get() == "None":
            return
        elem = self.input_list.loc[self.input_list['Name'] == self.list_planet_var.get()]
        self.name_np.delete(0, tk.END)
        self.name_np.insert(tk.END, str(elem["Name"].iloc[0]))
        self.mass_np.delete(0, tk.END)
        self.mass_np.insert(tk.END, str(elem["Mass_p"].iloc[0]))
        self.mass_sn_np.delete(0, tk.END)
        self.mass_sn_np.insert(tk.END, str(elem["Mass_sn_p"].iloc[0]))
        self.mass_sp_np.delete(0, tk.END)
        self.mass_sp_np.insert(tk.END, str(elem["Mass_sp_p"].iloc[0]))
        self.radius_np.delete(0, tk.END)
        self.radius_np.insert(tk.END, str(elem["Radius_p"].iloc[0]))
        self.radius_sn_np.delete(0, tk.END)
        self.radius_sn_np.insert(tk.END, str(elem["Radius_sn_p"].iloc[0]))
        self.radius_sp_np.delete(0, tk.END)
        self.radius_sp_np.insert(tk.END, str(elem["Radius_sp_p"].iloc[0]))
        if self.check_age_host:
            self.age_host_np.delete(0, tk.END)
            self.age_host_np.insert(tk.END, str(elem["Age"].iloc[0]))
        if self.check_tstar:
            self.tstar_np.delete(0, tk.END)
            self.tstar_np.insert(tk.END, str(elem["Tstar"].iloc[0]))
        if self.check_mass_star:
            self.mstar_np.delete(0, tk.END)
            self.mstar_np.insert(tk.END, str(elem["Mstar"].iloc[0]))
        if self.check_radius_star:
            self.rstar_np.delete(0, tk.END)
            self.rstar_np.insert(tk.END, str(elem["Rstar"].iloc[0]))
        if self.check_p_orb:
            self.p_orb_np.delete(0, tk.END)
            self.p_orb_np.insert(tk.END, str(elem["p_orb"].iloc[0]))
        if self.check_a_orb:
            self.a_orb_np.delete(0, tk.END)
            self.a_orb_np.insert(tk.END, str(elem["a_orb"].iloc[0]))
        if self.check_ecc:
            self.ecc_np.delete(0, tk.END)
            self.ecc_np.insert(tk.END, str(elem["Ecc"].iloc[0]))
        if self.check_teq:
            self.tplanet_np.delete(0, tk.END)
            self.tplanet_np.insert(tk.END, str(elem["tPlanet"].iloc[0]))
        if self.check_FeH:
            self.fe_h_np.delete(0, tk.END)
            self.fe_h_np.insert(tk.END, str(elem["[Fe/H]"].iloc[0]))
