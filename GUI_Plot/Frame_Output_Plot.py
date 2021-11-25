import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Frame_Output_Plot:
    gui = None
    frame_width = 950
    frame_height = 940
    frame_master = None
    frame_histogram_mass = None
    plot_combined_fig = None
    plot_combined_canvas = None
    grid = None
    histogram_mass = None
    histogram_zeta = None
    mass_radius_plot = None
    histogram_radius = None

    def __init__(self, window, gui):
        self.gui = gui
        self.frame_master = tk.Frame(window, width=self.frame_width, height=self.frame_height, highlightbackground="black", highlightthickness=1, padx=5, pady=2)
        self.plot_combined_fig = plt.Figure()
        self.grid = plt.GridSpec(20, 20)
        self.grid.update(wspace=0.025, hspace=0.05)
        self.histogram_mass = self.plot_combined_fig.add_subplot(self.grid[0:5, 0:14])
        self.histogram_zeta = self.plot_combined_fig.add_subplot(self.grid[0:5, 15:20])
        self.mass_radius_plot = self.plot_combined_fig.add_subplot(self.grid[6:20, 0:14])
        self.histogram_radius = self.plot_combined_fig.add_subplot(self.grid[6:20, 15:20])
        self.plot_combined_canvas = FigureCanvasTkAgg(self.plot_combined_fig, self.frame_master)
        self.plot_combined_canvas.get_tk_widget().pack(fill=tk.BOTH, expand='True')
        self.frame_master.pack_propagate(0)
        self.frame_master.pack(padx=3, pady=3, fill='both', side="right", expand='True')
