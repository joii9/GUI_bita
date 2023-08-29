import tkinter
import sqlite3

import tkinter as tk
from tkinter import *
from tkinter import ttk

from common import GUI


class MainWindow(GUI):

    def __init__(self):

        title = "BITACORA DE SISTEMAS"
        configure = "#D49FFF"
        geometry = "1250x600" #Originalmente tenia un valor de x300 pero para poder visualizar 10 entradas en la db lo modifiqué a x600
        super().__init__(title, configure, geometry) #Ejemplo de HERENCIA
    
    def bar_menu(self):

        my_menu= Menu(self.win)
        self.win.config(menu=my_menu)

        #Create a menu item
        file_menu = Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label= "Exit...", command=self.win.quit)
        
        #Create a export menu
        export_menu= Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label="Export", menu= export_menu)
        export_menu.add_command(label="MX2 - Morelos")
        export_menu.add_command(label="MX3 - Bicentenario")
        export_menu.add_command(label="Ambos")
    
    def search(self):
        frame=LabelFrame(self.win, text="Busqueda")
        frame.config(bg = "#D49FFF")
        frame.pack(side="top", anchor= E, padx = 10, pady = 10)
        my_entry = Entry(frame) #Invocamos la función entry_box dentro de la funcion busqueda, en el frame. Tener cuidado con el nombre de las variables de los frames, ya que en los argumentos del frame lo colocara en frame correspondiente
        my_entry.grid()
        add_event= Button(frame, text= "Buscar")
        add_event.grid(row= 0, column= 2, padx = 5, pady = 10)
    
    def create_title(self, title):
        label= tk.Label(self.win, text=title, font=("Helvetica", 15), fg="#4D4D4D")
        label.configure(bg="#D49FFF")
        label.pack()

    def create_table(self): #Aquí podria faltar win. 
        columns = ("DATEID", "USERID", "EVENT", "SOLUTION")
        self.my_tree = ttk.Treeview(self.win, column = columns, show = 'headings', height = 10) #Originalmente son 5, pero con propositos de desarrollo lo duplique a 10

        self.my_tree.column("DATEID", anchor= CENTER, width=100)
        self.my_tree.column("USERID", anchor= CENTER, width=100) 
        self.my_tree.column("EVENT", anchor= W, width= 300)
        self.my_tree.column("SOLUTION", anchor= W, width=600)

        self.my_tree.heading("DATEID", text="FECHA-ID", anchor=CENTER)
        self.my_tree.heading("USERID", text="USUARIO", anchor=CENTER)
        self.my_tree.heading("EVENT", text="EVENTO", anchor=W)     
        self.my_tree.heading("SOLUTION", text="SOLUCION", anchor=CENTER)
        self.my_tree.pack()
    
    def update_table(self):
        #Connection with our data base
        connection = sqlite3.connect("C:/Users/Joel/Desktop/test_db/IT_database.db")

        #Creating a cursor
        cursor = connection.cursor()

        #Visualize data
        cursor.execute("Select * from EVENTS")

        #Ordenar por pila y no por fila!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        rows= cursor.fetchall()
        print(rows)
        for row in rows:
            self.my_tree.insert("", tk.END, values = row)
        connection.close()
    
    def create_button(self, texto):
        add_event=tk.Button(text=texto, command= create_event_window)
        add_event.pack()


def create_event_window():

    from EventWindowGUI import EventWindow
    from bita import MainWindow

    event_window = EventWindow()
    event_window.logging_section()
    event_window.event_section()
    event_window.checkbox_section()
    event_window.solution_section()
    event_window.show()