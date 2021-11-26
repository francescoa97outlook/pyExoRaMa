import tkinter as tk

import GUI_Load_Data.Gui_Data


class Frame_Import_Data:
    gui = None
    frame_import_Data = None
    loadData = None

    def __init__(self, window, gui):
        self.gui = gui
        self.frame_import_Data = tk.Frame(window, highlightbackground="black", highlightthickness=1, padx=5, pady=2)
        self.loadData = tk.Button(master=self.frame_import_Data, text=" Load Data ", bg="#00ff00", width=40,  font=('Sans', '9', 'bold'), command=self.loadDataFunc)
        self.loadData.grid(column=0, row=0)
        self.frame_import_Data.pack(padx=3, pady=3)

    def loadDataFunc(self):
        self.gui.window.destroy()
        gui = GUI_Load_Data.Gui_Data.GUI_Data()
        gui.window.mainloop()
