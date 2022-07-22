import math
import time
import tkinter as tk
import pandas as pd
from tkinter import messagebox as msgbox

import matplotlib.colors as colors
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

import numpy as np

from matplotlib import pyplot as plt

from GUI_Plot import MassRadiusDB


def pureFunction(type_name, x):
    if type_name == "pure-high-pressure-ices":
        return np.power(10, (0.13666292574887867 + 0.27183702181443314 * x -
                             0.007134024332627119 * np.power(x, 2) - 0.0021407416433092126 * np.power(x, 3) -
                             0.0022608931475693915 * np.power(x, 4) - 0.0002516518649610248 * np.power(x, 5) +
                             0.00011968169122553435 * np.power(x, 6) + 0.000011663496987412905 * np.power(x, 7) -
                             3.536434693875541e-6 * np.power(x, 8) - 1.6848230313524644e-7 * np.power(x, 9) +
                             4.4044933682275176e-8 * np.power(x, 10)))
    elif type_name == "pure-Silicates":
        return np.power(10, (0.020013868549526272 + 0.29811170324848235 * x -
                             0.02012734730157388 * np.power(x, 2) - 0.0052918215948260265 * np.power(x, 3) -
                             0.0003311775031243655 * np.power(x, 4) + 0.00004856681718363753 * np.power(x, 5) -
                             0.00001245509278944841 * np.power(x, 6) - 1.3074832660503483e-6 * np.power(x, 7) +
                             8.211419885278952e-7 * np.power(x, 8) + 3.47368749025812e-8 * np.power(x, 9) -
                             1.1251826465596989e-8 * np.power(x, 10)))
    else:
        return (np.power(10, (-0.11408792224566819 + 0.27851883673695 * x -
                              0.01997874049680844 * np.power(x, 2) - 0.002490304269884624 * np.power(x, 3) +
                              0.00007525048500183394 * np.power(x, 4) - 0.00007162041164677924 * np.power(x, 5) -
                              0.00003393158521958243 * np.power(x, 6) + 8.589995554646332e-7 * np.power(x, 7) +
                              1.132375249329131e-6 * np.power(x, 8) + 2.2299345660512832e-8 * np.power(x, 9) -
                              1.0475165171649914e-8 * np.power(x, 10))))


def rangeFunction(type_name, x, r):
    if type_name == "Fe-Silicates":
        return ((np.power(10, (-0.11408792224566819 + 0.27851883673695 * x -
                               0.01997874049680844 * np.power(x, 2) - 0.002490304269884624 * np.power(x, 3) +
                               0.00007525048500183394 * np.power(x, 4) - 0.00007162041164677924 * np.power(x, 5) -
                               0.00003393158521958243 * np.power(x, 6) + 8.589995554646332e-7 * np.power(x, 7) +
                               1.132375249329131e-6 * np.power(x, 8) + 2.2299345660512832e-8 * np.power(x, 9) -
                               1.0475165171649914e-8 * np.power(x, 10)))) < r) & (
                       r < (np.power(10, (0.020013868549526272 + 0.29811170324848235 * x -
                                          0.02012734730157388 * np.power(x, 2) - 0.0052918215948260265 * np.power(x,
                                                                                                                  3) -
                                          0.0003311775031243655 * np.power(x,
                                                                           4) + 0.00004856681718363753 * np.power(x,
                                                                                                                  5) -
                                          0.00001245509278944841 * np.power(x,
                                                                            6) - 1.3074832660503483e-6 * np.power(x,
                                                                                                                  7) +
                                          8.211419885278952e-7 * np.power(x, 8) + 3.47368749025812e-8 * np.power(x,
                                                                                                                 9) -
                                          1.1251826465596989e-8 * np.power(x, 10)))))
    elif type_name == "Silicates-H2O":
        return ((np.power(10, (0.020013868549526272 + 0.29811170324848235 * x -
                               0.02012734730157388 * np.power(x, 2) - 0.0052918215948260265 * np.power(x, 3) -
                               0.0003311775031243655 * np.power(x, 4) + 0.00004856681718363753 * np.power(x, 5) -
                               0.00001245509278944841 * np.power(x, 6) - 1.3074832660503483e-6 * np.power(x, 7) +
                               8.211419885278952e-7 * np.power(x, 8) + 3.47368749025812e-8 * np.power(x, 9) -
                               1.1251826465596989e-8 * np.power(x, 10)))) < r) & (
                       r < np.power(10, (0.13666292574887867 + 0.27183702181443314 * x -
                                         0.007134024332627119 * np.power(x, 2) - 0.0021407416433092126 * np.power(x,
                                                                                                                  3) -
                                         0.0022608931475693915 * np.power(x, 4) - 0.0002516518649610248 * np.power(
                           x, 5) +
                                         0.00011968169122553435 * np.power(x,
                                                                           6) + 0.000011663496987412905 * np.power(
                           x, 7) -
                                         3.536434693875541e-6 * np.power(x, 8) - 1.6848230313524644e-7 * np.power(x,
                                                                                                                  9) +
                                         4.4044933682275176e-8 * np.power(x, 10))))
    elif type_name == "Envelope-H2O":
        return (np.power(10, (0.13666292574887867 + 0.27183702181443314 * x -
                              0.007134024332627119 * np.power(x, 2) - 0.0021407416433092126 * np.power(x, 3) -
                              0.0022608931475693915 * np.power(x, 4) - 0.0002516518649610248 * np.power(x, 5) +
                              0.00011968169122553435 * np.power(x, 6) + 0.000011663496987412905 * np.power(x, 7) -
                              3.536434693875541e-6 * np.power(x, 8) - 1.6848230313524644e-7 * np.power(x, 9) +
                              4.4044933682275176e-8 * np.power(x, 10)))) < r
    elif type_name == "Envelope-Silicates":
        return (np.power(10, (0.020013868549526272 + 0.29811170324848235 * x -
                              0.02012734730157388 * np.power(x, 2) - 0.0052918215948260265 * np.power(x, 3) -
                              0.0003311775031243655 * np.power(x, 4) + 0.00004856681718363753 * np.power(x, 5) -
                              0.00001245509278944841 * np.power(x, 6) - 1.3074832660503483e-6 * np.power(x, 7) +
                              8.211419885278952e-7 * np.power(x, 8) + 3.47368749025812e-8 * np.power(x, 9) -
                              1.1251826465596989e-8 * np.power(x, 10)))) < r
    else:
        return (np.power(10, (-0.11408792224566819 + 0.27851883673695 * x -
                              0.01997874049680844 * np.power(x, 2) - 0.002490304269884624 * np.power(x, 3) +
                              0.00007525048500183394 * np.power(x, 4) - 0.00007162041164677924 * np.power(x, 5) -
                              0.00003393158521958243 * np.power(x, 6) + 8.589995554646332e-7 * np.power(x, 7) +
                              1.132375249329131e-6 * np.power(x, 8) + 2.2299345660512832e-8 * np.power(x, 9) -
                              1.0475165171649914e-8 * np.power(x, 10)))) < r


