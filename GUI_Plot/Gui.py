import tkinter as tk

from GUI_Plot import Frame_Input_Data
from GUI_Plot import Frame_Output_Plot


class GUI_Planet:
    # Window
    window = None
    # Master Inputs
    frame_input_master = None
    # Output Plot
    frame_output_plot = None

    def __init__(self, data0, mass_coeff, radius_coeff, age_coeff, index_ecc, index_FeH, index_tstar, index_mass_max, index_p_orb, index_a_orb, index_teq, index_mass_min, index_min_rad, index_mass_star, index_radius_star, index_rad_max, index_rad_p, index_mass_p, index_age_host, check_age_host, check_ecc, check_FeH, check_tstar, check_p_orb, check_a_orb, check_teq, check_mass_star, check_radius_star):
        # Window
        self.window = tk.Tk()
        self.window.geometry("1850x1000+10+10")
        self.window.title("Tool for statistical studies based on the exoplanet mass-radius diagram")
        self.window.resizable(False, False)
        # Planet Inputs
        self.frame_input_master = Frame_Input_Data.Frame_Input_Data(self.window, self, data0, mass_coeff, radius_coeff, age_coeff, index_ecc, index_FeH, index_tstar, index_mass_max, index_p_orb, index_a_orb, index_teq, index_mass_min, index_min_rad, index_mass_star, index_radius_star, index_rad_max, index_rad_p, index_mass_p, index_age_host, check_age_host, check_ecc, check_FeH, check_tstar, check_p_orb, check_a_orb, check_teq, check_mass_star, check_radius_star)
        # Output Plot
        self.frame_output_plot = Frame_Output_Plot.Frame_Output_Plot(self.window, self)
