import tkinter as tk
from tkinter import messagebox as msgbox


def helpButtonFunc():
    msgbox.showinfo(title="INFO",
                    message="Plot and statistical options: \nInsert the range for each selected parameter. Any of this parameter can be used as the third variable in the 3D colormap plot.\n\nSelect the “Show planet mass(radius) errors?” if you want the error bars to be displayed in the mass-radius diagram.\n\nSelecting 'filter by systems with multiple planets?' it is possible to plot only multi-planetary systems with a minimum number N of planets as provided by the user.")


class Frame_Input_Planets:
    gui = None
    frame_input_planet = None
    label = None
    limits = None
    age_host_min = None
    age_host_max = None
    t_eff_star_min = None
    t_eff_star_max = None
    Fe_H_min = None
    Fe_H_max = None
    M_star_min = None
    M_star_max = None
    R_star_min = None
    R_star_max = None
    P_orb_planet_min = None
    P_orb_planet_max = None
    semi_major_axes_planet_min = None
    semi_major_axes_planet_max = None
    eccentricity_planet_min = None
    eccentricity_planet_max = None
    T_eq_planet_min = None
    T_eq_planet_max = None
    show_error_check = None
    show_error_plot_var = None
    check_ecc = None
    check_FeH = None
    check_tstar = None
    check_p_orb = None
    check_a_orb = None
    check_teq = None
    check_mass_star = None
    check_radius_star = None
    age_coeff = None
    help_button = None
    show_planets_labels_var = None
    show_planets_labels_check = None
    get_only_planetary_system_var = None
    get_only_planetary_system_check = None
    number_planets_system = None

    def __init__(self, window, gui, age_coeff, check_age_host, check_ecc, check_FeH, check_tstar, check_p_orb,
                 check_a_orb, check_teq, check_mass_star, check_radius_star):
        self.gui = gui
        self.age_coeff = age_coeff
        if age_coeff == 1000:
            age = "Myr"
        else:
            age = "Gyr"
        self.frame_input_planet = tk.Frame(window, highlightbackground="black", highlightthickness=1, padx=5, pady=2)
        self.age_host_min = tk.Entry(master=self.frame_input_planet, width=10)
        self.age_host_min.grid(column=0, row=0)
        self.age_host_min.insert(tk.END, "0")
        self.label = tk.Label(master=self.frame_input_planet, text=' <= Age [' + age + ']<= ', fg="blue",
                              font=('Sans', '9', 'bold'))
        self.label.grid(column=1, row=0)
        self.age_host_max = tk.Entry(master=self.frame_input_planet, width=10)
        self.age_host_max.grid(column=2, row=0)
        self.age_host_max.insert(tk.END, str(14 * self.age_coeff))
        if not check_age_host:
            self.age_host_min.configure(state="disable")
            self.age_host_max.configure(state="disable")
        self.limits = tk.Label(master=self.frame_input_planet, text='i.e. {0, ' + str(14 * self.age_coeff) + '}',
                               fg="red", font=('Sans', '9', 'bold'))
        self.limits.grid(column=3, row=0)
        self.help_button = tk.Button(master=self.frame_input_planet, text="?", command=helpButtonFunc, bg="black",
                                     fg="yellow", font=('Sans', '10', 'bold'))
        self.help_button.grid(column=5, row=0)
        self.t_eff_star_min = tk.Entry(master=self.frame_input_planet, width=10)
        self.t_eff_star_min.grid(column=0, row=1)
        self.t_eff_star_min.insert(tk.END, "2500")
        self.label = tk.Label(master=self.frame_input_planet, text=' <= T Star [K] <= ', fg="blue",
                              font=('Sans', '9', 'bold'))
        self.label.grid(column=1, row=1)
        self.t_eff_star_max = tk.Entry(master=self.frame_input_planet, width=10)
        self.t_eff_star_max.grid(column=2, row=1)
        self.t_eff_star_max.insert(tk.END, "10000")
        if not check_tstar:
            self.t_eff_star_min.configure(state="disable")
            self.t_eff_star_max.configure(state="disable")
        self.limits = tk.Label(master=self.frame_input_planet, text='i.e. {2500, 10000}', fg="red",
                               font=('Sans', '9', 'bold'))
        self.limits.grid(column=3, row=1)
        self.Fe_H_min = tk.Entry(master=self.frame_input_planet, width=10)
        self.Fe_H_min.grid(column=0, row=2)
        self.Fe_H_min.insert(tk.END, "-0.5")
        self.label = tk.Label(master=self.frame_input_planet, text=' <= [Fe/H] <= ', fg="blue",
                              font=('Sans', '9', 'bold'))
        self.label.grid(column=1, row=2)
        self.Fe_H_max = tk.Entry(master=self.frame_input_planet, width=10)
        self.Fe_H_max.grid(column=2, row=2)
        self.Fe_H_max.insert(tk.END, "0.5")
        if not check_FeH:
            self.Fe_H_min.configure(state="disable")
            self.Fe_H_max.configure(state="disable")
        self.limits = tk.Label(master=self.frame_input_planet, text='i.e. {-0.5, 0.5}', fg="red",
                               font=('Sans', '9', 'bold'))
        self.limits.grid(column=3, row=2)
        self.M_star_min = tk.Entry(master=self.frame_input_planet, width=10)
        self.M_star_min.grid(column=0, row=3)
        self.M_star_min.insert(tk.END, "0")
        self.label = tk.Label(master=self.frame_input_planet, text=' <= M☉ <= ', fg="blue", font=('Sans', '9', 'bold'))
        self.label.grid(column=1, row=3)
        self.M_star_max = tk.Entry(master=self.frame_input_planet, width=10)
        self.M_star_max.grid(column=2, row=3)
        self.M_star_max.insert(tk.END, "2")
        if not check_mass_star:
            self.M_star_max.configure(state="disable")
            self.M_star_min.configure(state="disable")
        self.limits = tk.Label(master=self.frame_input_planet, text='i.e. {0., 2.}', fg="red",
                               font=('Sans', '9', 'bold'))
        self.limits.grid(column=3, row=3)
        self.R_star_min = tk.Entry(master=self.frame_input_planet, width=10)
        self.R_star_min.grid(column=0, row=4)
        self.R_star_min.insert(tk.END, "0")
        self.label = tk.Label(master=self.frame_input_planet, text=' <= R☉ <= ', fg="blue", font=('Sans', '9', 'bold'))
        self.label.grid(column=1, row=4)
        self.R_star_max = tk.Entry(master=self.frame_input_planet, width=10)
        self.R_star_max.grid(column=2, row=4)
        self.R_star_max.insert(tk.END, "2")
        if not check_radius_star:
            self.R_star_min.configure(state="disable")
            self.R_star_max.configure(state="disable")
        self.limits = tk.Label(master=self.frame_input_planet, text='i.e. {0., 2.}', fg="red",
                               font=('Sans', '9', 'bold'))
        self.limits.grid(column=3, row=4)
        self.P_orb_planet_min = tk.Entry(master=self.frame_input_planet, width=10)
        self.P_orb_planet_min.grid(column=0, row=5)
        self.P_orb_planet_min.insert(tk.END, "0.1")
        self.label = tk.Label(master=self.frame_input_planet, text=' <= P orb [days] <= ', fg="blue",
                              font=('Sans', '9', 'bold'))
        self.label.grid(column=1, row=5)
        self.P_orb_planet_max = tk.Entry(master=self.frame_input_planet, width=10)
        self.P_orb_planet_max.grid(column=2, row=5)
        self.P_orb_planet_max.insert(tk.END, "100")
        if not check_p_orb:
            self.P_orb_planet_min.configure(state="disable")
            self.P_orb_planet_max.configure(state="disable")
        self.limits = tk.Label(master=self.frame_input_planet, text='i.e. {0.1, 100.}', fg="red",
                               font=('Sans', '9', 'bold'))
        self.limits.grid(column=3, row=5)
        self.semi_major_axes_planet_min = tk.Entry(master=self.frame_input_planet, width=10)
        self.semi_major_axes_planet_min.grid(column=0, row=6)
        self.semi_major_axes_planet_min.insert(tk.END, "0.01")
        self.label = tk.Label(master=self.frame_input_planet, text=' <= a orb [AU] <= ', fg="blue",
                              font=('Sans', '9', 'bold'))
        self.label.grid(column=1, row=6)
        self.semi_major_axes_planet_max = tk.Entry(master=self.frame_input_planet, width=10)
        self.semi_major_axes_planet_max.grid(column=2, row=6)
        self.semi_major_axes_planet_max.insert(tk.END, "0.5")
        if not check_a_orb:
            self.semi_major_axes_planet_min.configure(state="disable")
            self.semi_major_axes_planet_max.configure(state="disable")
        self.limits = tk.Label(master=self.frame_input_planet, text='i.e. {0.01, 0.5}', fg="red",
                               font=('Sans', '9', 'bold'))
        self.limits.grid(column=3, row=6)
        self.eccentricity_planet_min = tk.Entry(master=self.frame_input_planet, width=10)
        self.eccentricity_planet_min.grid(column=0, row=7)
        self.eccentricity_planet_min.insert(tk.END, "0")
        self.label = tk.Label(master=self.frame_input_planet, text=' <= Eccentricity <= ', fg="blue",
                              font=('Sans', '9', 'bold'))
        self.label.grid(column=1, row=7)
        self.eccentricity_planet_max = tk.Entry(master=self.frame_input_planet, width=10)
        self.eccentricity_planet_max.grid(column=2, row=7)
        self.eccentricity_planet_max.insert(tk.END, "1")
        if not check_ecc:
            self.eccentricity_planet_min.configure(state="disable")
            self.eccentricity_planet_max.configure(state="disable")
        self.limits = tk.Label(master=self.frame_input_planet, text='i.e. {0., 1.}', fg="red",
                               font=('Sans', '9', 'bold'))
        self.limits.grid(column=3, row=7)
        self.T_eq_planet_min = tk.Entry(master=self.frame_input_planet, width=10)
        self.T_eq_planet_min.grid(column=0, row=8)
        self.T_eq_planet_min.insert(tk.END, "200")
        self.label = tk.Label(master=self.frame_input_planet, text=' <= T eq [K] <= ', fg="blue",
                              font=('Sans', '9', 'bold'))
        self.label.grid(column=1, row=8)
        self.T_eq_planet_max = tk.Entry(master=self.frame_input_planet, width=10)
        self.T_eq_planet_max.grid(column=2, row=8)
        self.T_eq_planet_max.insert(tk.END, "3000")
        if not check_teq:
            self.T_eq_planet_max.configure(state="disable")
            self.T_eq_planet_min.configure(state="disable")
        self.limits = tk.Label(master=self.frame_input_planet, text='i.e. {200., 3000.}', fg="red",
                               font=('Sans', '9', 'bold'))
        self.limits.grid(column=3, row=8)
        self.show_error_plot_var = tk.IntVar()
        self.show_error_check = tk.Checkbutton(master=self.frame_input_planet, text="Show planets mass/radius errors?",
                                               variable=self.show_error_plot_var, fg="#cc3300",
                                               font=('Sans', '9', 'bold'))
        self.show_error_check.grid(column=4, row=1, columnspan=2)
        self.show_planets_labels_var = tk.IntVar()
        self.show_planets_labels_check = tk.Checkbutton(master=self.frame_input_planet, text="Show planets labels?",
                                                        variable=self.show_planets_labels_var, fg="#cc3300",
                                                        font=('Sans', '9', 'bold'))
        self.show_planets_labels_check.grid(column=4, row=3, columnspan=2)
        self.get_only_planetary_system_var = tk.IntVar()
        self.get_only_planetary_system_check = tk.Checkbutton(master=self.frame_input_planet,
                                                              text="Filter by systems with mutliple planets?",
                                                              variable=self.get_only_planetary_system_var,
                                                              fg="#cc3300",
                                                              font=('Sans', '9', 'bold'), command=self.numberOfPlanetEn)
        self.get_only_planetary_system_check.grid(column=4, row=5, columnspan=2)
        self.label = tk.Label(master=self.frame_input_planet, text='N. Planets', fg="blue",
                              font=('Sans', '9', 'bold'))
        self.label.grid(column=4, row=6)
        self.number_planets_system = tk.Entry(master=self.frame_input_planet, width=10)
        self.number_planets_system.grid(column=5, row=6)
        self.number_planets_system.insert(tk.END, "2")
        self.number_planets_system.configure(state='disabled')
        self.frame_input_planet.pack(padx=3, pady=3)

    def numberOfPlanetEn(self):
        if self.get_only_planetary_system_var.get():
            self.number_planets_system.configure(state='normal')
        else:
            self.number_planets_system.configure(state='disabled')

