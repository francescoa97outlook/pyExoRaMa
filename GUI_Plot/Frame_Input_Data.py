import tkinter as tk

from GUI_Plot import Frame_Import_Data
from GUI_Plot import Frame_Envelope_Plot
from GUI_Plot import Frame_Export_Files
from GUI_Plot import Frame_Input_Planets
from GUI_Plot import Frame_New_Planet
from GUI_Plot import Frame_Pure_Hydrogen
from GUI_Plot import Frame_Run_Plot
from GUI_Plot import Frame_Scale_Plot
from GUI_Plot import Frame_Histogram_Info


class Frame_Input_Data:
    window = None
    frame_width = None
    frame_height = None
    # Input Master Frame
    frame_input_master = None
    # Planet Inputs
    frame_input_planet = None
    # Run Plot
    frame_run_plot = None
    # Scale Plot
    frame_scale_plot = None
    # Histogram Info
    frame_histogram_info = None
    # Envelope Plot
    frame_envelope_plot = None
    # Pure Hydrogen
    frame_pure_hydrogen = None
    # New Planet
    frame_new_planet = None
    # Export File
    frame_export_file = None
    # Import Data
    frame_import_Data = None

    def __init__(self, window, gui, data0, mass_coeff, radius_coeff, age_coeff, index_ecc, index_FeH, index_tstar, index_mass_max, index_p_orb, index_a_orb, index_teq, index_mass_min, index_min_rad, index_mass_star, index_radius_star, index_rad_max, index_rad_p, index_mass_p, index_age_host, check_age_host, check_ecc, check_FeH, check_tstar, check_p_orb, check_a_orb, check_teq, check_mass_star, check_radius_star):
        self.window = gui
        self.frame_width = 700
        self.frame_height = 900
        # Input Master Frame
        self.frame_input_master = tk.Frame(window, width=self.frame_width, height=self.frame_height, highlightbackground="black", highlightthickness=1, padx=5, pady=2)
        # Import Data
        self.frame_import_Data = Frame_Import_Data.Frame_Import_Data(self.frame_input_master, gui)
        # Planet Inputs
        self.frame_input_planet = Frame_Input_Planets.Frame_Input_Planets(self.frame_input_master, gui, age_coeff, check_age_host, check_ecc, check_FeH, check_tstar, check_p_orb, check_a_orb, check_teq, check_mass_star, check_radius_star)
        # Run Plot
        self.frame_run_plot = Frame_Run_Plot.Frame_Run_Plot(self.frame_input_master, gui, data0, mass_coeff, radius_coeff, index_ecc, index_FeH, index_tstar, index_mass_max, index_p_orb, index_a_orb, index_teq, index_mass_min, index_min_rad, index_mass_star, index_radius_star, index_rad_max, index_rad_p, index_mass_p, index_age_host, check_age_host, check_ecc, check_FeH, check_tstar, check_p_orb, check_a_orb, check_teq, check_mass_star, check_radius_star)
        # Scale Plot
        self.frame_scale_plot = Frame_Scale_Plot.Frame_Scale_Plot(self.frame_input_master, gui)
        # Histogram Info
        self.frame_histogram_info = Frame_Histogram_Info.Frame_Histogram_Info(self.frame_input_master, gui)
        # Envelope Plot
        self.frame_envelope_plot = Frame_Envelope_Plot.Frame_Envelope_Plot(self.frame_input_master, gui)
        # Pure Hydrogen
        self.frame_pure_hydrogen = Frame_Pure_Hydrogen.Frame_Pure_Hydrogen(self.frame_input_master, gui)
        # New Planet
        self.frame_new_planet = Frame_New_Planet.Frame_New_Planet(self.frame_input_master, gui, check_age_host, check_ecc, check_FeH, check_tstar, check_p_orb, check_a_orb, check_teq, check_mass_star, check_radius_star)
        # Export File
        self.frame_export_file = Frame_Export_Files.Frame_Export_Files(self.frame_input_master, gui)
        # PACK
        self.frame_input_master.pack_propagate(0)
        self.frame_input_master.pack(padx=3, pady=3, fill='both', side='left', expand='True')
