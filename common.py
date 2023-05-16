import sqlite3
import tkinter


import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import date


class GUI:
    def __init__(self, title, configure, geometry):
        self.win= tkinter.Tk()
        self.win.title(title)
        self.win.configure(bg=configure)
        self.win.geometry(geometry)
        #self.win.resizable(False, False)

    def text(self, texto, fila, columna):
        label= tkinter.Label(self.win, text=texto, font=("Helvetica", 15), fg="#4D4D4D") ##F2F2F2 #
        label.configure(bg="#D49FFF")
        label.pack()
        #label.grid(row = fila, column= columna)

    #Aquí se define la funcion del boton
    def button(self, texto, fila, columna):
        add_event= tk.Button(text=texto, command= e_window)
        #add_event.grid(row= fila, column= columna)
        add_event.pack()
        
    #Aquí se define la función de caja de entrada
    def entry_box(self, frame, fila, columna, padx):
        my_entry= Entry(frame) #Aqui Roberto cambio el self.win por frame
        #my_entry.insert(0, "tu mamá 🍕")
        #my_entry.pack()
        my_entry.grid(row=fila, column=columna, padx=padx)

    def show(self):
        self.win.mainloop()


def e_window():
    
    
    from EventWindowGUI import EventWindow
    event_window = EventWindow()
    event_window.logging()
    event_window.check_dateid()
    event_window.event()
    #event_window.get_input()
    event_window.checkbox()
    event_window.solution()
    #event_window.show()
