import tkinter
import sqlite3
import webbrowser
import subprocess

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from EventWindowGUI import EventWindow
from TraceWindowGUI import traceWindow
from aboutWindowGUI import AboutWindow
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
        file_menu.add_command(label="Indicadores", command= self.exporting)
        file_menu.add_separator()
        file_menu.add_command(label= "Exit...", command=self.win.quit)

        #Create an about option
        about_menu= Menu(my_menu, tearoff=0)
        my_menu.add_cascade(label="Help", menu=about_menu, command=self.win.quit)
        about_menu.add_command(label="Info. Indicadores", command=self.ind_info)
        about_menu.add_separator()
        about_menu.add_command(label="About", command=AboutWindow) #About window
    
    def ind_info (self):

        messagebox.showinfo("INFORMACIÓN DE INDICADORES", Ind_Info)

    def exporting (self):
        
        subprocess.call(["sqlite3", "IT_database.db", ". read QUERY_TO_EXPORT.sql"], shell=True) 
    
    def search(self):

        #Aun me falta buscar por DATEID
        
        frame=LabelFrame(self.win, text="Busqueda")
        frame.config(bg = "#D49FFF")
        frame.pack(side="top", anchor= E, padx = 10, pady = 10)
        self.busqueda = Entry(frame) #Invocamos la función entry_box dentro de la funcion busqueda, en el frame. Tener cuidado con el nombre de las variables de los frames, ya que en los argumentos del frame lo colocara en frame correspondiente
        #self.busqueda.bind("<Button-1>", lambda e: self.busqueda.delete(0, tk.END))
        #self.busqueda.insert(END, "ind: YYYYMMDDII - YYYYMMDDII")
        self.busqueda.config(width=30)
        self.busqueda.grid(padx = 5)
        add_event= Button(frame, text= "Buscar", command=self.create_tableHTML)
        add_event.grid(row= 0, column= 2, padx = 5, pady = 10)

        buscar=self.busqueda.get()
        print(buscar)

    def create_tableHTML(self):
        
        buscar=self.busqueda.get()
        print(type(buscar))

        try:
            data=int(buscar)
            data_plus= data+1
            print(data_plus)
            under=buscar[::-1].zfill(10)[::-1]
            print(under)
            top=str(data_plus)[::-1].zfill(10)[::-1]
            print(top)
            texto=f'"%{buscar}%"'
            QUERY_SEARCH=f"""
            SELECT DATEID, TICKET, USERID, EVENT FROM EVENTS
            WHERE DATEID >= {under} AND DATEID < {top}
            """ 
        except:
            buscar_texto=f'"{buscar}"'
            print(buscar_texto)
            texto=f'"%{buscar}%"'
            print(texto)
            QUERY_SEARCH= f"""
            SELECT DATEID, TICKET, USERID, EVENT FROM EVENTS
            WHERE TICKET={buscar_texto}
            OR USERID={buscar_texto}
            OR EVENT LIKE {texto}
            """
        
        if buscar[0:4] == "ind:" and len(buscar) < 28:
            messagebox.showerror("Error de formato", Info)
        elif buscar[:-24] == "ind:" and len(buscar) == 28:
            print("Estas dentro del if")    
            if len(buscar[5:-13]) == 10:
                print("Se trata del inicio de los indicadores ")
                inicio=buscar[5:-13]
                print(inicio)        
                if len(buscar[-10:]) == 10:
                    print("Se trata del fin de los indicadores")
                    fin=buscar[-10:]
                    print(fin)

                    connection = sqlite3.connect(path)
                    cursor = connection.cursor()

                    QUERY_INDICATORS=""".mode box
.headers on
.excel
SELECT EVENTS.DATEID, EVENTS.USERID, EVENTS.TICKET, EVENTS.EVENT, MARKSMX2.DAILY, MARKSMX2.WEEKLY, MARKSMX2.SEMESTER, MARKSMX2.INCMX2, MARKSMX2.CORRMX2, MARKSMX2.ATINCMX2, MARKSMX3.DAILY, MARKSMX3.WEEKLY, MARKSMX3.SEMESTER, MARKSMX3.INCMX3, MARKSMX3.CORRMX3, MARKSMX3.ATINCMX3
FROM EVENTS
LEFT JOIN MARKSMX2
ON EVENTS.DATEID = MARKSMX2.DATEID
LEFT JOIN MARKSMX3
ON EVENTS.DATEID = MARKSMX3.DATEID
WHERE EVENTS.DATEID > """+inicio+" AND EVENTS.DATEID < "+fin+";"""


                    f = open(ind, "w")
                    f.write(QUERY_INDICATORS)
                    f.close()

                    subprocess.call(["sqlite3", "IT_database.db", ".read indicadores.sql"], shell=True)
    

                    
        #else: Este else deberia estar habilitado, pero debido a un error en la linea #148 se comporta de forma correcta

        connection = sqlite3.connect(path)
        cursor = connection.cursor()


        #print(f"SELECT DATEID, TICKET, USERID, EVENT FROM EVENTS WHERE TICKET={buscar_texto} OR USERID={buscar_texto} OR EVENT LIKE {texto}")
        cursor.execute(QUERY_SEARCH)
        rows= cursor.fetchall()
        print(rows)

        print("LISTA rows[0]")
        print(rows[0])
        

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

        def writing_rows(rows):
    
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
            text+=writing_rows(row)
            #print(text)

        print("INICIO")
        print(head+text+end)

        f = open("extras/table.html", "w")
        f.write(head+text+end)
        

        f = open("extras/table.html", "r")
        print(f.read())

        webbrowser.open(search_path)

    
    def create_title(self, title):

        label= tk.Label(self.win, text=title, font=("Helvetica", 15), fg="#4D4D4D")
        label.configure(bg="#D49FFF")
        label.pack()

    def create_table(self): #Aquí podria faltar win. 

        if hasattr(self, 'my_tree'):
            self.my_tree.destroy() #Destruye el treeview si existe
            self.add_event.destroy() #Destruye el boton add_event si existe

        columns = ("DATEID", "TICKET", "USERID", "EVENT", "ATINCMX2", "ATINCMX3")
        self.my_tree = ttk.Treeview(self.win, column = columns, show = 'headings', height = 5) #height = Significa el numero de renglones que tiene el treeview

        self.my_tree.column("DATEID", anchor= CENTER, width=100)
        self.my_tree.column("TICKET", anchor= CENTER, width=100)
        self.my_tree.column("USERID", anchor= CENTER, width=100) 
        self.my_tree.column("EVENT", anchor= W, width= 600)
        self.my_tree.column("ATINCMX2", anchor= CENTER, width= 100)
        self.my_tree.column("ATINCMX3", anchor= CENTER, width= 100)

        self.my_tree.heading("DATEID", text="DATEID", anchor=CENTER)
        self.my_tree.heading("TICKET", text="TICKET", anchor=CENTER)
        self.my_tree.heading("USERID", text="USUARIO", anchor=CENTER)
        self.my_tree.heading("EVENT", text="EVENTO", anchor=W)
        self.my_tree.heading("ATINCMX2", text="ATENCION MX2", anchor=CENTER)     
        self.my_tree.heading("ATINCMX3", text="ATENCION MX3", anchor=CENTER)     
        self.my_tree.pack()
    
        connection = sqlite3.connect(path)

        #Creating a cursor
        cursor = connection.cursor()

        
        cursor.execute(QUERY_TV)
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
    