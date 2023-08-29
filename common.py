import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk


class GUI:
    def __init__(self, title, configure, geometry):
        self.win= tkinter.Tk()
        self.win.title(title)
        self.win.configure(bg=configure)
        self.win.geometry(geometry)
    
    def show(self):
        self.win.mainloop()



