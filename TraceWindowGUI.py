import tkinter
#import sqlite3

import tkinter as tk
from tkinter import *
from tkinter import ttk

class traceWindow():
    
    def __init__(self,sel):
        self.win= tkinter.Tk()
        self.win.title("BITACORA DE SISTEMAS                                                                                                                                                                                                     Developed by Ing. Joel Carbajal Muñoz")
        self.win.configure(bg="#D49FFF")
        self.win.geometry("1100x300")
        print(sel)
        self.win.mainloop()

#traceWindow=traceWindow()