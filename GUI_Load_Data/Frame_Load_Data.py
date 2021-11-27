import tkinter as tk
from tkinter import messagebox as msgbox
import pandas as pd
import webbrowser
from tkinter.filedialog import askopenfilename


def infoPandasDocFunc():
    webbrowser.open('https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html', new=2)


class Frame_Load_Data:
    gui = None
    frame_load_Data = None
    label = None
    text = None
    loadData = None
    data0 = None
    skiprow = None
    delim_whitespace_var = None
    delim_whitespace = None
    infoPandasDoc = None
    openFile = None

    def __init__(self, window, gui):
        self.gui = gui
        self.frame_load_Data = tk.Frame(window, highlightbackground="black", highlightthickness=1, padx=5, pady=2)

        self.label = tk.Label(master=self.frame_load_Data, text='Insert Url or Local path: ', fg="blue", font=('Sans', '13', 'bold'))
        self.label.grid(column=0, row=0)

        self.text = tk.Text(master=self.frame_load_Data, width=75, height=1)
        self.text.grid(column=1, row=0, columnspan=8)
        self.text.insert(tk.END, "https://www.astro.keele.ac.uk/jkt/tepcat/allplanets-ascii.txt")

        self.openFile = tk.Button(master=self.frame_load_Data, text=" Open File ", bg="orange", font=('Sans', '13', 'bold'), command=self.openFileFunc)
        self.openFile.grid(column=9, row=0)

        self.label = tk.Label(master=self.frame_load_Data, text=' Skiprow * ', fg="blue", font=('Sans', '13', 'bold'))
        self.label.grid(column=0, row=1)

        self.skiprow = tk.Entry(master=self.frame_load_Data, width=10)
        self.skiprow.grid(column=1, row=1)
        self.skiprow.insert(tk.END, "1")

        self.delim_whitespace_var = tk.BooleanVar()
        self.delim_whitespace = tk.Checkbutton(master=self.frame_load_Data, text=" Delim_whitespace ** ", variable=self.delim_whitespace_var, fg="#cc3300", font=('Sans', '13', 'bold'))
        self.delim_whitespace_var.set(True)
        self.delim_whitespace.grid(column=5, row=1)

        self.label = tk.Label(master=self.frame_load_Data, text=' Delimiter *** ', fg="blue", font=('Sans', '13', 'bold'))
        self.label.grid(column=8, row=1)

        self.delimiter = tk.Entry(master=self.frame_load_Data, width=10)
        self.delimiter.grid(column=9, row=1)
        self.delimiter.insert(tk.END, "None")

        self.loadData = tk.Button(master=self.frame_load_Data, width=30, height=2, text=" Load Data ", bg="#00ff00", font=('Sans', '13', 'bold'), command=self.loadDataFunc)
        self.loadData.grid(column=0, columnspan=10, row=2)

        self.label = tk.Label(master=self.frame_load_Data,
                              text='NB: header is automatically skipped\n* In some cases (like Tepcat catalogue) skiprow should remain at least 1 to avoid the reading of merged columns (or column names)\n** Check if your table uses space as delimiter\n*** The columns delimiter\n\nClick the button below for more information',
                              fg="red", font=('Sans', '13', 'bold'))
        self.label.grid(column=0, row=3, columnspan=10)

        self.infoPandasDoc = tk.Button(master=self.frame_load_Data, text=" Pandas Documentation read_csv ", bg="yellow", width=30, font=('Sans', '13', 'bold'), command=infoPandasDocFunc)
        self.infoPandasDoc.grid(column=2, row=4, columnspan=5)

        self.frame_load_Data.pack(padx=3, pady=3)

    def loadDataFunc(self):
        try:
            text = self.text.get("1.0", tk.END)
            text = text.replace("\n", "")
            if self.delim_whitespace_var.get() or self.delimiter == "None":
                delimiter = None
            else:
                delimiter = self.delimiter.get()
            self.data0 = pd.read_csv(text, skiprows=int(self.skiprow.get()), delimiter=delimiter, delim_whitespace=self.delim_whitespace_var.get(), header=None)
            for child in self.gui.frame_constrains.frame_constrains.winfo_children():
                child.configure(state='normal')
        except:
            msgbox.showerror(title="ERROR", message="Unable to load Data, check your the path/URL or the connection")

    def openFileFunc(self):
        filename = askopenfilename(initialdir="Data")
        if filename != '':
            self.text.delete('1.0', tk.END)
            self.text.insert(tk.END, filename)
