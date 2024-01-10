import tkinter
import sqlite3
import webbrowser

import tkinter as tk
from tkinter import *
from tkinter import ttk

from EventWindowGUI import EventWindow
from TraceWindowGUI import traceWindow
from miscellaneous import *


class MainWindow():

    def __init__(self):

        self.win= tkinter.Tk()
        self.win.title("BITACORA DE SISTEMAS")
        self.win.configure(bg="#D49FFF")
        self.win.geometry("1200x300")
        
    
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
        #export_menu.add_command(label="MX2 - Morelos")
        #export_menu.add_command(label="MX3 - Bicentenario")
        export_menu.add_command(label="MX2 & MX3", command=self.exporting)

        #Create an about option
        about_menu= Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label="About", menu=about_menu, command=self.win.quit)
        about_menu.add_command(label="About", command=self.win.quit) #About window

    def exporting (self):
        
        connection = sqlite3.connect(path)
        cursor = connection.cursor()

        #cursor.execute("excel")
        #connection.commit()

        QUERY_TO_EXPORT="""SELECT EVENTS.DATEID, EVENTS.USERID, EVENTS.TICKET, EVENTS.EVENT, 
                        MARKSMX2.DAILY, MARKSMX2.WEEKLY, MARKSMX2.SEMESTER, MARKSMX2.INCMX2, MARKSMX2.CORRMX2, MARKSMX2.ATINCMX2, 
                        MARKSMX3.DAILY, MARKSMX3.WEEKLY, MARKSMX3.SEMESTER, MARKSMX3.INCMX3, MARKSMX3.CORRMX3, MARKSMX3.ATINCMX3
                        FROM EVENTS
                        LEFT JOIN MARKSMX2
                        ON EVENTS.DATEID = MARKSMX2.DATEID
                        LEFT JOIN MARKSMX3
                        ON EVENTS.DATEID = MARKSMX3.DATEID;"""
        
        cursor.execute(QUERY_TO_EXPORT)
        connection.commit()
        #rows= cursor.fetchall()
        #print(rows)
    
    def search(self):

        #Aun me falta buscar por DATEID
        
        frame=LabelFrame(self.win, text="Busqueda")
        frame.config(bg = "#D49FFF")
        frame.pack(side="top", anchor= E, padx = 10, pady = 10)
        self.busqueda = Entry(frame) #Invocamos la función entry_box dentro de la funcion busqueda, en el frame. Tener cuidado con el nombre de las variables de los frames, ya que en los argumentos del frame lo colocara en frame correspondiente
        self.busqueda.grid(padx = 5)
        add_event= Button(frame, text= "Buscar", command=self.create_tableHTML)
        add_event.grid(row= 0, column= 2, padx = 5, pady = 10)

        buscar=self.busqueda.get()
        print(buscar)

    def create_tableHTML(self):
        
        buscar=self.busqueda.get()
        print(buscar)
        
        
        buscar_TU=f'"{buscar}"'
        print(buscar_TU)
        texto=f'"%{buscar}%"'
        print(texto)

        #texto='"%analista%"'
        #print(texto)

        connection = sqlite3.connect(path)
        cursor = connection.cursor()

        #print(f"SELECT DATEID, TICKET, USERID, EVENT FROM EVENTS WHERE TICKET={buscar_TU} OR USERID={buscar_TU} OR EVENT LIKE {texto}")
        cursor.execute(f"SELECT DATEID, TICKET, USERID, EVENT FROM EVENTS WHERE TICKET={buscar_TU} OR USERID={buscar_TU} OR EVENT LIKE {texto}")
        rows= cursor.fetchall()
        print(rows)

        print("LISTA rows[0]")
        print(rows[0])
        #print("STRING rows[0]")
        #print(str(rows[0]))

        #chain=str(rows[0]).split(",")
        #print("Y ESTE?")
        #print(chain[0])

        connection.close()

        head="""
            <body bgcolor="black">
            <body text="white">
            <h1>CONSULTA DE EVENTOS</h1>

            <h2>Filtro: <em>"""+texto+"""</em> </h2> <!-- texto va a ser el filtro de busqueda en los querys-->

            <table bgcolor="white">
                <tr bgcolor="black">
                    <th width=150>FECHAID</th>
                    <th width=150>TICKET</th>
                    <th width=150>USUARIO</th>
                    <th width=1300>EVENTO</th>
                </tr>
        

            """

        def generating_file(rows):
    
            table= """
                <tr bgcolor="black" align="center">
                    <td>"""+str(rows[0])+"""</td> 
                    <td>"""+str(rows[1])+"""</td>
                    <td>"""+str(rows[2])+"""</td>
                    <td align="left">"""+rows[3]+"""</td>
                </tr>
                """
            print(table)
            return table

        end= "</table>"

        text=""
        for row in rows:
            text+=generating_file(row)
            #print(text)

        print("INICIO")
        print(head+text+end)

        f = open("extras/table.html", "w")
        f.write(head+text+end)
        

        f = open("extras/table.html", "r")
        print(f.read())

        webbrowser.open("C:/Users/Joel/Desktop/GUI_bita/extras/table.html")

    
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

        columns = ("DATEID", "TICKET", "USERID", "EVENT", "ATINCMX2", "ATINCMX3")
        self.my_tree = ttk.Treeview(self.win, column = columns, show = 'headings', height = 5) #Originalmente son 5, pero con propositos de desarrollo lo duplique a 10

        self.my_tree.column("DATEID", anchor= CENTER, width=100)
        self.my_tree.column("TICKET", anchor= CENTER, width=100)
        self.my_tree.column("USERID", anchor= CENTER, width=100) 
        self.my_tree.column("EVENT", anchor= W, width= 600)
        self.my_tree.column("ATINCMX2", anchor= CENTER, width= 100)
        self.my_tree.column("ATINCMX3", anchor= CENTER, width= 100)
        #self.my_tree.column("SOLUTION", anchor= W, width=600)

        self.my_tree.heading("DATEID", text="DATEID", anchor=CENTER)
        self.my_tree.heading("TICKET", text="TICKET", anchor=CENTER)
        self.my_tree.heading("USERID", text="USUARIO", anchor=CENTER)
        self.my_tree.heading("EVENT", text="EVENTO", anchor=W)
        self.my_tree.heading("ATINCMX2", text="ATENCION MX2", anchor=CENTER)     
        self.my_tree.heading("ATINCMX3", text="ATENCION MX3", anchor=CENTER)     
        #self.my_tree.heading("SOLUTION", text="SOLUCION", anchor=CENTER)
        self.my_tree.pack()
    
        connection = sqlite3.connect(path)

        #Creating a cursor
        cursor = connection.cursor()

        #Visualize data
        QUERY="""   SELECT EVENTS.DATEID, EVENTS.TICKET, EVENTS.USERID, EVENTS.EVENT, MARKSMX2.ATINCMX2, MARKSMX3.ATINCMX3 
                    FROM EVENTS 
                    LEFT JOIN MARKSMX2 
                    ON EVENTS.DATEID = MARKSMX2.DATEID 
                    LEFT JOIN MARKSMX3 
                    ON EVENTS.DATEID = MARKSMX3.DATEID;"""
        
        cursor.execute(QUERY)
        #cursor.execute("Select * from prueba")

        rows= cursor.fetchall()
        print(rows) #Este print son los primeros que pone en el treeview
       
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
    