def applyFunction(type_name, x, r):
    if type_name == "Fe-Silicates":
        return (r - np.power(10, (-0.11408792224566819 + 0.27851883673695 * x -
                                  0.01997874049680844 * np.power(x, 2) - 0.002490304269884624 * np.power(x, 3) +
                                  0.00007525048500183394 * np.power(x, 4) - 0.00007162041164677924 * np.power(x, 5) -
                                  0.00003393158521958243 * np.power(x, 6) + 8.589995554646332e-7 * np.power(x, 7) +
                                  1.132375249329131e-6 * np.power(x, 8) + 2.2299345660512832e-8 * np.power(x, 9) -
                                  1.0475165171649914e-8 * np.power(x, 10)))) / (
                       np.power(10, (0.020013868549526272 + 0.29811170324848235 * x -
                                     0.02012734730157388 * np.power(x, 2) - 0.0052918215948260265 * np.power(x, 3) -
                                     0.0003311775031243655 * np.power(x, 4) + 0.00004856681718363753 * np.power(x,
                                                                                                                5) -
                                     0.00001245509278944841 * np.power(x, 6) - 1.3074832660503483e-6 * np.power(x,
                                                                                                                7) +
                                     8.211419885278952e-7 * np.power(x, 8) + 3.47368749025812e-8 * np.power(x, 9) -
                                     1.1251826465596989e-8 * np.power(x, 10))) - np.power(10, (
                       -0.11408792224566819 + 0.27851883673695 * x -
                       0.01997874049680844 * np.power(x,
                                                      2) - 0.002490304269884624 * np.power(x, 3) +
                       0.00007525048500183394 * np.power(x,
                                                         4) - 0.00007162041164677924 * np.power(x, 5) -
                       0.00003393158521958243 * np.power(x,
                                                         6) + 8.589995554646332e-7 * np.power(x, 7) +
                       1.132375249329131e-6 * np.power(x,
                                                       8) + 2.2299345660512832e-8 * np.power(x, 9) -
                       1.0475165171649914e-8 * np.power(x, 10))))
    elif type_name == "Silicates-H2O":
        return (r - np.power(10, (0.020013868549526272 + 0.29811170324848235 * x -
                                  0.02012734730157388 * np.power(x, 2) - 0.0052918215948260265 * np.power(x, 3) -
                                  0.0003311775031243655 * np.power(x, 4) + 0.00004856681718363753 * np.power(x, 5) -
                                  0.00001245509278944841 * np.power(x, 6) - 1.3074832660503483e-6 * np.power(x, 7) +
                                  8.211419885278952e-7 * np.power(x, 8) + 3.47368749025812e-8 * np.power(x, 9) -
                                  1.1251826465596989e-8 * np.power(x, 10)))) / (
                       np.power(10., (0.13666292574887867 + 0.27183702181443314 * x -
                                      0.007134024332627119 * np.power(x, 2) - 0.0021407416433092126 * np.power(x,
                                                                                                               3) -
                                      0.0022608931475693915 * np.power(x, 4) - 0.0002516518649610248 * np.power(x,
                                                                                                                5) +
                                      0.00011968169122553435 * np.power(x, 6) + 0.000011663496987412905 * np.power(
                                   x, 7) -
                                      3.536434693875541e-6 * np.power(x, 8) - 1.6848230313524644e-7 * np.power(x,
                                                                                                               9) +
                                      4.4044933682275176e-8 * np.power(x, 10))) - np.power(10.,
                                                                                           (
                                                                                                   0.020013868549526272 + 0.29811170324848235 * x -
                                                                                                   0.02012734730157388 * np.power(
                                                                                               x,
                                                                                               2) - 0.0052918215948260265 * np.power(
                                                                                               x, 3) -
                                                                                                   0.0003311775031243655 * np.power(
                                                                                               x,
                                                                                               4) + 0.00004856681718363753 * np.power(
                                                                                               x, 5) -
                                                                                                   0.00001245509278944841 * np.power(
                                                                                               x,
                                                                                               6) - 1.3074832660503483e-6 * np.power(
                                                                                               x, 7) +
                                                                                                   8.211419885278952e-7 * np.power(
                                                                                               x,
                                                                                               8) + 3.47368749025812e-8 * np.power(
                                                                                               x, 9) -
                                                                                                   1.1251826465596989e-8 * np.power(
                                                                                               x, 10))))
    elif type_name == "Envelope-H2O":
        return ((1 / np.power(10, (0.13666292574887867 + 0.27183702181443314 * x -
                                   0.007134024332627119 * np.power(x, 2) - 0.0021407416433092126 * np.power(x, 3) -
                                   0.0022608931475693915 * np.power(x, 4) - 0.0002516518649610248 * np.power(x, 5) +
                                   0.00011968169122553435 * np.power(x, 6) + 0.000011663496987412905 * np.power(x, 7) -
                                   3.536434693875541e-6 * np.power(x, 8) - 1.6848230313524644e-7 * np.power(x, 9) +
                                   4.4044933682275176e-8 * np.power(x, 10))) - 1 / r)) * np.power(10, x)

    elif type_name == "Envelope-Silicates":
        return ((1 / np.power(10, (0.020013868549526272 + 0.29811170324848235 * x -
                                   0.02012734730157388 * np.power(x, 2) - 0.0052918215948260265 * np.power(x, 3) -
                                   0.0003311775031243655 * np.power(x, 4) + 0.00004856681718363753 * np.power(x, 5) -
                                   0.00001245509278944841 * np.power(x, 6) - 1.3074832660503483e-6 * np.power(x, 7) +
                                   8.211419885278952e-7 * np.power(x, 8) + 3.47368749025812e-8 * np.power(x, 9) -
                                   1.1251826465596989e-8 * np.power(x, 10))) - 1 / r)) * np.power(10, x)
    else:
        return ((1 / np.power(10, (-0.11408792224566819 + 0.27851883673695 * x -
                                   0.01997874049680844 * np.power(x, 2) - 0.002490304269884624 * np.power(x, 3) +
                                   0.00007525048500183394 * np.power(x, 4) - 0.00007162041164677924 * np.power(x, 5) -
                                   0.00003393158521958243 * np.power(x, 6) + 8.589995554646332e-7 * np.power(x, 7) +
                                   1.132375249329131e-6 * np.power(x, 8) + 2.2299345660512832e-8 * np.power(x, 9) -
                                   1.0475165171649914e-8 * np.power(x, 10))) - 1 / r)) * np.power(10, x)


def helpButtonFunc():
    msgbox.showinfo(title="INFO",
                    message="Plot options. \n\nThe user can plot planets with mass and radius measured with a relative uncertainty better than a specific threshold (in %). \nThe threshold can be increased/decreased by steps of 1% by using the +/- button. \nBy pushing the button '\u25B6', the threshold (for mass or radius) is increased automatically by steps of 1%, and the mass-radius diagram is updated in a sequence, adding progressively to the plot the planets with less precise measurements. \n\nFrom the drop down menu, the user can select the parameter to be used in the 3D colormap plot. \n\nThe green button 'Plot' will refresh the mass-radius diagram after any change to the input values and selected options made by the user.")


