import tkinter
#import sqlite3

import tkinter as tk
from tkinter import *
from tkinter import ttk

class traceWindow():
    
    def __init__(self, selection):
        self.win= tkinter.Tk()
        self.win.title("SEGUIMIENTO")
        self.win.configure(bg="#D49FFF")
        self.win.geometry("500x500")
        self.put_label(selection)
        print(selection)
        self.win.mainloop()
    
    def put_label(self, selection):
        
        label= tk.Label(self.win, text=selection[0], font=("Helvetica", 15), fg="#4D4D4D")
        label.configure(bg="#D49FFF")
        label.pack()

        label1= tk.Label(self.win, text=selection[1], font=("Helvetica", 15), fg="#4D4D4D")
        label1.configure(bg="#D49FFF")
        label1.pack()

        label2= tk.Label(self.win, text=selection[2], font=("Helvetica", 15), fg="#4D4D4D")
        label2.configure(bg="#D49FFF")
        label2.pack()


#traceWindow=traceWindow()