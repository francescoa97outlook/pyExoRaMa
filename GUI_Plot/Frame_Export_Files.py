import os
import tkinter as tk


class Frame_Export_Files:
    gui = None
    frame_export_files = None
    label = None
    export_mass_radius_plot_pdf = None
    export_mass_radius_plot_eps = None
    export_mass_radius_plot_jpg = None
    export_selected_planets_table = None
    export_all_planets_table = None
    export_histogram_planet_radius_pdf = None
    export_histogram_planet_radius_eps = None
    export_histogram_planet_radius_jpg = None
    export_histogram_planet_mass_pdf = None
    export_histogram_planet_mass_eps = None
    export_histogram_planet_mass_jpg = None
    export_histogram_zeta_pdf = None
    export_histogram_zeta_eps = None
    export_histogram_zeta_jpg = None
    export_combined_pdf = None
    export_combined_eps = None
    export_combined_jpg = None
    padding_x = None
    padding_y = None
    dpi_label = None
    dpi_entry = None

    def __init__(self, window, gui):
        self.gui = gui
        self.padding_x = 70
        self.padding_y = 40
        self.frame_export_files = tk.Frame(window, highlightbackground="black", highlightthickness=1, padx=5, pady=2)
        self.label = tk.Label(master=self.frame_export_files, text='Export mass-radius plot: ', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(column=0, row=0)
        self.export_mass_radius_plot_pdf = tk.Button(master=self.frame_export_files, text=" pdf ", bg="red", font=('Sans', '8', 'bold'), command=self.exportMassRadiusPlotPdf)
        self.export_mass_radius_plot_pdf.grid(column=1, row=0)
        self.export_mass_radius_plot_eps = tk.Button(master=self.frame_export_files, text=" eps ", bg="yellow", font=('Sans', '8', 'bold'), command=self.exportMassRadiusPlotEps)
        self.export_mass_radius_plot_eps.grid(column=2, row=0)
        self.export_mass_radius_plot_jpg = tk.Button(master=self.frame_export_files, text=" jpg ", bg="cyan", font=('Sans', '8', 'bold'), command=self.exportMassRadiusPlotJpg)
        self.export_mass_radius_plot_jpg.grid(column=3, row=0)
        self.label = tk.Label(master=self.frame_export_files, text='Export histogram of planet radius: ', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(column=0, row=1)
        self.export_histogram_planet_radius_pdf = tk.Button(master=self.frame_export_files, text=" pdf ", bg="red", font=('Sans', '8', 'bold'), command=self.exportHistogramPlanetRadiusPdf)
        self.export_histogram_planet_radius_pdf.grid(column=1, row=1)
        self.export_histogram_planet_radius_eps = tk.Button(master=self.frame_export_files, text=" eps ", bg="yellow", font=('Sans', '8', 'bold'), command=self.exportHistogramPlanetRadiusEps)
        self.export_histogram_planet_radius_eps.grid(column=2, row=1)
        self.export_histogram_planet_radius_jpg = tk.Button(master=self.frame_export_files, text=" jpg ", bg="cyan", font=('Sans', '8', 'bold'), command=self.exportHistogramPlanetRadiusJpg)
        self.export_histogram_planet_radius_jpg.grid(column=3, row=1)
        self.label = tk.Label(master=self.frame_export_files, text='Export histogram of planet mass: ', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(column=0, row=2)
        self.export_histogram_planet_mass_pdf = tk.Button(master=self.frame_export_files, text=" pdf ", bg="red", font=('Sans', '8', 'bold'), command=self.exportHistogramPlanetMassPdf)
        self.export_histogram_planet_mass_pdf.grid(column=1, row=2)
        self.export_histogram_planet_mass_eps = tk.Button(master=self.frame_export_files, text=" eps ", bg="yellow", font=('Sans', '8', 'bold'), command=self.exportHistogramPlanetMassEps)
        self.export_histogram_planet_mass_eps.grid(column=2, row=2)
        self.export_histogram_planet_mass_jpg = tk.Button(master=self.frame_export_files, text=" jpg ", bg="cyan", font=('Sans', '8', 'bold'), command=self.exportHistogramPlanetMassJpg)
        self.export_histogram_planet_mass_jpg.grid(column=3, row=2)
        self.label = tk.Label(master=self.frame_export_files, text='Export histogram of ζ: ', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(column=0, row=3)
        self.export_histogram_zeta_pdf = tk.Button(master=self.frame_export_files, text=" pdf ", bg="red", font=('Sans', '8', 'bold'), command=self.exportHistogramZetaPdf)
        self.export_histogram_zeta_pdf.grid(column=1, row=3)
        self.export_histogram_zeta_eps = tk.Button(master=self.frame_export_files, text=" eps ", bg="yellow", font=('Sans', '8', 'bold'), command=self.exportHistogramZetaEps)
        self.export_histogram_zeta_eps.grid(column=2, row=3)
        self.export_histogram_zeta_jpg = tk.Button(master=self.frame_export_files, text=" jpg ", bg="cyan", font=('Sans', '8', 'bold'), command=self.exportHistogramZetaJpg)
        self.export_histogram_zeta_jpg.grid(column=3, row=3)
        self.label = tk.Label(master=self.frame_export_files, text='Export combined plot: ', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(column=0, row=4)
        self.export_combined_pdf = tk.Button(master=self.frame_export_files, text=" pdf ", bg="red", font=('Sans', '8', 'bold'), command=self.exportCombinedPlotPdf)
        self.export_combined_pdf.grid(column=1, row=4)
        self.export_combined_eps = tk.Button(master=self.frame_export_files, text=" eps ", bg="yellow", font=('Sans', '8', 'bold'), command=self.exportCombinedPlotEps)
        self.export_combined_eps.grid(column=2, row=4)
        self.export_combined_jpg = tk.Button(master=self.frame_export_files, text=" jpg ", bg="cyan", font=('Sans', '8', 'bold'), command=self.exportCombinedPlotJpg)
        self.export_combined_jpg.grid(column=3, row=4)
        self.dpi_label = tk.Label(master=self.frame_export_files, text='DPI ', fg="blue", font=('Sans', '8', 'bold'))
        self.dpi_label.grid(column=5, row=0, rowspan=6)
        self.dpi_entry = tk.Entry(master=self.frame_export_files, width=8)
        self.dpi_entry.grid(column=6, row=0, rowspan=6)
        self.dpi_entry.insert(-1, "300")
        self.label = tk.Label(master=self.frame_export_files, text='Export planet table: ', fg="blue", font=('Sans', '8', 'bold'))
        self.label.grid(column=0, row=5)
        self.export_selected_planets_table = tk.Button(master=self.frame_export_files, text=" Selected Planets ", bg="#ffff66", font=('Sans', '8', 'bold'), command=self.exportSelectedPlanets)
        self.export_selected_planets_table.grid(column=1, row=5, columnspan=2)
        self.export_all_planets_table = tk.Button(master=self.frame_export_files, text=" All Planets ", bg="#6600cc", font=('Sans', '8', 'bold'), command=self.exportAllPlanets)
        self.export_all_planets_table.grid(column=3, row=5)
        self.frame_export_files.pack(padx=3, pady=3)

    def exportMassRadiusPlotPdf(self):
        bbox = self.gui.frame_output_plot.mass_radius_plot.get_tightbbox(self.gui.frame_output_plot.plot_combined_fig.canvas.get_renderer(), call_axes_locator=True)
        self.gui.frame_output_plot.plot_combined_fig.savefig('Output' + os.sep + 'MassRadiusPlot.pdf', format='pdf', bbox_inches=bbox.transformed(self.gui.frame_output_plot.plot_combined_fig.dpi_scale_trans.inverted()), dpi=int(self.dpi_entry.get()))

    def exportMassRadiusPlotEps(self):
        bbox = self.gui.frame_output_plot.mass_radius_plot.get_tightbbox(self.gui.frame_output_plot.plot_combined_fig.canvas.get_renderer(), call_axes_locator=True)
        self.gui.frame_output_plot.plot_combined_fig.savefig('Output' + os.sep + 'MassRadiusPlot.eps', format='eps', bbox_inches=bbox.transformed(self.gui.frame_output_plot.plot_combined_fig.dpi_scale_trans.inverted()), dpi=int(self.dpi_entry.get()))

    def exportMassRadiusPlotJpg(self):
        bbox = self.gui.frame_output_plot.mass_radius_plot.get_tightbbox(self.gui.frame_output_plot.plot_combined_fig.canvas.get_renderer(), call_axes_locator=True)
        self.gui.frame_output_plot.plot_combined_fig.savefig('Output' + os.sep + 'MassRadiusPlot.jpg', format='jpg', bbox_inches=bbox.transformed(self.gui.frame_output_plot.plot_combined_fig.dpi_scale_trans.inverted()), dpi=int(self.dpi_entry.get()))

    def exportHistogramPlanetRadiusPdf(self):
        bbox = self.gui.frame_output_plot.histogram_radius.get_tightbbox(self.gui.frame_output_plot.plot_combined_fig.canvas.get_renderer(), call_axes_locator=True)
        self.gui.frame_output_plot.plot_combined_fig.savefig('Output' + os.sep + 'HistogramRadius.pdf', format='pdf', bbox_inches=bbox.transformed(self.gui.frame_output_plot.plot_combined_fig.dpi_scale_trans.inverted()), dpi=int(self.dpi_entry.get()))

    def exportHistogramPlanetRadiusEps(self):
        bbox = self.gui.frame_output_plot.histogram_radius.get_tightbbox(self.gui.frame_output_plot.plot_combined_fig.canvas.get_renderer(), call_axes_locator=True)
        self.gui.frame_output_plot.plot_combined_fig.savefig('Output' + os.sep + 'HistogramRadius.eps', format='eps', bbox_inches=bbox.transformed(self.gui.frame_output_plot.plot_combined_fig.dpi_scale_trans.inverted()), dpi=int(self.dpi_entry.get()))

    def exportHistogramPlanetRadiusJpg(self):
        bbox = self.gui.frame_output_plot.histogram_radius.get_tightbbox(self.gui.frame_output_plot.plot_combined_fig.canvas.get_renderer(), call_axes_locator=True)
        self.gui.frame_output_plot.plot_combined_fig.savefig('Output' + os.sep + 'HistogramRadius.jpg', format='jpg', bbox_inches=bbox.transformed(self.gui.frame_output_plot.plot_combined_fig.dpi_scale_trans.inverted()), dpi=int(self.dpi_entry.get()))

    def exportHistogramPlanetMassPdf(self):
        bbox = self.gui.frame_output_plot.histogram_mass.get_tightbbox(self.gui.frame_output_plot.plot_combined_fig.canvas.get_renderer(), call_axes_locator=True)
        self.gui.frame_output_plot.plot_combined_fig.savefig('Output' + os.sep + 'HistogramMass.pdf', format='pdf', bbox_inches=bbox.transformed(self.gui.frame_output_plot.plot_combined_fig.dpi_scale_trans.inverted()), dpi=int(self.dpi_entry.get()))

    def exportHistogramPlanetMassEps(self):
        bbox = self.gui.frame_output_plot.histogram_mass.get_tightbbox(self.gui.frame_output_plot.plot_combined_fig.canvas.get_renderer(), call_axes_locator=True)
        self.gui.frame_output_plot.plot_combined_fig.savefig('Output' + os.sep + 'HistogramMass.eps', format='eps', bbox_inches=bbox.transformed(self.gui.frame_output_plot.plot_combined_fig.dpi_scale_trans.inverted()), dpi=int(self.dpi_entry.get()))

    def exportHistogramPlanetMassJpg(self):
        bbox = self.gui.frame_output_plot.histogram_mass.get_tightbbox(self.gui.frame_output_plot.plot_combined_fig.canvas.get_renderer(), call_axes_locator=True)
        self.gui.frame_output_plot.plot_combined_fig.savefig('Output' + os.sep + 'HistogramMass.jpg', format='jpg', bbox_inches=bbox.transformed(self.gui.frame_output_plot.plot_combined_fig.dpi_scale_trans.inverted()), dpi=int(self.dpi_entry.get()))

    def exportHistogramZetaPdf(self):
        bbox = self.gui.frame_output_plot.histogram_zeta.get_tightbbox(self.gui.frame_output_plot.plot_combined_fig.canvas.get_renderer(), call_axes_locator=True)
        self.gui.frame_output_plot.plot_combined_fig.savefig('Output' + os.sep + 'HistogramZeta.pdf', format='pdf', bbox_inches=bbox.transformed(self.gui.frame_output_plot.plot_combined_fig.dpi_scale_trans.inverted()), dpi=int(self.dpi_entry.get()))

    def exportHistogramZetaEps(self):
        bbox = self.gui.frame_output_plot.histogram_zeta.get_tightbbox(self.gui.frame_output_plot.plot_combined_fig.canvas.get_renderer(), call_axes_locator=True)
        self.gui.frame_output_plot.plot_combined_fig.savefig('Output' + os.sep + 'HistogramZeta.eps', format='eps', bbox_inches=bbox.transformed(self.gui.frame_output_plot.plot_combined_fig.dpi_scale_trans.inverted()), dpi=int(self.dpi_entry.get()))

    def exportHistogramZetaJpg(self):
        bbox = self.gui.frame_output_plot.histogram_zeta.get_tightbbox(self.gui.frame_output_plot.plot_combined_fig.canvas.get_renderer(), call_axes_locator=True)
        self.gui.frame_output_plot.plot_combined_fig.savefig('Output' + os.sep + 'HistogramZeta.jpg', format='jpg', bbox_inches=bbox.transformed(self.gui.frame_output_plot.plot_combined_fig.dpi_scale_trans.inverted()), dpi=int(self.dpi_entry.get()))

    def exportCombinedPlotPdf(self):
        self.gui.frame_output_plot.plot_combined_fig.savefig('Output' + os.sep + 'Combined.pdf', format='pdf', dpi=int(self.dpi_entry.get()))

    def exportCombinedPlotEps(self):
        self.gui.frame_output_plot.plot_combined_fig.savefig('Output' + os.sep + 'Combined.eps', format='eps', dpi=int(self.dpi_entry.get()))

    def exportCombinedPlotJpg(self):
        self.gui.frame_output_plot.plot_combined_fig.savefig('Output' + os.sep + 'Combined.jpg', format='jpg', dpi=int(self.dpi_entry.get()))

    def exportSelectedPlanets(self):
        if self.gui.frame_input_master.frame_run_plot.subsetdata is not None:
            self.gui.frame_input_master.frame_run_plot.subsetdata.to_csv("Output" + os.sep + "selected_planet.csv")

    def exportAllPlanets(self):
        self.gui.frame_input_master.frame_run_plot.data0.to_csv("Output" + os.sep + "all_planet.csv")
