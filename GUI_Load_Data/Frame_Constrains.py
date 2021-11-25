import os
import tkinter as tk
from tkinter.filedialog import askopenfilename

import pandas as pd
import GUI_Plot.Gui


def deleteRow(data, index):
    data0 = (data.drop(index, axis=1).join(data[index].apply(pd.to_numeric, errors='coerce')))
    data0 = data0[data0[index].notnull()]
    return data0


class Frame_Constrains:
    gui = None
    frame_constrains = None
    label = None
    t_eff_star_check = None
    t_eff_star_check_var = None
    t_eff_star_entry = None
    Fe_H_check = None
    Fe_H_check_var = None
    Fe_H_entry = None
    M_star_check = None
    M_star_check_var = None
    M_star_entry = None
    R_star_check = None
    R_star_check_var = None
    R_star_entry = None
    P_orb_planet_check = None
    P_orb_planet_check_var = None
    P_orb_planet_entry = None
    semi_major_axes_planet_check = None
    semi_major_axes_planet_check_var = None
    semi_major_axes_planet_entry = None
    eccentricity_planet_check = None
    eccentricity_planet_check_var = None
    eccentricity_planet_entry = None
    T_eq_planet_check = None
    T_eq_planet_check_var = None
    T_eq_planet_entry = None
    age_host_check = None
    age_host_check_var = None
    age_host_entry = None
    mass_planet_entry = None
    mass_planet_sigma_min_entry = None
    mass_planet_sigma_max_entry = None
    radius_planet_entry = None
    radius_planet_sigma_min_entry = None
    radius_planet_sigma_max_entry = None
    runPlot = None
    conf_entry = None
    load_file = None
    save_file = None

    def __init__(self, window, gui):
        self.gui = gui
        self.frame_constrains = tk.Frame(window, highlightbackground="black", highlightthickness=1, padx=5, pady=2)

        self.label = tk.Label(master=self.frame_constrains,
                              text='Check the constrains that will/can be applied to the dataframe.\nAdd the right column index for each constrains according to your input file.\nPlease, note that the planet\'s mass and radius are mandatory, like their sigma.\nThe software will assume that the planet name is located in the first column.\nNB those constrains are valid for the Tepcat files. \nCI = Column Index',
                              fg="green", font=('Sans', '8', 'bold'))
        self.label.grid(padx=3, column=0, row=0, columnspan=7, rowspan=3)

        self.label = tk.Label(master=self.frame_constrains, text=' Filename ', fg="#66ccff", font=('Sans', '8', 'bold'))
        self.label.grid(padx=3, column=7, row=0)
        self.conf_entry = tk.Entry(master=self.frame_constrains)
        self.conf_entry.grid(padx=3, column=8, row=0)
        self.conf_entry.insert(tk.END, "configuration")

        self.save_file = tk.Button(master=self.frame_constrains, width=20, text=" Save File ", bg="#66ccff", font=('Sans', '8', 'bold'), command=self.saveFileFunc)
        self.save_file.grid(padx=3, column=7, row=1, columnspan=2)

        self.runPlot = tk.Button(master=self.frame_constrains, width=20, text=" Load File ", bg="#cc9900", font=('Sans', '8', 'bold'), command=self.loadFileFunc)
        self.runPlot.grid(padx=3, pady=3, column=7, row=2, columnspan=2)

        self.label = tk.Label(master=self.frame_constrains, text=' Mass Planet CI ', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(padx=3, column=0, row=3)
        self.mass_planet_entry = tk.Entry(master=self.frame_constrains, width=10)
        self.mass_planet_entry.grid(padx=3, column=0, row=4)
        self.mass_planet_entry.insert(tk.END, "26")

        self.label = tk.Label(master=self.frame_constrains, text=' Mass Planet \u03C3 Min CI ', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(padx=3, column=1, row=3, columnspan=2)
        self.mass_planet_sigma_min_entry = tk.Entry(master=self.frame_constrains, width=10)
        self.mass_planet_sigma_min_entry.grid(padx=3, column=1, row=4, columnspan=2)
        self.mass_planet_sigma_min_entry.insert(tk.END, "27")

        self.label = tk.Label(master=self.frame_constrains, text=' Mass Planet \u03C3 Max CI ', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(padx=3, column=3, row=3, columnspan=2)
        self.mass_planet_sigma_max_entry = tk.Entry(master=self.frame_constrains, width=10)
        self.mass_planet_sigma_max_entry.grid(padx=3, column=3, row=4, columnspan=2)
        self.mass_planet_sigma_max_entry.insert(tk.END, "28")

        self.label = tk.Label(master=self.frame_constrains, text=' Radius Planet CI ', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(padx=3, column=5, row=3)
        self.radius_planet_entry = tk.Entry(master=self.frame_constrains, width=10)
        self.radius_planet_entry.grid(padx=3, column=5, row=4)
        self.radius_planet_entry.insert(tk.END, "29")

        self.label = tk.Label(master=self.frame_constrains, text=' Radius Planet \u03C3 Min CI ', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(padx=3, column=6, row=3, columnspan=2)
        self.radius_planet_sigma_min_entry = tk.Entry(master=self.frame_constrains, width=10)
        self.radius_planet_sigma_min_entry.grid(padx=3, column=6, row=4, columnspan=2)
        self.radius_planet_sigma_min_entry.insert(tk.END, "30")

        self.label = tk.Label(master=self.frame_constrains, text=' Radius Planet \u03C3 Max CI ', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(padx=3, column=8, row=3, columnspan=2)
        self.radius_planet_sigma_max_entry = tk.Entry(master=self.frame_constrains, width=10)
        self.radius_planet_sigma_max_entry.grid(padx=3, column=8, row=4, columnspan=2)
        self.radius_planet_sigma_max_entry.insert(tk.END, "31")

        self.label = tk.Label(master=self.frame_constrains,
                              text=' ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ',
                              fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(padx=3, column=0, row=5, columnspan=9)

        self.t_eff_star_check_var = tk.BooleanVar()
        self.t_eff_star_check = tk.Checkbutton(master=self.frame_constrains, text=" T Star [K] ", variable=self.t_eff_star_check_var, fg="#cc3300", font=('Sans', '8', 'bold'))
        self.t_eff_star_check_var.set(True)
        self.t_eff_star_check.grid(padx=3, column=0, row=6)
        self.label = tk.Label(master=self.frame_constrains, text=' CI ', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(padx=3, column=0, row=7)
        self.t_eff_star_entry = tk.Entry(master=self.frame_constrains, width=10)
        self.t_eff_star_entry.grid(padx=3, column=0, row=8)
        self.t_eff_star_entry.insert(tk.END, "1")

        self.Fe_H_check_var = tk.BooleanVar()
        self.Fe_H_check = tk.Checkbutton(master=self.frame_constrains, text=" [Fe/H] ", variable=self.Fe_H_check_var, fg="#cc3300", font=('Sans', '8', 'bold'))
        self.Fe_H_check_var.set(True)
        self.Fe_H_check.grid(padx=3, column=1, row=6)
        self.label = tk.Label(master=self.frame_constrains, text=' CI ', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(padx=3, column=1, row=7)
        self.Fe_H_entry = tk.Entry(master=self.frame_constrains, width=10)
        self.Fe_H_entry.grid(padx=3, column=1, row=8)
        self.Fe_H_entry.insert(tk.END, "4")

        self.M_star_check_var = tk.BooleanVar()
        self.M_star_check = tk.Checkbutton(master=self.frame_constrains, text=" M☉ ", variable=self.M_star_check_var, fg="#cc3300", font=('Sans', '8', 'bold'))
        self.M_star_check_var.set(True)
        self.M_star_check.grid(padx=3, column=2, row=6)
        self.label = tk.Label(master=self.frame_constrains, text=' CI ', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(padx=3, column=2, row=7)
        self.M_star_entry = tk.Entry(master=self.frame_constrains, width=10)
        self.M_star_entry.grid(padx=3, column=2, row=8)
        self.M_star_entry.insert(tk.END, "7")

        self.R_star_check_var = tk.BooleanVar()
        self.R_star_check = tk.Checkbutton(master=self.frame_constrains, text=" R☉ ", variable=self.R_star_check_var, fg="#cc3300", font=('Sans', '8', 'bold'))
        self.R_star_check_var.set(True)
        self.R_star_check.grid(padx=3, column=3, row=6)
        self.label = tk.Label(master=self.frame_constrains, text=' CI ', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(padx=3, column=3, row=7)
        self.R_star_entry = tk.Entry(master=self.frame_constrains, width=10)
        self.R_star_entry.grid(padx=3, column=3, row=8)
        self.R_star_entry.insert(tk.END, "10")

        self.P_orb_planet_check_var = tk.BooleanVar()
        self.P_orb_planet_check = tk.Checkbutton(master=self.frame_constrains, text=" P orb (days) ", variable=self.P_orb_planet_check_var, fg="#cc3300", font=('Sans', '8', 'bold'))
        self.P_orb_planet_check_var.set(True)
        self.P_orb_planet_check.grid(padx=3, column=4, row=6)
        self.label = tk.Label(master=self.frame_constrains, text=' CI ', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(padx=3, column=4, row=7)
        self.P_orb_planet_entry = tk.Entry(master=self.frame_constrains, width=10)
        self.P_orb_planet_entry.grid(padx=3, column=4, row=8)
        self.P_orb_planet_entry.insert(tk.END, "19")

        self.semi_major_axes_planet_check_var = tk.BooleanVar()
        self.semi_major_axes_planet_check = tk.Checkbutton(master=self.frame_constrains, text=" a orb (AU) ", variable=self.semi_major_axes_planet_check_var, fg="#cc3300", font=('Sans', '8', 'bold'))
        self.semi_major_axes_planet_check_var.set(True)
        self.semi_major_axes_planet_check.grid(padx=3, column=5, row=6)
        self.label = tk.Label(master=self.frame_constrains, text=' CI ', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(padx=3, column=5, row=7)
        self.semi_major_axes_planet_entry = tk.Entry(master=self.frame_constrains, width=10)
        self.semi_major_axes_planet_entry.grid(padx=3, column=5, row=8)
        self.semi_major_axes_planet_entry.insert(tk.END, "23")

        self.eccentricity_planet_check_var = tk.BooleanVar()
        self.eccentricity_planet_check = tk.Checkbutton(master=self.frame_constrains, text=" Eccentricity ", variable=self.eccentricity_planet_check_var, fg="#cc3300", font=('Sans', '8', 'bold'))
        self.eccentricity_planet_check_var.set(True)
        self.eccentricity_planet_check.grid(padx=3, column=6, row=6)
        self.label = tk.Label(master=self.frame_constrains, text=' CI ', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(padx=3, column=6, row=7)
        self.eccentricity_planet_entry = tk.Entry(master=self.frame_constrains, width=10)
        self.eccentricity_planet_entry.grid(padx=3, column=6, row=8)
        self.eccentricity_planet_entry.insert(tk.END, "20")

        self.T_eq_planet_check_var = tk.BooleanVar()
        self.T_eq_planet_check = tk.Checkbutton(master=self.frame_constrains, text=" T eq (K) ", variable=self.T_eq_planet_check_var, fg="#cc3300", font=('Sans', '8', 'bold'))
        self.T_eq_planet_check_var.set(True)
        self.T_eq_planet_check.grid(padx=3, column=7, row=6)
        self.label = tk.Label(master=self.frame_constrains, text=' CI ', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(padx=3, column=7, row=7)
        self.T_eq_planet_entry = tk.Entry(master=self.frame_constrains, width=10)
        self.T_eq_planet_entry.grid(padx=3, column=7, row=8)
        self.T_eq_planet_entry.insert(tk.END, "38")

        self.age_host_check_var = tk.BooleanVar()
        self.age_host_check = tk.Checkbutton(master=self.frame_constrains, text=" Age Host (Gyr) ", variable=self.age_host_check_var, fg="#cc3300", font=('Sans', '8', 'bold'))
        self.age_host_check_var.set(False)
        self.age_host_check.grid(padx=3, column=8, row=6)
        self.label = tk.Label(master=self.frame_constrains, text=' CI ', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(padx=3, column=8, row=7)
        self.age_host_entry = tk.Entry(master=self.frame_constrains, width=10)
        self.age_host_entry.grid(padx=3, column=8, row=8)
        self.age_host_entry.insert(tk.END, "1")

        self.label = tk.Label(master=self.frame_constrains,
                              text=' ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ',
                              fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(padx=3, column=0, row=9, columnspan=9)

        words_mass = ["Earth Mass", "Jupiter Mass"]
        self.label = tk.Label(master=self.frame_constrains, text=' Mass expressed in:  ', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(padx=3, column=2, row=10, columnspan=2)
        self.mass_expressed_var = tk.StringVar()
        self.mass_expressed = tk.OptionMenu(self.frame_constrains, self.mass_expressed_var, *words_mass)
        self.mass_expressed.grid(padx=3, column=4, row=10)
        self.mass_expressed_var.set("Jupiter Mass")

        words_radius = ["Earth Radius", "Jupiter Radius"]
        self.label = tk.Label(master=self.frame_constrains, text=' Radius expressed in:  ', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(padx=3, column=5, row=10, columnspan=2)
        self.radius_expressed_var = tk.StringVar()
        self.radius_expressed = tk.OptionMenu(self.frame_constrains, self.radius_expressed_var, *words_radius)
        self.radius_expressed.grid(padx=3, column=7, row=10)
        self.radius_expressed_var.set("Jupiter Radius")

        self.runPlot = tk.Button(master=self.frame_constrains, width=50, height=2, text=" Run Algorithm ", bg="#00ff00", font=('Sans', '15', 'bold'), command=self.RunGuiPlot)
        self.runPlot.grid(padx=3, pady=3, column=0, row=11, columnspan=9)

        self.frame_constrains.pack(padx=3, pady=3)
        for child in self.frame_constrains.winfo_children():
            child.configure(state='disable')

    def RunGuiPlot(self):
        index_ecc = int(self.eccentricity_planet_entry.get())
        index_FeH = int(self.Fe_H_entry.get())
        index_tstar = int(self.t_eff_star_entry.get())
        index_p_orb = int(self.P_orb_planet_entry.get())
        index_a_orb = int(self.semi_major_axes_planet_entry.get())
        index_teq = int(self.T_eq_planet_entry.get())
        index_mass_star = int(self.M_star_entry.get())
        index_radius_star = int(self.R_star_entry.get())
        index_rad_p = int(self.radius_planet_entry.get())
        index_rad_max = int(self.radius_planet_sigma_max_entry.get())
        index_min_rad = int(self.radius_planet_sigma_min_entry.get())
        index_mass_p = int(self.mass_planet_entry.get())
        index_mass_min = int(self.mass_planet_sigma_min_entry.get())
        index_mass_max = int(self.mass_planet_sigma_max_entry.get())
        index_age_host = int(self.age_host_entry.get())
        check_ecc = self.eccentricity_planet_check_var.get()
        check_FeH = self.Fe_H_check_var.get()
        check_tstar = self.t_eff_star_check_var.get()
        check_p_orb = self.P_orb_planet_check_var.get()
        check_a_orb = self.semi_major_axes_planet_check_var.get()
        check_teq = self.T_eq_planet_check_var.get()
        check_mass_star = self.M_star_check_var.get()
        check_radius_star = self.R_star_check_var.get()
        check_age_host = self.age_host_check_var.get()
        data0 = self.gui.frame_load_data.data0
        data0 = deleteRow(data0, index_mass_p)
        data0 = deleteRow(data0, index_mass_min)
        data0 = deleteRow(data0, index_mass_max)
        data0 = deleteRow(data0, index_rad_p)
        data0 = deleteRow(data0, index_min_rad)
        data0 = deleteRow(data0, index_rad_max)
        if check_a_orb:
            data0 = deleteRow(data0, index_a_orb)
        if check_ecc:
            data0 = deleteRow(data0, index_ecc)
        if check_p_orb:
            data0 = deleteRow(data0, index_p_orb)
        if check_age_host:
            data0 = deleteRow(data0, index_age_host)
        if check_tstar:
            data0 = deleteRow(data0, index_tstar)
        if check_mass_star:
            data0 = deleteRow(data0, index_mass_star)
        if check_radius_star:
            data0 = deleteRow(data0, index_radius_star)
        if check_teq:
            data0 = deleteRow(data0, index_teq)
        if check_FeH:
            data0 = deleteRow(data0, index_FeH)
        if self.mass_expressed_var.get() == "Jupiter Mass":
            mass_coeff = 317.8
        else:
            mass_coeff = 1
        if self.radius_expressed_var.get() == "Jupiter Radius":
            radius_coeff = 11.2
        else:
            radius_coeff = 1
        self.gui.window.destroy()
        gui = GUI_Plot.Gui.GUI_Planet(data0, mass_coeff, radius_coeff, index_ecc, index_FeH, index_tstar, index_mass_max, index_p_orb, index_a_orb, index_teq, index_mass_min, index_min_rad,
                                      index_mass_star, index_radius_star, index_rad_max, index_rad_p, index_mass_p, index_age_host, check_age_host, check_ecc, check_FeH, check_tstar, check_p_orb,
                                      check_a_orb, check_teq, check_mass_star, check_radius_star)
        gui.window.mainloop()

    def saveFileFunc(self):
        index_ecc = int(self.eccentricity_planet_entry.get())
        index_FeH = int(self.Fe_H_entry.get())
        index_tstar = int(self.t_eff_star_entry.get())
        index_p_orb = int(self.P_orb_planet_entry.get())
        index_a_orb = int(self.semi_major_axes_planet_entry.get())
        index_teq = int(self.T_eq_planet_entry.get())
        index_mass_star = int(self.M_star_entry.get())
        index_radius_star = int(self.R_star_entry.get())
        index_rad_p = int(self.radius_planet_entry.get())
        index_rad_max = int(self.radius_planet_sigma_max_entry.get())
        index_min_rad = int(self.radius_planet_sigma_min_entry.get())
        index_mass_p = int(self.mass_planet_entry.get())
        index_mass_min = int(self.mass_planet_sigma_min_entry.get())
        index_mass_max = int(self.mass_planet_sigma_max_entry.get())
        index_age_host = int(self.age_host_entry.get())
        check_ecc = self.eccentricity_planet_check_var.get()
        check_FeH = self.Fe_H_check_var.get()
        check_tstar = self.t_eff_star_check_var.get()
        check_p_orb = self.P_orb_planet_check_var.get()
        check_a_orb = self.semi_major_axes_planet_check_var.get()
        check_teq = self.T_eq_planet_check_var.get()
        check_mass_star = self.M_star_check_var.get()
        check_radius_star = self.R_star_check_var.get()
        check_age_host = self.age_host_check_var.get()
        mass_expr = self.mass_expressed_var.get()
        radius_expr = self.radius_expressed_var.get()
        df = pd.DataFrame({"Index": [str(index_mass_p), str(index_mass_min), str(index_mass_max), str(index_rad_p), str(index_min_rad), str(index_rad_max), str(index_tstar), str(index_FeH), str(index_mass_star), str(index_radius_star), str(index_p_orb),
                                     str(index_a_orb), str(index_ecc), str(index_teq), str(index_age_host), mass_expr],
                           "Check": ["True", "True", "True", "True", "True", "True", str(check_tstar), str(check_FeH), str(check_mass_star), str(check_radius_star), str(check_p_orb), str(check_a_orb), str(check_ecc), str(check_teq), str(check_age_host), radius_expr]})
        df.to_csv("Configuration" + os.sep + self.conf_entry.get() + ".csv")

    def loadFileFunc(self):
        filename = askopenfilename(initialdir="Configuration")
        df = pd.read_csv(filename)
        self.mass_planet_entry.delete('0', tk.END)
        self.mass_planet_entry.insert(tk.END, str(df.iloc[0]['Index']))
        self.mass_planet_sigma_min_entry.delete('0', tk.END)
        self.mass_planet_sigma_min_entry.insert(tk.END, str(df.iloc[1]['Index']))
        self.mass_planet_sigma_max_entry.delete('0', tk.END)
        self.mass_planet_sigma_max_entry.insert(tk.END, str(df.iloc[2]['Index']))
        self.radius_planet_entry.delete('0', tk.END)
        self.radius_planet_entry.insert(tk.END, str(df.iloc[3]['Index']))
        self.radius_planet_sigma_min_entry.delete('0', tk.END)
        self.radius_planet_sigma_min_entry.insert(tk.END, str(df.iloc[4]['Index']))
        self.radius_planet_sigma_max_entry.delete('0', tk.END)
        self.radius_planet_sigma_max_entry.insert(tk.END, str(df.iloc[5]['Index']))
        self.t_eff_star_entry.delete('0', tk.END)
        self.t_eff_star_entry.insert(tk.END, str(df.iloc[6]['Index']))
        self.Fe_H_entry.delete('0', tk.END)
        self.Fe_H_entry.insert(tk.END, str(df.iloc[7]['Index']))
        self.M_star_entry.delete('0', tk.END)
        self.M_star_entry.insert(tk.END, str(df.iloc[8]['Index']))
        self.R_star_entry.delete('0', tk.END)
        self.R_star_entry.insert(tk.END, str(df.iloc[9]['Index']))
        self.P_orb_planet_entry.delete('0', tk.END)
        self.P_orb_planet_entry.insert(tk.END, str(df.iloc[10]['Index']))
        self.semi_major_axes_planet_entry.delete('0', tk.END)
        self.semi_major_axes_planet_entry.insert(tk.END, str(df.iloc[11]['Index']))
        self.eccentricity_planet_entry.delete('0', tk.END)
        self.eccentricity_planet_entry.insert(tk.END, str(df.iloc[12]['Index']))
        self.T_eq_planet_entry.delete('0', tk.END)
        self.T_eq_planet_entry.insert(tk.END, str(df.iloc[13]['Index']))
        self.age_host_entry.delete('0', tk.END)
        self.age_host_entry.insert(tk.END, str(df.iloc[14]['Index']))
        self.mass_expressed_var.set(str(df.iloc[15]['Index']))
        self.t_eff_star_check_var.set(str(df.iloc[6]['Check']))
        self.Fe_H_check_var.set(str(df.iloc[7]['Check']))
        self.M_star_check_var.set(str(df.iloc[8]['Check']))
        self.R_star_check_var.set(str(df.iloc[9]['Check']))
        self.P_orb_planet_check_var.set(str(df.iloc[10]['Check']))
        self.semi_major_axes_planet_check_var.set(str(df.iloc[11]['Check']))
        self.eccentricity_planet_check_var.set(str(df.iloc[12]['Check']))
        self.T_eq_planet_check_var.set(str(df.iloc[13]['Check']))
        self.age_host_check_var.set(str(df.iloc[14]['Check']))
        self.radius_expressed_var.set(str(df.iloc[15]['Check']))
