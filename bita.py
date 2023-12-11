import tkinter
import sqlite3

import tkinter as tk
from tkinter import *
from tkinter import ttk

from EventWindowGUI import EventWindow
from TraceWindowGUI import traceWindow


class MainWindow():

    def __init__(self):

        self.win= tkinter.Tk()
        self.win.title("BITACORA DE SISTEMAS                                                                                                                                                                                                     Developed by Eng. Joel Carbajal Muñoz")
        self.win.configure(bg="#D49FFF")
        self.win.geometry("1100x300")
        
    
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
        my_entry.grid(padx = 5)
        add_event= Button(frame, text= "Buscar")
        add_event.grid(row= 0, column= 2, padx = 5, pady = 10)
    
    def create_title(self, title):

        label= tk.Label(self.win, text=title, font=("Helvetica", 15), fg="#4D4D4D")
        label.configure(bg="#D49FFF")
        label.pack()

    def create_table(self): #Aquí podria faltar win. 

        #try:
        if hasattr(self, 'my_tree'):
            self.my_tree.destroy() #Destruye el treeview si existe
            self.add_event.destroy() #Destruye el boton add_event si existe
        #except:
        #else:
            #print("ah ah ahhhh") #En la primer corrida, como my_tree ni add_event existen en la consola se observa la impresion

        columns = ("TICKET", "USERID", "EVENT")
        self.my_tree = ttk.Treeview(self.win, column = columns, show = 'headings', height = 5) #Originalmente son 5, pero con propositos de desarrollo lo duplique a 10

        self.my_tree.column("TICKET", anchor= CENTER, width=100)
        self.my_tree.column("USERID", anchor= CENTER, width=100) 
        self.my_tree.column("EVENT", anchor= W, width= 800)
        #self.my_tree.column("SOLUTION", anchor= W, width=600)

        self.my_tree.heading("TICKET", text="TICKET", anchor=CENTER)
        self.my_tree.heading("USERID", text="USUARIO", anchor=CENTER)
        self.my_tree.heading("EVENT", text="EVENTO", anchor=W)     
        #self.my_tree.heading("SOLUTION", text="SOLUCION", anchor=CENTER)
        self.my_tree.pack()
    
        connection = sqlite3.connect("C:/Users/Joel/Desktop/GUI_bita/IT_database.db")

        #Creating a cursor
        cursor = connection.cursor()

        #Visualize data
        cursor.execute("Select TICKET ,USERID, EVENT from EVENTS")

        rows= cursor.fetchall()
        #print(rows) Este print son los primeros que pone en el treeview
       
        for row in rows:
            self.my_tree.insert("", 0, values = row)
        connection.close()
        
        #self.sel=self.my_tree.focus()
        self.my_tree.bind("<Double-1>", self.click) #acuerdate que con () la funcion se ejecuta a la de a webo
        
        self.add_event=tk.Button(text="Añadir Evento", command= lambda:EventWindow(self)) #Antes self.win pero de esta forma solo pasaba la ventana a EventWindow. La forma correcta es solo self para pasar el objeto completo.
        self.add_event.pack()

    def click(self, e):

        #trace_Window=traceWindow(self)
        self.selection=self.my_tree.focus()
        print(self.selection)
        #traceWindow(self)
        self.selection=traceWindow(self.my_tree.item(self.selection, "values") ,self)#[0]
        #variable=traceWindow(arg1,arg2)#arg1=selection, arg2=MainWindow

    
    
    
    def show(self):

        self.win.mainloop()
    