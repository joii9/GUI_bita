import sqlite3
import tkinter


import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import date

from common import GUI
from EventWindowGUI import EventWindow


class MainWindow(GUI):

    def __init__(self):

        title = "BITACORA DE SISTEMAS"
        configure = "#D49FFF"
        geometry = "1250x300"
        super().__init__(title, configure, geometry) #Ejemplo de HERENCIA

    def busqueda(self):
        frame=LabelFrame(self.win, text="Busqueda")
        frame.config(bg = "#D49FFF")
        frame.pack(side="top", anchor= E, padx = 10, pady = 10)
        
        # my_entry= Entry(frame)
        # my_entry.insert(0, "tu mamá 🍕")
        # my_entry.grid(row=0, column=1, padx = 10, pady = 10)
        my_entry = self.entry_box(frame, 0, 1, 5) #Invocamos la función entry_box dentro de la funcion busqueda, en el frame. Tener cuidado con el nombre de las variables de los frames, ya que en los argumentos del frame lo colocara en frame correspondiente
        
        add_event= Button(frame, text= "Buscar")
        add_event.grid(row= 0, column= 2, padx = 5, pady = 10)
        #self.button(frame,"Hola,", 0,2)
                        
    def table(self): #Aquí podria faltar win. 
        columns = ("DATEID", "USERID", "EVENT", "SOLUTION")
        my_tree = ttk.Treeview(self.win, column = columns, show = 'headings', height = 5) # Aquí podria ser self.win

        my_tree.column("DATEID", anchor= CENTER, width=100)
        my_tree.column("USERID", anchor= CENTER, width=100) 
        my_tree.column("EVENT", anchor= W, width= 300)
        my_tree.column("SOLUTION", anchor= W, width=600)

        my_tree.heading("DATEID", text="FECHA-ID", anchor=CENTER)
        my_tree.heading("USERID", text="USUARIO", anchor=CENTER)
        my_tree.heading("EVENT", text="EVENTO", anchor=W)     
        my_tree.heading("SOLUTION", text="SOLUCION", anchor=CENTER)
        my_tree.pack()
        #my_tree.grid(row=2, column=2)

        #Connection with our data base
        connection = sqlite3.connect("C:/Users/Joel/Escritorio/test_db/IT_database.db")

        #Creating a cursor
        cursor = connection.cursor()

        #Visualize data
        cursor.execute("Select * from EVENTS")

        rows= cursor.fetchall()
        print(rows)
        for row in rows:
            my_tree.insert("", tk.END, values = row)
        connection.close()
    
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




# def e_window():
#     event_window = EventWindow()
#     event_window.logging()
#     event_window.event()
#     #event_window.get_input()
#     event_window.checkbox()
#     event_window.solution()
#     #event_window.text("Fecha-ID: ", 0,0)
#     #event_window.text(event_window.dateid(), 0,1)
#     #event_window.text("Usuario: ", 0, 2)
#     #event_window.entry_box(0,3)
#     #event_window.text("Contraseña: ", 0,4)
#     #event_window.entry_box(0, 5)
#     #event_window.show()

main_window = MainWindow()
#main_window.frame()
main_window.busqueda()
#main_window.text("Busqueda", 0,0)
#main_window.entry_box(0,2)
#main_window.button("Buscar", 0, 3)
main_window.text("Eventos pasados", 1, 2)
main_window.table()
main_window.button("Añadir Evento", 3, 2)
main_window.bar_menu()
main_window.show()