class Frame_Run_Plot:
    cbl_third_coord = None
    cbl_cmap = None
    gui = None
    frame_run_plot = None
    label = None
    mass_step = None
    mass_back_step_btn = None
    mass_next_step_btn = None
    mass_start_step_btn = None
    mass_verse_btn = None
    mass_label_verse = None
    radius_step = None
    radius_back_step_btn = None
    radius_next_step_btn = None
    radius_start_step_btn = None
    radius_verse_btn = None
    radius_label_verse = None
    plot_current_situation_btn = None
    data0 = None
    # Internal Variables
    mmin = None
    mmax = None
    rmin = None
    rmax = None
    xscale = None
    yscale = None
    age_host_min = None
    age_host_max = None
    Teff_min = None
    Teff_max = None
    FeHdex_min = None
    FeHdex_max = None
    mstar_min = None
    mstar_max = None
    rstar_min = None
    rstar_max = None
    Porb_min = None
    Porb_max = None
    aorb_min = None
    aorb_max = None
    eccentricity_min = None
    eccentricity_max = None
    Teq_min = None
    Teq_max = None
    sigmaMpercent = None
    sigmaRpercent = None
    histmassbin = None
    histradiusbin = None
    histzetabin = None
    logcountinmass = None
    logcountinradius = None
    env2 = None
    env1 = None
    env3 = None
    env4 = None
    add1 = None
    filter1 = None
    add2 = None
    np2 = None
    subsetdata = None
    newPlanets = None
    global_stop_mass = None
    global_stop_radius = None
    mass_radius_plot = None
    number_element_plot_density = None
    fullDBMatrix = None
    ticks_x = None
    ticks_y = None
    names = None
    sc = None
    sc2 = None
    sc1 = None
    sc3 = None
    annot = None
    num_new_planets = None
    newcmp = None
    show_error_plot = None
    mass_coeff = None
    radius_coeff = None
    index_ecc = None
    index_FeH = None
    index_tstar = None
    index_mass_max = None
    index_p_orb = None
    index_a_orb = None
    index_teq = None
    index_mass_min = None
    index_min_rad = None
    index_mass_star = None
    index_radius_star = None
    index_rad_max = None
    index_rad_p = None
    index_mass_p = None
    index_age_host = None
    check_ecc = None
    check_FeH = None
    check_tstar = None
    check_p_orb = None
    check_a_orb = None
    check_teq = None
    check_mass_star = None
    check_radius_star = None
    check_age_host = None
    choose_filter_map_var = None
    choose_filter_map = None
    max_val = None
    min_val = None
    chosen_index = None
    check = None
    coeff = None
    help_button = None
    font_labels = None
    font_ticks = None
    ticks_y_lim = None
    ticks_x_lim = None
    show_all_planets_labels = None
    core_contours = None
    get_only_planetary_system = None
    number_planets_system = None

    def __init__(self, window, gui, data0, mass_coeff, radius_coeff, index_ecc, index_FeH, index_tstar, index_mass_max,
                 index_p_orb, index_a_orb, index_teq, index_mass_min, index_min_rad,
                 index_mass_star, index_radius_star, index_rad_max, index_rad_p, index_mass_p, index_age_host,
                 check_age_host, check_ecc, check_FeH, check_tstar, check_p_orb, check_a_orb, check_teq,
                 check_mass_star, check_radius_star):
        self.data0 = data0
        self.mass_coeff = mass_coeff
        self.radius_coeff = radius_coeff
        self.index_ecc = index_ecc
        self.index_FeH = index_FeH
        self.index_tstar = index_tstar
        self.index_mass_max = index_mass_max
        self.index_p_orb = index_p_orb
        self.index_a_orb = index_a_orb
        self.index_teq = index_teq
        self.index_mass_min = index_mass_min
        self.index_min_rad = index_min_rad
        self.index_mass_star = index_mass_star
        self.index_radius_star = index_radius_star
        self.index_rad_max = index_rad_max
        self.index_rad_p = index_rad_p
        self.index_mass_p = index_mass_p
        self.index_age_host = index_age_host
        self.check_age_host = check_age_host
        self.check_ecc = check_ecc
        self.check_FeH = check_FeH
        self.check_tstar = check_tstar
        self.check_p_orb = check_p_orb
        self.check_a_orb = check_a_orb
        self.check_teq = check_teq
        self.check_mass_star = check_mass_star
        self.check_radius_star = check_radius_star
        self.gui = gui
        self.number_element_plot_density = 5
        self.frame_run_plot = tk.Frame(window, highlightbackground="black", highlightthickness=1, padx=5, pady=2)
        self.label = tk.Label(master=self.frame_run_plot, text='\u03C3Mp/Mp(%)', fg="blue", font=('Sans', '9', 'bold'))
        self.label.grid(column=0, row=0)
        self.mass_step = tk.Entry(master=self.frame_run_plot, width=4)
        self.mass_step.grid(column=1, row=0)
        self.mass_step.insert(-1, "50")
        self.mass_back_step_btn = tk.Button(master=self.frame_run_plot, text="-", command=self.massStepBackBtn,
                                            bg="#cc0099", font=('Sans', '9', 'bold'))
        self.mass_back_step_btn.grid(column=2, row=0)
        self.mass_start_step_btn = tk.Button(master=self.frame_run_plot, text="\u25B6", command=self.massRunBtn,
                                             bg="#ffff00", font=('Sans', '9', 'bold'))
        self.mass_start_step_btn.grid(column=3, row=0)
        self.mass_next_step_btn = tk.Button(master=self.frame_run_plot, text="+", command=self.massStepForwardBtn,
                                            bg="#c65353", font=('Sans', '9', 'bold'))
        self.mass_next_step_btn.grid(column=4, row=0)
        self.mass_verse_btn = tk.Button(master=self.frame_run_plot, text="Verse", bg="#669999",
                                        font=('Sans', '9', 'bold'), command=self.massChangeVerse)
        self.mass_verse_btn.grid(column=5, row=0)
        self.mass_label_verse = tk.Label(master=self.frame_run_plot, text='Forward', fg="#ff6600",
                                         font=('Sans', '9', 'bold'), borderwidth=2, relief="ridge")
        self.mass_label_verse.grid(column=6, row=0)
        self.help_button = tk.Button(master=self.frame_run_plot, text="?", command=helpButtonFunc, bg="black",
                                     fg="yellow", font=('Sans', '10', 'bold'))
        self.help_button.grid(column=9, row=0)
        self.label = tk.Label(master=self.frame_run_plot, text='\u03C3Rp/Rp(%)', fg="blue", font=('Sans', '9', 'bold'))
        self.label.grid(column=0, row=1)
        self.radius_step = tk.Entry(master=self.frame_run_plot, width=4)
        self.radius_step.grid(column=1, row=1)
        self.radius_step.insert(-1, "20")
        self.radius_back_step_btn = tk.Button(master=self.frame_run_plot, text="-", command=self.radiusStepBackBtn,
                                              bg="#cc0099", font=('Sans', '9', 'bold'))
        self.radius_back_step_btn.grid(column=2, row=1)
        self.radius_start_step_btn = tk.Button(master=self.frame_run_plot, text="\u25B6", command=self.radiusRunBtn,
                                               bg="#ffff00", font=('Sans', '9', 'bold'))
        self.radius_start_step_btn.grid(column=3, row=1)
        self.radius_next_step_btn = tk.Button(master=self.frame_run_plot, text="+", command=self.radiusStepForwardBtn,
                                              bg="#c65353", font=('Sans', '9', 'bold'))
        self.radius_next_step_btn.grid(column=4, row=1)
        self.radius_verse_btn = tk.Button(master=self.frame_run_plot, text="Verse", bg="#669999",
                                          font=('Sans', '9', 'bold'),
                                          command=self.radiusChangeVerse)
        self.radius_verse_btn.grid(column=5, row=1)
        self.radius_label_verse = tk.Label(master=self.frame_run_plot, text='Forward', fg="#ff6600",
                                           font=('Sans', '9', 'bold'), borderwidth=2, relief="ridge")
        self.radius_label_verse.grid(column=6, row=1)

        options_list = ["None"]
        if self.check_teq:
            options_list.append("Planet Temp")
        if self.check_mass_star:
            options_list.append("Star Mass")
        if self.check_radius_star:
            options_list.append("Star Radius")
        if self.check_tstar:
            options_list.append("Star Temp")
        if self.check_FeH:
            options_list.append("[Fe/H]")
        if self.check_ecc:
            options_list.append("Eccentricity")
        if self.check_age_host:
            options_list.append("Age")
        if self.check_p_orb:
            options_list.append("Orbital Period")
        if self.check_a_orb:
            options_list.append("Semi-major axis")
        self.choose_filter_map_var = tk.StringVar()
        self.choose_filter_map = tk.OptionMenu(self.frame_run_plot, self.choose_filter_map_var, *options_list)
        self.choose_filter_map.grid(column=7, row=0, rowspan=2)
        self.choose_filter_map_var.set("None")
        self.plot_current_situation_btn = tk.Button(master=self.frame_run_plot, text="PLOT", width=15,
                                                    bg="#00ff00", font=('Sans', '13', 'bold'),
                                                    command=self.plotCurrentSituation)
        self.plot_current_situation_btn.grid(column=8, row=0, rowspan=2)
        self.frame_run_plot.pack(padx=3, pady=3)

    def massStepBackBtn(self):
        self.stepBackForwMass(int(self.mass_step.get()), -1)

    def massStepForwardBtn(self):
        self.stepBackForwMass(int(self.mass_step.get()), 1)

    def stepBackForwMass(self, val, step):
        self.mass_step.delete(0, tk.END)
        self.mass_step.insert(-1, val + step)
        self.executeRoutine(int(self.mass_step.get()), int(self.radius_step.get()))

    def massRunBtn(self):
        if self.mass_start_step_btn["text"] == "\u25B6":
            self.global_stop_mass = False
            self.mass_start_step_btn["text"] = "\u23F8"
            var_start = int(self.mass_step.get())
            if self.mass_label_verse["text"] == "Forward":
                var_stop = 100
                var_step = 1
            else:
                var_stop = 0
                var_step = -1
            for i in range(var_start, var_stop, var_step):
                if self.global_stop_mass:
                    break
                time.sleep(1)
                self.mass_step.delete(0, tk.END)
                self.mass_step.insert(-1, str(i))
                self.executeRoutine(i, int(self.radius_step.get()))
                self.gui.window.update()
        else:
            self.mass_start_step_btn["text"] = "\u25B6"
            self.global_stop_mass = True
            self.gui.window.update()

    def massChangeVerse(self):
        if self.mass_label_verse["text"] == "Forward":
            self.mass_label_verse["text"] = "Backward"
        else:
            self.mass_label_verse["text"] = "Forward"

    def plotCurrentSituation(self):
        self.executeRoutine(int(self.mass_step.get()), int(self.radius_step.get()))

    def radiusStepBackBtn(self):
        self.stepBackForwRadius(int(self.radius_step.get()), -1)

    def radiusStepForwardBtn(self):
        self.stepBackForwRadius(int(self.radius_step.get()), 1)

    def stepBackForwRadius(self, val, step):
        self.radius_step.delete(0, tk.END)
        self.radius_step.insert(-1, val + step)
        self.executeRoutine(int(self.mass_step.get()), int(self.radius_step.get()))

    def radiusRunBtn(self):
        if self.radius_start_step_btn["text"] == "\u25B6":
            self.global_stop_radius = False
            self.radius_start_step_btn["text"] = "\u23F8"
            var_start = int(self.radius_step.get())
            if self.radius_label_verse["text"] == "Forward":
                var_stop = 100
                var_step = 1
            else:
                var_stop = 0
                var_step = -1
            for i in range(var_start, var_stop, var_step):
                if self.global_stop_radius:
                    break
                time.sleep(1)
                self.radius_step.delete(0, tk.END)
                self.radius_step.insert(-1, str(i))
                self.executeRoutine(int(self.mass_step.get()), i)
                self.gui.window.update()
        else:
            self.radius_start_step_btn["text"] = "\u25B6"
            self.global_stop_radius = True
            self.gui.window.update()

    def radiusChangeVerse(self):
        if self.radius_label_verse["text"] == "Forward":
            self.radius_label_verse["text"] = "Backward"
        else:
            self.radius_label_verse["text"] = "Forward"

    def dataAcquisition(self, sigmaMpercent, sigmaRpercent):
        self.ticks_x_lim = int(self.gui.frame_input_master.frame_export_file.x_ticks_entry.get())
        self.ticks_y_lim = int(self.gui.frame_input_master.frame_export_file.y_ticks_entry.get())
        self.font_labels = float(self.gui.frame_input_master.frame_export_file.font_labels_entry.get())
        self.font_ticks = float(self.gui.frame_input_master.frame_export_file.font_ticks_entry.get())
        self.mmin = float(self.gui.frame_input_master.frame_scale_plot.mass_min.get())
        self.mmax = float(self.gui.frame_input_master.frame_scale_plot.mass_max.get())
        self.rmin = float(self.gui.frame_input_master.frame_scale_plot.radius_min.get())
        self.rmax = float(self.gui.frame_input_master.frame_scale_plot.radius_max.get())
        self.xscale = self.gui.frame_input_master.frame_scale_plot.mass_label_scale['text']
        self.yscale = self.gui.frame_input_master.frame_scale_plot.radius_label_scale['text']
        self.age_host_min = float(self.gui.frame_input_master.frame_input_planet.age_host_min.get())
        self.age_host_max = float(self.gui.frame_input_master.frame_input_planet.age_host_max.get())
        self.Teff_min = float(self.gui.frame_input_master.frame_input_planet.t_eff_star_min.get())
        self.Teff_max = float(self.gui.frame_input_master.frame_input_planet.t_eff_star_max.get())
        self.FeHdex_min = float(self.gui.frame_input_master.frame_input_planet.Fe_H_min.get())
        self.FeHdex_max = float(self.gui.frame_input_master.frame_input_planet.Fe_H_max.get())
        self.mstar_min = float(self.gui.frame_input_master.frame_input_planet.M_star_min.get())
        self.mstar_max = float(self.gui.frame_input_master.frame_input_planet.M_star_max.get())
        self.rstar_min = float(self.gui.frame_input_master.frame_input_planet.R_star_min.get())
        self.rstar_max = float(self.gui.frame_input_master.frame_input_planet.R_star_max.get())
        self.Porb_min = float(self.gui.frame_input_master.frame_input_planet.P_orb_planet_min.get())
        self.Porb_max = float(self.gui.frame_input_master.frame_input_planet.P_orb_planet_max.get())
        self.aorb_min = float(self.gui.frame_input_master.frame_input_planet.semi_major_axes_planet_min.get())
        self.aorb_max = float(self.gui.frame_input_master.frame_input_planet.semi_major_axes_planet_max.get())
        self.eccentricity_min = float(self.gui.frame_input_master.frame_input_planet.eccentricity_planet_min.get())
        self.eccentricity_max = float(self.gui.frame_input_master.frame_input_planet.eccentricity_planet_max.get())
        self.show_error_plot = self.gui.frame_input_master.frame_input_planet.show_error_plot_var.get()
        self.show_all_planets_labels = self.gui.frame_input_master.frame_input_planet.show_planets_labels_var.get()
        self.get_only_planetary_system = self.gui.frame_input_master.frame_input_planet.get_only_planetary_system_var.get()
        if self.get_only_planetary_system:
            self.number_planets_system = int(self.gui.frame_input_master.frame_input_planet.number_planets_system.get())
            if self.number_planets_system <= 1:
                msgbox.showerror(title="ERROR", message="The number of planets must be greater than 1")
                return
        self.Teq_min = float(self.gui.frame_input_master.frame_input_planet.T_eq_planet_min.get())
        self.Teq_max = float(self.gui.frame_input_master.frame_input_planet.T_eq_planet_max.get())
        self.histmassbin = int(self.gui.frame_input_master.frame_histogram_info.mass_bin_var.get())
        self.histradiusbin = int(self.gui.frame_input_master.frame_histogram_info.radius_bin_var.get())
        self.histzetabin = int(self.gui.frame_input_master.frame_histogram_info.zeta_bin_var.get())
        self.logcountinmass = self.gui.frame_input_master.frame_histogram_info.mass_label_plot["text"]
        self.logcountinradius = self.gui.frame_input_master.frame_histogram_info.radius_label_plot["text"]
        self.env2 = self.gui.frame_input_master.frame_envelope_plot.label_envelope["text"]
        self.core_contours = self.gui.frame_input_master.frame_envelope_plot.core_contours_var.get()
        self.env1 = (self.env2 != "None")
        self.env3 = self.gui.frame_input_master.frame_pure_hydrogen.mass_radius_check_var.get()
        self.env4 = self.gui.frame_input_master.frame_pure_hydrogen.central_density_check_var.get()
        self.add1 = self.gui.frame_input_master.frame_new_planet.add_new_planet_check_var.get()
        self.filter1 = self.gui.frame_input_master.frame_new_planet.filter_new_planet_check_var.get()
        self.add2 = self.gui.frame_input_master.frame_new_planet.label_new_planet_check_var.get()
        data2 = self.data0
        # PLANETARY SYSTEM
        arr_letter = ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                      "u", "v", "w", "x", "y", "z"]
        if self.get_only_planetary_system:
            names = data2.iloc[:, 0]
            index = [idx for idx, s in enumerate(names) if s[-1] in arr_letter]
            names2 = np.array(names[index].array)
            names3 = list()
            for name in names2:
                names3.append(name[:-1])
            names4 = np.unique(names3)
            dizionario_planet = dict()
            for elem in names4:
                occur = names3.count(elem)
                if occur >= self.number_planets_system:
                    dizionario_planet[elem] = names3.count(elem)
            index2 = [idx for idx, s in enumerate(names) if s[:-1] in dizionario_planet.keys()]
            data2 = data2.iloc[index2, :]
        self.subsetdata = data2[
            (self.mmin <= data2[self.index_mass_p] * self.mass_coeff) & (
                    data2[self.index_mass_p] * self.mass_coeff <= self.mmax) &
            (self.rmin <= data2[self.index_rad_p] * self.radius_coeff) & (
                    data2[self.index_rad_p] * self.radius_coeff <= self.rmax) &
            (data2[self.index_rad_max] / data2[self.index_rad_p] <= sigmaRpercent / 100) &
            (data2[self.index_min_rad] / data2[self.index_rad_p] <= sigmaRpercent / 100) &
            (data2[self.index_mass_min] / data2[self.index_mass_p] <= sigmaMpercent / 100) &
            (data2[self.index_mass_max] / data2[self.index_mass_p] <= sigmaMpercent / 100) &
            ((data2[self.index_rad_p] * self.radius_coeff) ** 4 / (data2[self.index_mass_p] * self.mass_coeff) > 0.01)]
        if self.check_p_orb:
            self.subsetdata = self.subsetdata[(self.Porb_min <= self.subsetdata[self.index_p_orb]) & (
                    self.subsetdata[self.index_p_orb] <= self.Porb_max)]
        if self.check_teq:
            self.subsetdata = self.subsetdata[
                (self.Teq_min <= self.subsetdata[self.index_teq]) & (self.subsetdata[self.index_teq] <= self.Teq_max)]
        if self.check_tstar:
            self.subsetdata = self.subsetdata[(self.Teff_min <= self.subsetdata[self.index_tstar]) & (
                    self.subsetdata[self.index_tstar] <= self.Teff_max)]
        if self.check_ecc:
            self.subsetdata = self.subsetdata[(self.eccentricity_min <= self.subsetdata[self.index_ecc]) & (
                    self.subsetdata[self.index_ecc] <= self.eccentricity_max)]
        if self.check_mass_star:
            self.subsetdata = self.subsetdata[(self.mstar_min <= self.subsetdata[self.index_mass_star]) & (
                    self.subsetdata[self.index_mass_star] <= self.mstar_max)]
        if self.check_radius_star:
            self.subsetdata = self.subsetdata[(self.rstar_min <= self.subsetdata[self.index_radius_star]) & (
                    self.subsetdata[self.index_radius_star] <= self.rstar_max)]
        if self.check_a_orb:
            self.subsetdata = self.subsetdata[(self.aorb_min <= self.subsetdata[self.index_a_orb]) & (
                    self.subsetdata[self.index_a_orb] <= self.aorb_max)]
        if self.check_FeH:
            self.subsetdata = self.subsetdata[(self.FeHdex_min <= self.subsetdata[self.index_FeH]) & (
                    self.subsetdata[self.index_FeH] <= self.FeHdex_max)]
        if self.check_age_host:
            self.subsetdata = self.subsetdata[(self.age_host_min <= self.subsetdata[self.index_age_host]) & (
                    self.subsetdata[self.index_age_host] <= self.age_host_max)]

        # NEW PLANET INPUT
        self.num_new_planets = 0
        temp_df = self.gui.frame_input_master.frame_new_planet.input_list
        if self.add1 and len(temp_df) > 0:
            self.newPlanets = pd.DataFrame(
                {0: temp_df["Name"], self.index_mass_p: temp_df["Mass_p"], self.index_mass_min: temp_df["Mass_sn_p"],
                 self.index_mass_max: temp_df["Mass_sp_p"], self.index_rad_p: temp_df["Radius_p"],
                 self.index_min_rad: temp_df["Radius_sn_p"],
                 self.index_rad_max: temp_df["Radius_sp_p"]})
            if self.check_age_host:
                self.newPlanets[self.index_age_host] = temp_df["Age"]
            if self.check_tstar:
                self.newPlanets[self.index_tstar] = temp_df["Tstar"]
            if self.check_mass_star:
                self.newPlanets[self.index_mass_star] = temp_df["Mstar"]
            if self.check_radius_star:
                self.newPlanets[self.index_radius_star] = temp_df["Rstar"]
            if self.check_p_orb:
                self.newPlanets[self.index_p_orb] = temp_df["p_orb"]
            if self.check_a_orb:
                self.newPlanets[self.index_a_orb] = temp_df["a_orb"]
            if self.check_ecc:
                self.newPlanets[self.index_ecc] = temp_df["Ecc"]
            if self.check_teq:
                self.newPlanets[self.index_teq] = temp_df["tPlanet"]
            if self.check_FeH:
                self.newPlanets[self.index_FeH] = temp_df["[Fe/H]"]
            self.newPlanets = self.newPlanets[
                (self.mmin <= self.newPlanets[self.index_mass_p] * self.mass_coeff) & (
                        self.newPlanets[self.index_mass_p] * self.mass_coeff <= self.mmax) &
                (self.rmin <= self.newPlanets[self.index_rad_p] * self.radius_coeff) & (
                        self.newPlanets[self.index_rad_p] * self.radius_coeff <= self.rmax)]
            if self.filter1:
                self.newPlanets = self.newPlanets[
                    (self.newPlanets[self.index_rad_max] / self.newPlanets[self.index_rad_p] <= sigmaRpercent / 100) &
                    (self.newPlanets[self.index_min_rad] / self.newPlanets[self.index_rad_p] <= sigmaRpercent / 100) &
                    (self.newPlanets[self.index_mass_min] / self.newPlanets[self.index_mass_p] <= sigmaMpercent / 100) &
                    (self.newPlanets[self.index_mass_max] / self.newPlanets[self.index_mass_p] <= sigmaMpercent / 100) &
                    ((self.newPlanets[self.index_rad_p] * self.radius_coeff) ** 4 / (
                            self.newPlanets[self.index_mass_p] * self.mass_coeff) > 0.01)]
                if self.check_p_orb:
                    self.newPlanets = self.newPlanets[(self.Porb_min <= self.newPlanets[self.index_p_orb]) & (
                            self.newPlanets[self.index_p_orb] <= self.Porb_max)]
                if self.check_teq:
                    self.newPlanets = self.newPlanets[(self.Teq_min <= self.newPlanets[self.index_teq]) & (
                            self.newPlanets[self.index_teq] <= self.Teq_max)]
                if self.check_tstar:
                    self.newPlanets = self.newPlanets[(self.Teff_min <= self.newPlanets[self.index_tstar]) & (
                            self.newPlanets[self.index_tstar] <= self.Teff_max)]
                if self.check_ecc:
                    self.newPlanets = self.newPlanets[(self.eccentricity_min <= self.newPlanets[self.index_ecc]) & (
                            self.newPlanets[self.index_ecc] <= self.eccentricity_max)]
                if self.check_mass_star:
                    self.newPlanets = self.newPlanets[(self.mstar_min <= self.newPlanets[self.index_mass_star]) & (
                            self.newPlanets[self.index_mass_star] <= self.mstar_max)]
                if self.check_radius_star:
                    self.newPlanets = self.newPlanets[(self.rstar_min <= self.newPlanets[self.index_radius_star]) & (
                            self.newPlanets[self.index_radius_star] <= self.rstar_max)]
                if self.check_a_orb:
                    self.newPlanets = self.newPlanets[(self.aorb_min <= self.newPlanets[self.index_a_orb]) & (
                            self.newPlanets[self.index_a_orb] <= self.aorb_max)]
                if self.check_FeH:
                    self.newPlanets = self.newPlanets[(self.FeHdex_min <= self.newPlanets[self.index_FeH]) & (
                            self.newPlanets[self.index_FeH] <= self.FeHdex_max)]
                if self.check_age_host:
                    self.newPlanets = self.newPlanets[(self.age_host_min <= self.newPlanets[self.index_age_host]) & (
                            self.newPlanets[self.index_age_host] <= self.age_host_max)]
            self.subsetdata = self.subsetdata.append(self.newPlanets, ignore_index=True)
            self.num_new_planets = len(self.newPlanets)
        self.names = np.array(self.subsetdata[0])

    def plotHistogramMass(self):
        array = self.subsetdata[self.index_mass_p] * self.mass_coeff
        self.gui.frame_output_plot.histogram_mass.clear()
        self.ticks_x = np.linspace(self.mmin, self.mmax, self.ticks_x_lim)
        self.gui.frame_output_plot.histogram_mass.set_title('Histogram of Mp/M⊕', fontsize=self.font_labels)
        if self.xscale == "Log":
            hist, bins, _ = plt.hist(array, self.histmassbin)
            self.gui.frame_output_plot.histogram_mass.axes.set_xscale("log")
            self.ticks_x = np.logspace(math.log10(min(array)), math.log10(max(array)), self.ticks_x_lim)
            histmassbin = np.logspace(np.log10(bins[0]), np.log10(bins[-1]), len(bins))
            arr = self.gui.frame_output_plot.histogram_mass.hist(array, histmassbin, color='#f9d616', edgecolor='black')
        else:
            arr = self.gui.frame_output_plot.histogram_mass.hist(array, self.histmassbin, color='#f9d616',
                                                                 edgecolor='black')
        if len(self.ticks_x) >= 14:
            index = [i for i in range(2, len(self.ticks_x), 2)]
            self.ticks_x = np.delete(self.ticks_x, index)
        self.gui.frame_output_plot.histogram_mass.axes.set_xlim(xmin=self.mmin, xmax=self.mmax)
        self.gui.frame_output_plot.histogram_mass.axes.set_xticks(self.ticks_x)
        self.gui.frame_output_plot.histogram_mass.axes.set_xticklabels(np.round(self.ticks_x, 1),
                                                                       fontsize=self.font_ticks)
        if self.logcountinmass == "Count":
            self.gui.frame_output_plot.histogram_mass.set_ylabel('Count', fontsize=self.font_labels)
        else:
            self.gui.frame_output_plot.histogram_mass.axes.set_yscale("log")
            self.gui.frame_output_plot.histogram_mass.set_ylabel('Log Count', fontsize=self.font_labels)
        self.gui.frame_output_plot.histogram_mass.axes.minorticks_off()
        for i in range(self.histmassbin):
            self.gui.frame_output_plot.histogram_mass.text(arr[1][i], arr[0][i], str(arr[0][i]), fontsize=7)

    def plotHistogramRadius(self):
        array = self.subsetdata[self.index_rad_p] * self.radius_coeff
        self.gui.frame_output_plot.histogram_radius.clear()
        self.ticks_y = np.linspace(self.rmin, self.rmax, self.ticks_y_lim)
        self.gui.frame_output_plot.histogram_radius.set_title('Histogram of Rp/R⊕', fontsize=self.font_labels)
        if self.yscale == "Log":
            hist, bins, _ = plt.hist(array, self.histradiusbin)
            self.gui.frame_output_plot.histogram_radius.axes.set_yscale("log")
            self.ticks_y = np.logspace(math.log10(min(array)), math.log10(max(array)), self.ticks_y_lim)
            histradiusbin = np.logspace(np.log10(bins[0]), np.log10(bins[-1]), len(bins))
            arr = self.gui.frame_output_plot.histogram_radius.hist(array, histradiusbin, orientation="horizontal",
                                                                   color='#f9d616', edgecolor='black')
        else:
            arr = self.gui.frame_output_plot.histogram_radius.hist(array, self.histradiusbin, orientation="horizontal",
                                                                   color='#f9d616', edgecolor='black')
        if len(self.ticks_y) >= 20:
            index = [i for i in range(2, len(self.ticks_y), 2)]
            self.ticks_y = np.delete(self.ticks_y, index)
        self.gui.frame_output_plot.histogram_radius.axes.set_ylim(ymin=self.rmin, ymax=self.rmax)
        self.gui.frame_output_plot.histogram_radius.axes.set_yticks(self.ticks_y)
        self.gui.frame_output_plot.histogram_radius.axes.set_yticklabels(np.round(self.ticks_y, 1))
        plt.setp(self.gui.frame_output_plot.histogram_radius.axes.get_yticklabels(), rotation=-90, fontsize=7,
                 horizontalalignment='right')
        if self.logcountinradius == "Count":
            self.gui.frame_output_plot.histogram_radius.set_xlabel('Count', fontsize=self.font_labels)
        else:
            self.gui.frame_output_plot.histogram_radius.axes.set_xscale("log")
            self.gui.frame_output_plot.histogram_radius.set_xlabel('Log Count', fontsize=self.font_labels)
        self.gui.frame_output_plot.histogram_radius.axes.minorticks_off()
        for i in range(self.histradiusbin):
            self.gui.frame_output_plot.histogram_radius.text(arr[0][i], arr[1][i], str(arr[0][i]), fontsize=7)
        self.ticks_y = np.append(self.ticks_y, self.rmax)

    def plotHistogramZeta(self):
        array = (self.subsetdata[self.index_rad_p] * self.radius_coeff) / (
                (self.subsetdata[self.index_mass_p] * self.mass_coeff) ** (1 / 4))
        self.gui.frame_output_plot.histogram_zeta.clear()
        self.gui.frame_output_plot.histogram_zeta.set_title('Histogram of \nζ = (Rp/R⊕)/(Mp/M⊕)^1/4',
                                                            fontsize=self.font_labels)
        hist, bins, _ = plt.hist(array, self.histzetabin)
        self.gui.frame_output_plot.histogram_zeta.axes.set_xscale("log")
        ticks = np.logspace(math.log10(min(array)), math.log10(max(array)), self.histzetabin)
        histzetabin = np.logspace(np.log10(bins[0]), np.log10(bins[-1]), len(bins))
        arr = self.gui.frame_output_plot.histogram_zeta.hist(array, histzetabin, color='#f9d616', edgecolor='black')
        if len(ticks) >= 6:
            index = [i for i in range(2, len(ticks), 2)]
            ticks = np.delete(ticks, index)
        self.gui.frame_output_plot.histogram_zeta.axes.set_xticks(ticks)
        self.gui.frame_output_plot.histogram_zeta.axes.set_xticklabels(np.round(ticks, 1), fontsize=self.font_ticks)
        self.gui.frame_output_plot.histogram_zeta.axes.minorticks_off()
        # self.gui.frame_output_plot.histogram_zeta.set_ylabel('Count', fontsize=self.font_labels)
        for i in range(self.histzetabin):
            self.gui.frame_output_plot.histogram_zeta.text(arr[1][i], arr[0][i], str(arr[0][i]), fontsize=7)

    def plotMassRadius(self):
        self.gui.frame_output_plot.mass_radius_plot.clear()
        if self.xscale == "Log":
            self.gui.frame_output_plot.mass_radius_plot.axes.set_xscale("log")
        if self.yscale == "Log":
            self.gui.frame_output_plot.mass_radius_plot.axes.set_yscale("log")
        if self.env1:
            cmp = plt.cm.get_cmap(self.gui.frame_input_master.frame_envelope_plot.choose_cmap_var.get())
            cmp = cmp((np.linspace(0, 1, 500)))
            cmp[:, 3] = 0.6
            transp = [0, 0, 0, 0]
            cmp[0, :] = transp
            self.newcmp = colors.ListedColormap(cmp)
            if self.env2 == "H20":
                self.H2OPlot()
            elif self.env2 == "Silicates":
                self.SilicatesPlot()
            else:
                self.FePlot()
            self.plotPureLine()
        # just plot mass - radius curves for pure - Hydrogen composition at different specific entropy values
        # according to Becker et al . 2014 ApJS
        if self.env3:
            self.plotMassRadiusHydrogen()
        if self.env4:
            self.plotMassRadiusHydrogenCentralDensity()
        self.plotPlanetTepCat()
        self.plotPlanetSolarSystem()
        if self.add1 and self.num_new_planets > 0:
            self.plotPlanetInput()
        self.gui.frame_output_plot.mass_radius_plot.axes.minorticks_off()
        self.gui.frame_output_plot.mass_radius_plot.axes.set_xlim(xmin=self.mmin, xmax=self.mmax)
        self.gui.frame_output_plot.mass_radius_plot.axes.set_ylim(ymin=self.rmin, ymax=self.rmax)
        self.gui.frame_output_plot.mass_radius_plot.axes.set_xticks(self.ticks_x)
        self.gui.frame_output_plot.mass_radius_plot.axes.set_xticklabels(np.round(self.ticks_x, 1),
                                                                         fontsize=self.font_ticks)
        self.gui.frame_output_plot.mass_radius_plot.axes.set_yticks(self.ticks_y)
        self.gui.frame_output_plot.mass_radius_plot.axes.set_yticklabels(np.round(self.ticks_y, 1),
                                                                         fontsize=self.font_ticks)
        self.gui.frame_output_plot.mass_radius_plot.set_ylabel("Planet Radius (Rp/R⊕)", fontsize=self.font_labels)
        self.gui.frame_output_plot.mass_radius_plot.set_xlabel("Planet Mass (Mp/M⊕)", fontsize=self.font_labels)
        self.gui.frame_output_plot.mass_radius_plot.set_title(
            "Planet Mass-Radius: \n\u03C3Mp/Mp(%)<=" + str(self.mass_step.get()) + "% \u03C3Rp/Rp(%)<=" + str(
                self.radius_step.get()) + "%", fontsize=self.font_labels)
        self.gui.frame_output_plot.mass_radius_plot.legend(loc="upper left")
        self.gui.frame_output_plot.plot_combined_canvas.draw()
        self.gui.frame_output_plot.plot_combined_canvas.mpl_connect("motion_notify_event", self.hover)

    def H2OPlot(self):
        # Density Plot for Fe - Silicates Contour Mesh, approximated by Power - Series in lg[mass]
        xx, yy = np.meshgrid(np.logspace(np.log10(self.mmin), np.log10(self.mmax), 500),
                             np.logspace(np.log10(self.rmin), np.log10(self.rmax), 500))
        x_values = np.log10(xx)
        if self.core_contours:
            self.densityPlot("Fe-Silicates", xx, x_values, yy, [0.2, 0.4, 0.6, 0.8])
            # Density Plot for Silicates - H2O Contour Mesh, approximated by Power - Series in lg[mass]
            self.densityPlot("Silicates-H2O", xx, x_values, yy, [0.2, 0.4, 0.6, 0.8])
        # Density Plot for Envelope - H2O Contour Mesh, approximated by Power - Series in lg[mass]
        self.densityPlot("Envelope-H2O", xx, x_values, yy,
                         [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.5, 2, 2.5, 3, 4, 5])

    def SilicatesPlot(self):
        # Density Plot for Fe - Silicates Contour Mesh, approximated by Power - Series in lg[mass]
        xx, yy = np.meshgrid(np.logspace(np.log10(self.mmin), np.log10(self.mmax), 500),
                             np.logspace(np.log10(self.rmin), np.log10(self.rmax), 500))
        x_values = np.log10(xx)
        if self.core_contours:
            self.densityPlot("Fe-Silicates", xx, x_values, yy, [0.2, 0.4, 0.6, 0.8])
        # Density Plot for Envelope - Silicates Contour Mesh, approximated by Power - Series in lg[mass]
        self.densityPlot("Envelope-Silicates", xx, x_values, yy,
                         [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.5, 2, 2.5, 3, 4, 5])

    def FePlot(self):
        # Density Plot for Envelope - Fe Contour Mesh, approximated by Power - Series in lg[mass]
        xx, yy = np.meshgrid(np.logspace(np.log10(self.mmin), np.log10(self.mmax), 500),
                             np.logspace(np.log10(self.rmin), np.log10(self.rmax), 500))
        x_values = np.log10(xx)
        self.densityPlot("Envelope-Fe", xx, x_values, yy,
                         [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.5, 2, 2.5, 3, 4, 5])

    def densityPlot(self, envelope, xx, x_values, yy, levels):
        index = rangeFunction(envelope, x_values, yy)
        Z = applyFunction(envelope, x_values, yy)
        index = 1 * index
        valid = Z
        valid[index == 0] = np.max(Z)
        Z[index == 0] = np.min(Z) - 1
        maxv = np.max(Z)
        str_max = str(round(maxv, 2))
        if maxv >= 5:
            maxv = 5
            str_max = ">=5"
        minv = np.min(valid)
        ax = self.gui.frame_output_plot.mass_radius_plot.pcolormesh(xx, yy, Z, cmap=self.newcmp, shading="nearest",
                                                                    edgecolors=None, vmin=minv, vmax=maxv)
        cbaxes = inset_axes(self.gui.frame_output_plot.mass_radius_plot, width="3%", height="15%", loc=7)
        if self.cbl_cmap is not None:
            self.cbl_cmap.remove()
        self.cbl_cmap = plt.colorbar(ax, cax=cbaxes, ticks=[minv, maxv])
        self.cbl_cmap.ax.set_yticklabels([str(round(minv, 2)), str_max])
        self.cbl_cmap.ax.set_title("Z contours      ", fontsize=8)
        self.cbl_cmap.ax.yaxis.set_ticks_position('left')
        self.gui.frame_output_plot.mass_radius_plot.contour(xx, yy, Z, colors="#5d5857", levels=levels)

    def plotPureLine(self):
        xx = np.logspace(np.log10(self.mmin), np.log10(self.mmax), 500)
        x_values = np.log10(xx)
        yy = pureFunction("pure-Fe-metals", x_values)
        self.gui.frame_output_plot.mass_radius_plot.plot(xx, yy, "red", label="Fe-metals")
        yy = pureFunction("pure-Silicates", x_values)
        self.gui.frame_output_plot.mass_radius_plot.plot(xx, yy, "green", label="Silicates")
        yy = pureFunction("pure-high-pressure-ices", x_values)
        self.gui.frame_output_plot.mass_radius_plot.plot(xx, yy, "blue", label="Ices")

    def plotMassRadiusHydrogen(self):
        self.gui.frame_output_plot.mass_radius_plot.plot(MassRadiusDB.massradiusS03Becker[:, 0],
                                                         MassRadiusDB.massradiusS03Becker[:, 1])
        self.gui.frame_output_plot.mass_radius_plot.plot(MassRadiusDB.massradiusS04Becker[:, 0],
                                                         MassRadiusDB.massradiusS04Becker[:, 1])
        self.gui.frame_output_plot.mass_radius_plot.plot(MassRadiusDB.massradiusS05Becker[:, 0],
                                                         MassRadiusDB.massradiusS05Becker[:, 1])
        self.gui.frame_output_plot.mass_radius_plot.plot(MassRadiusDB.massradiusS06Becker[:, 0],
                                                         MassRadiusDB.massradiusS06Becker[:, 1])
        self.gui.frame_output_plot.mass_radius_plot.plot(MassRadiusDB.massradiusS07Becker[:, 0],
                                                         MassRadiusDB.massradiusS07Becker[:, 1])
        self.gui.frame_output_plot.mass_radius_plot.plot(MassRadiusDB.massradiusS08Becker[:, 0],
                                                         MassRadiusDB.massradiusS08Becker[:, 1])
        self.gui.frame_output_plot.mass_radius_plot.plot(MassRadiusDB.massradiusS09Becker[:, 0],
                                                         MassRadiusDB.massradiusS09Becker[:, 1])
        self.gui.frame_output_plot.mass_radius_plot.plot(MassRadiusDB.massradiusS10Becker[:, 0],
                                                         MassRadiusDB.massradiusS10Becker[:, 1])

    def plotMassRadiusHydrogenCentralDensity(self):
        for i in range(0, 40, 5):
            chosen_element = np.array([MassRadiusDB.massradiusS03Becker[i, :], MassRadiusDB.massradiusS04Becker[i, :],
                                       MassRadiusDB.massradiusS05Becker[i, :], MassRadiusDB.massradiusS06Becker[i, :],
                                       MassRadiusDB.massradiusS07Becker[i, :], MassRadiusDB.massradiusS08Becker[i, :],
                                       MassRadiusDB.massradiusS09Becker[i, :], MassRadiusDB.massradiusS10Becker[i, :]])
            self.gui.frame_output_plot.mass_radius_plot.plot(chosen_element[:, 0], chosen_element[:, 1])

    def plotPlanetSolarSystem(self):
        self.gui.frame_output_plot.mass_radius_plot.scatter(MassRadiusDB.Mercury[0], MassRadiusDB.Mercury[1], c="black",
                                                            s=20, marker="$m$")
        self.gui.frame_output_plot.mass_radius_plot.scatter(MassRadiusDB.Venus[0], MassRadiusDB.Venus[1], c="black",
                                                            s=20, marker="$V$")
        self.gui.frame_output_plot.mass_radius_plot.scatter(MassRadiusDB.Earth[0], MassRadiusDB.Earth[1], c="black",
                                                            s=20, marker="$E$")
        self.gui.frame_output_plot.mass_radius_plot.scatter(MassRadiusDB.Mars[0], MassRadiusDB.Mars[1], c="black", s=20,
                                                            marker="$M$")
        self.gui.frame_output_plot.mass_radius_plot.scatter(MassRadiusDB.Jupiter[0], MassRadiusDB.Jupiter[1], c="black",
                                                            s=20, marker="$J$")
        self.gui.frame_output_plot.mass_radius_plot.scatter(MassRadiusDB.Saturn[0], MassRadiusDB.Saturn[1], c="black",
                                                            s=20, marker="$S$")
        self.gui.frame_output_plot.mass_radius_plot.scatter(MassRadiusDB.Uranus[0], MassRadiusDB.Uranus[1], c="black",
                                                            s=20, marker="$U$")
        self.gui.frame_output_plot.mass_radius_plot.scatter(MassRadiusDB.Neptune[0], MassRadiusDB.Neptune[1], c="black",
                                                            s=20, marker="$N$")

    def plotPlanetTepCat(self):
        X = np.array(self.subsetdata[self.index_mass_p] * self.mass_coeff)
        Y = np.array(self.subsetdata[self.index_rad_p] * self.radius_coeff)
        deltaYm = np.array(self.subsetdata[self.index_min_rad]) * self.radius_coeff
        deltaYp = np.array(self.subsetdata[self.index_rad_max]) * self.radius_coeff
        deltaXm = np.array(self.subsetdata[self.index_mass_min]) * self.mass_coeff
        deltaXp = np.array(self.subsetdata[self.index_mass_max]) * self.mass_coeff
        d1 = deltaYm[np.logical_and(deltaXm != 0, deltaXp != 0)]
        d2 = deltaYp[np.logical_and(deltaXm != 0, deltaXp != 0)]
        d3 = deltaXm[np.logical_and(deltaXm != 0, deltaXp != 0)]
        d4 = deltaXp[np.logical_and(deltaXm != 0, deltaXp != 0)]
        x1 = X[np.logical_and(deltaXm != 0, deltaXp != 0)]
        y1 = Y[np.logical_and(deltaXm != 0, deltaXp != 0)]
        self.check = 0
        filter_arr = None
        space = "              "
        self.coeff = 1
        if self.choose_filter_map_var.get() == "Planet Temp":
            if self.check_teq:
                self.chosen_index = self.index_teq
                self.check = 1
        elif self.choose_filter_map_var.get() == "Planet Mass":
            space = "            "
            self.coeff = 317.8
            self.chosen_index = self.index_mass_p
            self.check = 1
        elif self.choose_filter_map_var.get() == "Planet Radius":
            self.chosen_index = self.index_rad_p
            self.coeff = 11.2
            self.check = 1
        elif self.choose_filter_map_var.get() == "Star Temp":
            space = "        "
            if self.check_tstar:
                self.chosen_index = self.index_tstar
                self.check = 1
        elif self.choose_filter_map_var.get() == "Star Mass":
            space = "        "
            if self.check_mass_star:
                self.chosen_index = self.index_mass_star
                self.check = 1
        elif self.choose_filter_map_var.get() == "Star Radius":
            if self.check_radius_star:
                self.chosen_index = self.index_radius_star
                self.check = 1
        elif self.choose_filter_map_var.get() == "Eccentricity":
            space = "               "
            if self.check_ecc:
                self.chosen_index = self.index_ecc
                self.check = 1
        elif self.choose_filter_map_var.get() == "Semi-major axis":
            space = "                     "
            if self.check_a_orb:
                self.chosen_index = self.index_a_orb
                self.check = 1
        elif self.choose_filter_map_var.get() == "Orbital Period":
            space = "                 "
            if self.check_p_orb:
                self.chosen_index = self.index_p_orb
                self.check = 1
        elif self.choose_filter_map_var.get() == "Age":
            space = "       "
            if self.check_age_host:
                self.chosen_index = self.index_age_host
                self.check = 1
        elif self.choose_filter_map_var.get() == "[Fe/H]":
            space = "    "
            if self.check_FeH:
                self.chosen_index = self.index_FeH
                self.check = 1
        self.min_val = 1
        self.max_val = 3000
        if self.check:
            filter_arr = np.array(self.subsetdata[self.chosen_index])
            self.max_val = np.max(filter_arr) * self.coeff
            self.min_val = np.min(filter_arr) * self.coeff
            filter_cmap = filter_arr[np.logical_and(deltaXm != 0, deltaXp != 0)]
            filter_cmap = filter_cmap * self.coeff
        else:
            filter_cmap = None
        self.sc = self.gui.frame_output_plot.mass_radius_plot.scatter(x1, y1, s=20, c=filter_cmap,
                                                                      cmap=plt.cm.get_cmap("jet"), vmin=self.min_val,
                                                                      vmax=self.max_val, edgecolors="black", zorder=100,
                                                                      label="Planets")
        if self.show_error_plot:
            self.gui.frame_output_plot.mass_radius_plot.errorbar(x1, y1, yerr=[d1, d2], xerr=[d3, d4], linestyle="None",
                                                                 zorder=101, alpha=0.5)
        if self.check:
            cbaxes = inset_axes(self.gui.frame_output_plot.mass_radius_plot, width="3%", height="15%", loc=6)
            if self.cbl_third_coord is not None:
                self.cbl_third_coord.remove()
            self.cbl_third_coord = plt.colorbar(self.sc, cax=cbaxes, ticks=[self.min_val, self.max_val])
            self.cbl_third_coord.ax.set_title(space + self.choose_filter_map_var.get(), fontsize=8)
        if self.index_mass_min != self.index_mass_max:
            x1 = X[np.logical_and(deltaXm == 0, deltaXp != 0)]
            y1 = Y[np.logical_and(deltaXm == 0, deltaXp != 0)]
            if self.check:
                filter_cmap = filter_arr[np.logical_and(deltaXm == 0, deltaXp != 0)]
                filter_cmap = filter_cmap * self.coeff
            else:
                filter_cmap = None
            d1 = deltaYm[np.logical_and(deltaXm == 0, deltaXp != 0)]
            d2 = deltaYp[np.logical_and(deltaXm == 0, deltaXp != 0)]
            d3 = deltaXm[np.logical_and(deltaXm == 0, deltaXp != 0)]
            d4 = deltaXp[np.logical_and(deltaXm == 0, deltaXp != 0)]
            if x1.size != 0:
                self.sc1 = self.gui.frame_output_plot.mass_radius_plot.scatter(x1, y1, s=20, c=filter_cmap,
                                                                               cmap=plt.cm.get_cmap("jet"),
                                                                               vmin=self.min_val, vmax=self.max_val,
                                                                               edgecolors="black", zorder=100,
                                                                               marker='v',
                                                                               label="Planets (only \u03C3+ mass)")
                if self.show_error_plot:
                    self.gui.frame_output_plot.mass_radius_plot.errorbar(x1, y1, yerr=[d1, d2], xerr=[d3, d4],
                                                                         linestyle="None", zorder=101, alpha=0.5)
            x1 = X[np.logical_and(deltaXm != 0, deltaXp == 0)]
            y1 = Y[np.logical_and(deltaXm != 0, deltaXp == 0)]
            if self.check:
                filter_cmap = filter_arr[np.logical_and(deltaXm != 0, deltaXp == 0)]
                filter_cmap = filter_cmap * self.coeff
            else:
                filter_cmap = None
            d1 = deltaYm[np.logical_and(deltaXm != 0, deltaXp == 0)]
            d2 = deltaYp[np.logical_and(deltaXm != 0, deltaXp == 0)]
            d3 = deltaXm[np.logical_and(deltaXm != 0, deltaXp == 0)]
            d4 = deltaXp[np.logical_and(deltaXm != 0, deltaXp == 0)]
            if x1.size != 0:
                self.sc2 = self.gui.frame_output_plot.mass_radius_plot.scatter(x1, y1, s=20, c=filter_cmap,
                                                                               cmap=plt.cm.get_cmap("jet"),
                                                                               vmin=self.min_val, vmax=self.max_val,
                                                                               edgecolors="black", zorder=100,
                                                                               marker='^',
                                                                               label="Planets (only \u03C3- mass)")
                if self.show_error_plot:
                    self.gui.frame_output_plot.mass_radius_plot.errorbar(x1, y1, yerr=[d1, d2], xerr=[d3, d4],
                                                                         linestyle="None", zorder=101, alpha=0.5)
        x1 = X[np.logical_and(deltaXm == 0, deltaXp == 0)]
        y1 = Y[np.logical_and(deltaXm == 0, deltaXp == 0)]
        if self.check:
            filter_cmap = filter_arr[np.logical_and(deltaXm == 0, deltaXp == 0)]
            filter_cmap = filter_cmap * self.coeff
        else:
            filter_cmap = None
        d1 = deltaYm[np.logical_and(deltaXm == 0, deltaXp == 0)]
        d2 = deltaYp[np.logical_and(deltaXm == 0, deltaXp == 0)]
        d3 = deltaXm[np.logical_and(deltaXm == 0, deltaXp == 0)]
        d4 = deltaXp[np.logical_and(deltaXm == 0, deltaXp == 0)]
        if x1.size != 0:
            self.sc3 = self.gui.frame_output_plot.mass_radius_plot.scatter(x1, y1, s=20, c=filter_cmap,
                                                                           cmap=plt.cm.get_cmap("jet"),
                                                                           vmin=self.min_val, vmax=self.max_val,
                                                                           edgecolors="black", zorder=100, marker='D',
                                                                           label="Planets (no \u03C3 mass)")
            if self.show_error_plot:
                self.gui.frame_output_plot.mass_radius_plot.errorbar(x1, y1, yerr=[d1, d2], xerr=[d3, d4],
                                                                     linestyle="None", zorder=101, alpha=0.5)
        self.annot = self.gui.frame_output_plot.mass_radius_plot.axes.annotate("", xy=(0, 0), xytext=(20, 20),
                                                                               textcoords="offset points",
                                                                               bbox=dict(boxstyle="round", fc="w"),
                                                                               arrowprops=dict(arrowstyle="->"),
                                                                               zorder=102)
        self.annot.set_visible(False)
        if self.show_all_planets_labels:
            names = np.array(self.subsetdata[0])
            for i in range(len(X)):
                if X[i] >= self.mmax / 3:
                    x = -60
                else:
                    x = 20
                if X[i] >= self.rmax / 2:
                    y = -20
                else:
                    y = 20
                self.gui.frame_output_plot.mass_radius_plot.axes.annotate(str(names[i]), xy=(X[i], Y[i]), xytext=(x, y),
                                                                          textcoords="offset points",
                                                                          bbox=dict(boxstyle="round", fc="w"),
                                                                          arrowprops=dict(arrowstyle="->"))

    def update_annot(self, ind, sc):
        pos = sc.get_offsets()[ind["ind"][0]]
        self.annot.xy = pos
        el = ind["ind"]
        self.annot.set_text(self.names[el[-1]])
        self.annot.get_bbox_patch().set_alpha(0.75)

    def hover(self, event):
        vis = self.annot.get_visible()
        if event.inaxes == self.gui.frame_output_plot.mass_radius_plot.axes:
            if self.sc is not None:
                cont, ind = self.sc.contains(event)
                if cont:
                    self.update_annot(ind, self.sc)
                    self.annot.set_visible(True)
                    self.gui.frame_output_plot.plot_combined_canvas.draw_idle()
                else:
                    if vis:
                        self.annot.set_visible(False)
                        self.gui.frame_output_plot.plot_combined_canvas.draw_idle()
            if self.sc1 is not None:
                cont, ind = self.sc1.contains(event)
                if cont:
                    self.update_annot(ind, self.sc1)
                    self.annot.set_visible(True)
                    self.gui.frame_output_plot.plot_combined_canvas.draw_idle()
                else:
                    if vis:
                        self.annot.set_visible(False)
                        self.gui.frame_output_plot.plot_combined_canvas.draw_idle()
            if self.sc2 is not None:
                cont, ind = self.sc2.contains(event)
                if cont:
                    self.update_annot(ind, self.sc2)
                    self.annot.set_visible(True)
                    self.gui.frame_output_plot.plot_combined_canvas.draw_idle()
                else:
                    if vis:
                        self.annot.set_visible(False)
                        self.gui.frame_output_plot.plot_combined_canvas.draw_idle()
            if self.sc3 is not None:
                cont, ind = self.sc3.contains(event)
                if cont:
                    self.update_annot(ind, self.sc3)
                    self.annot.set_visible(True)
                    self.gui.frame_output_plot.plot_combined_canvas.draw_idle()
                else:
                    if vis:
                        self.annot.set_visible(False)
                        self.gui.frame_output_plot.plot_combined_canvas.draw_idle()

    def plotPlanetInput(self):
        tempSubData = self.subsetdata.tail(self.num_new_planets)
        X = np.array(tempSubData[self.index_mass_p] * self.mass_coeff)
        Y = np.array(tempSubData[self.index_rad_p] * self.radius_coeff)
        deltaYm = np.array(tempSubData[self.index_min_rad]) * self.radius_coeff
        deltaYp = np.array(tempSubData[self.index_rad_max]) * self.radius_coeff
        deltaXm = np.array(tempSubData[self.index_mass_min]) * self.radius_coeff
        deltaXp = np.array(tempSubData[self.index_mass_max]) * self.radius_coeff
        d1 = deltaYm[np.logical_and(deltaXm != 0, deltaXp != 0)]
        d2 = deltaYp[np.logical_and(deltaXm != 0, deltaXp != 0)]
        d3 = deltaXm[np.logical_and(deltaXm != 0, deltaXp != 0)]
        d4 = deltaXp[np.logical_and(deltaXm != 0, deltaXp != 0)]

        if self.check:
            filter_arr = np.array(tempSubData[self.chosen_index])
            filter_cmap = filter_arr[np.logical_and(deltaXm != 0, deltaXp != 0)]
            filter_cmap = filter_cmap * self.coeff
        else:
            filter_arr = None
            filter_cmap = None
        x1 = X[np.logical_and(deltaXm != 0, deltaXp != 0)]
        y1 = Y[np.logical_and(deltaXm != 0, deltaXp != 0)]
        names = np.array(tempSubData[0])
        self.gui.frame_output_plot.mass_radius_plot.scatter(x1, y1, edgecolors="black", s=100, c=filter_cmap,
                                                            cmap=plt.cm.get_cmap("jet"), vmin=self.min_val,
                                                            vmax=self.max_val, zorder=103)
        if self.show_error_plot:
            self.gui.frame_output_plot.mass_radius_plot.errorbar(x1, y1, yerr=[d1, d2], xerr=[d3, d4], linestyle="None",
                                                                 zorder=104, alpha=0.5)
        if self.index_mass_min != self.index_mass_max:
            x1 = X[np.logical_and(deltaXm == 0, deltaXp != 0)]
            y1 = Y[np.logical_and(deltaXm == 0, deltaXp != 0)]
            if self.check:
                filter_cmap = filter_arr[np.logical_and(deltaXm == 0, deltaXp != 0)]
                filter_cmap = filter_cmap * self.coeff
            else:
                filter_cmap = None
            d1 = deltaYm[np.logical_and(deltaXm == 0, deltaXp != 0)]
            d2 = deltaYp[np.logical_and(deltaXm == 0, deltaXp != 0)]
            d3 = deltaXm[np.logical_and(deltaXm == 0, deltaXp != 0)]
            d4 = deltaXp[np.logical_and(deltaXm == 0, deltaXp != 0)]
            if x1.size != 0:
                self.gui.frame_output_plot.mass_radius_plot.scatter(x1, y1, s=20, c=filter_cmap,
                                                                    cmap=plt.cm.get_cmap("jet"), vmin=self.min_val,
                                                                    vmax=self.max_val, edgecolors="black", zorder=100,
                                                                    marker='v')
                if self.show_error_plot:
                    self.gui.frame_output_plot.mass_radius_plot.errorbar(x1, y1, yerr=[d1, d2], xerr=[d3, d4],
                                                                         linestyle="None", zorder=101, alpha=0.5)
            x1 = X[np.logical_and(deltaXm != 0, deltaXp == 0)]
            y1 = Y[np.logical_and(deltaXm != 0, deltaXp == 0)]
            if self.check:
                filter_cmap = filter_arr[np.logical_and(deltaXm != 0, deltaXp == 0)]
                filter_cmap = filter_cmap * self.coeff
            else:
                filter_cmap = None
            d1 = deltaYm[np.logical_and(deltaXm != 0, deltaXp == 0)]
            d2 = deltaYp[np.logical_and(deltaXm != 0, deltaXp == 0)]
            d3 = deltaXm[np.logical_and(deltaXm != 0, deltaXp == 0)]
            d4 = deltaXp[np.logical_and(deltaXm != 0, deltaXp == 0)]
            if x1.size != 0:
                self.gui.frame_output_plot.mass_radius_plot.scatter(x1, y1, s=20, c=filter_cmap,
                                                                    cmap=plt.cm.get_cmap("jet"), vmin=self.min_val,
                                                                    vmax=max, edgecolors="black", zorder=100,
                                                                    marker='^')
                if self.show_error_plot:
                    self.gui.frame_output_plot.mass_radius_plot.errorbar(x1, y1, yerr=[d1, d2], xerr=[d3, d4],
                                                                         linestyle="None", zorder=101, alpha=0.5)
        x1 = X[np.logical_and(deltaXm == 0, deltaXp == 0)]
        y1 = Y[np.logical_and(deltaXm == 0, deltaXp == 0)]
        if self.check:
            filter_cmap = filter_arr[np.logical_and(deltaXm == 0, deltaXp == 0)]
            filter_cmap = filter_cmap * self.coeff
        else:
            filter_cmap = None
        d1 = deltaYm[np.logical_and(deltaXm == 0, deltaXp == 0)]
        d2 = deltaYp[np.logical_and(deltaXm == 0, deltaXp == 0)]
        d3 = deltaXm[np.logical_and(deltaXm == 0, deltaXp == 0)]
        d4 = deltaXp[np.logical_and(deltaXm == 0, deltaXp == 0)]
        if x1.size != 0:
            self.gui.frame_output_plot.mass_radius_plot.scatter(x1, y1, s=20, c=filter_cmap,
                                                                cmap=plt.cm.get_cmap("jet"), vmin=self.min_val,
                                                                vmax=self.max_val, edgecolors="black", zorder=100,
                                                                marker='D')
            if self.show_error_plot:
                self.gui.frame_output_plot.mass_radius_plot.errorbar(x1, y1, yerr=[d1, d2], xerr=[d3, d4],
                                                                     linestyle="None", zorder=101, alpha=0.5)
        if self.add2:
            for i in range(self.num_new_planets):
                if X[i] >= self.mmax / 3:
                    x = -60
                else:
                    x = 20
                if X[i] >= self.rmax / 2:
                    y = -20
                else:
                    y = 20
                self.gui.frame_output_plot.mass_radius_plot.axes.annotate(str(names[i]), xy=(X[i], Y[i]), xytext=(x, y),
                                                                          textcoords="offset points",
                                                                          bbox=dict(boxstyle="round", fc="w"),
                                                                          arrowprops=dict(arrowstyle="->"))

    def executeRoutine(self, mass, radius):
        self.dataAcquisition(mass, radius)
        if self.subsetdata.empty:
            msgbox.showerror(title="ERROR", message="No planet found with these boundaries")
            return
        self.plotHistogramMass()
        self.plotHistogramRadius()
        self.plotHistogramZeta()
        self.plotMassRadius()
