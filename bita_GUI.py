import tkinter
import sqlite3

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

    #def frame(self, texto):
        #frame=LabelFrame(self.win, )
        #frame.pack()


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

class EventWindow(GUI):
    
    def __init__(self):
        title = "Eventos"
        configure = "#D49FFF"
        geometry = "650x500"
        super().__init__(title, configure, geometry)

    def dateid (self):
        today=date.today()
        dateformat=today.strftime("%Y%m%d")
        return str(dateformat)
    
    def logging (self):
        self.logging_frame= tk.Frame(self.win, padx=10, pady=10, bg="#D49FFF")
        self.logging_frame.pack(side="top", fill="both") #expand=True,

        label= tk.Label(self.logging_frame, text="Fecha-ID:", font=("Helvetica", 15), bg="#D49FFF", fg="#4D4D4D") ##F2F2F2
        label.grid(row= 0, column= 0)

        label_date= tk.Label(self.logging_frame, text=EventWindow.dateid(self), font=("Helvetica", 15), bg="#D49FFF", fg="#4D4D4D")
        label_date.grid(row=0, column=1)
        #event_window.text(event_window.dateid(), 0,1)

        user= StringVar(self.logging_frame)
        user.set("Usuario")
        pullDown_menuUser = OptionMenu(self.logging_frame, user, "JAGM", "JCM", "Guest")
        pullDown_menuUser.grid(row=0, column= 2, padx=60)

        #label_user = tk.Label(self.logging_frame, text="Usuario:", font=("Helvetica", 15), bg="#D49FFF", fg="#4D4D4D")
        #label_user.grid(row=0, column=2)

        #user_Entry = tk.Entry(self.logging_frame) #Esta opción la cambiaré por un desplegable con los usuarios dados de alta y un invitado
        #user_Entry.grid(row=0, column=3)

        label_password = tk.Label(self.logging_frame, text="Contraseña", font=("Helvetica", 15), bg="#D49FFF", fg="#4D4D4D")
        label_password.grid(row=0, column=3)

        password_Entry = tk.Entry(self.logging_frame)
        password_Entry.grid(row= 0, column= 4)

    def event(self):
        
        event_frame=LabelFrame(self.win, text="EVENTO", bg="#D49FFF")
        event_frame.pack(side="top", expand=True, fill="both", padx = 10, pady = 10) #anchor= E

        event_entry = tk.Entry(event_frame)
        event_entry.pack(expand=True, fill="both", padx= 5, pady=5)
        
    
    def checkbox(self):
        self.checkbox_frame= tk.Frame(self.win, padx=10, pady=10, bg="#D49FFF")
        self.checkbox_frame.pack(side="top") #expand=True, fill="both"


        label_marks= tk.Label(self.checkbox_frame, text="MARCADORES", font=("Helvetica", 15), bg="#D49FFF",fg="#4D4D4D")
        label_marks.grid(row=0, column=1)
        label_mx2= tk.Label(self.checkbox_frame, text="MX2", bg="#D49FFF",fg="#4D4D4D") #font=("Helvetica", 15)
        label_mx2.grid(row=1, column=0)
        label_mx3= tk.Label(self.checkbox_frame, text="MX3", bg="#D49FFF",fg="#4D4D4D") #font=("Helvetica", 15)
        label_mx3.grid(row=1, column=2)


        checkbutton_mx2w = tk.Checkbutton(self.checkbox_frame, bg="#D49FFF")
        checkbutton_mx2w.grid(row=2, column=0)
        label_weekly= tk.Label(self.checkbox_frame, text="SEMANAL", bg="#D49FFF",fg="#4D4D4D") #font=("Helvetica", 15)
        label_weekly.grid(row=2, column=1)
        checkbutton_mx3w = tk.Checkbutton(self.checkbox_frame, bg="#D49FFF")
        checkbutton_mx3w.grid(row=2, column=2)

        checkbutton_mx2s = tk.Checkbutton(self.checkbox_frame, bg="#D49FFF")
        checkbutton_mx2s.grid(row=3, column=0)
        label_semester= tk.Label(self.checkbox_frame, text="SEMESTRAL", bg="#D49FFF",fg="#4D4D4D") #font=("Helvetica", 15)
        label_semester.grid(row=3, column=1)
        checkbutton_mx3s = tk.Checkbutton(self.checkbox_frame, bg="#D49FFF")
        checkbutton_mx3s.grid(row=3, column=2)

        checkbutton_incmx2 = tk.Checkbutton(self.checkbox_frame, bg="#D49FFF")
        checkbutton_incmx2.grid(row=4, column=0)
        label_inc= tk.Label(self.checkbox_frame, text="INCIDENCIA", bg="#D49FFF",fg="#4D4D4D")
        label_inc.grid(row=4, column=1)
        checkbutton_incmx3 = tk.Checkbutton(self.checkbox_frame, bg="#D49FFF")
        checkbutton_incmx3.grid(row=4, column=2)

        checkbutton_att_incmx2 = tk.Checkbutton(self.checkbox_frame, bg="#D49FFF")
        checkbutton_att_incmx2.grid(row=5, column=0)
        label_attinc= tk.Label(self.checkbox_frame, text="ATENCION A INCIDENCIA", bg="#D49FFF",fg="#4D4D4D")
        label_attinc.grid(row=5, column=1)
        checkbutton_att_incmx3 = tk.Checkbutton(self.checkbox_frame, bg="#D49FFF")
        checkbutton_att_incmx3.grid(row=5, column=2)

        checkbutton_corr_mx2 = tk.Checkbutton(self.checkbox_frame, bg="#D49FFF")
        checkbutton_corr_mx2.grid(row=6, column=0)
        label_corr= tk.Label(self.checkbox_frame, text="CORRECTIVO", bg="#D49FFF",fg="#4D4D4D")
        label_corr.grid(row=6, column=1)
        checkbutton_corr_mx3 = tk.Checkbutton(self.checkbox_frame, bg="#D49FFF")
        checkbutton_corr_mx3.grid(row=6, column=2)

        checkbutton_ticket_mx2 = tk.Checkbutton(self.checkbox_frame, bg="#D49FFF")
        checkbutton_ticket_mx2.grid(row=7, column=0)
        label_ticket= tk.Label(self.checkbox_frame, text="TICKET", bg="#D49FFF",fg="#4D4D4D")
        label_ticket.grid(row=7, column=1)
        checkbutton_ticket_mx3 = tk.Checkbutton(self.checkbox_frame, bg="#D49FFF")
        checkbutton_ticket_mx3.grid(row=7, column=2)

        getInto_event= tk.Button(self.checkbox_frame, text="Ingresar")
        getInto_event.grid(row= 8, column= 1, pady=20)

    def solution(self):
        solution_frame = LabelFrame(self.win, text="SOLUCION", bg="#D49FFF")
        solution_frame.pack(side="top", expand=True, fill="both", padx = 10, pady = 10) #anchor= E

        solution_entry = tk.Entry(solution_frame)
        solution_entry.pack(expand=True, fill="both", padx= 5, pady=5)



def e_window():
    event_window = EventWindow()
    event_window.logging()
    event_window.event()
    event_window.checkbox()
    event_window.solution()
    #event_window.text("Fecha-ID: ", 0,0)
    #event_window.text(event_window.dateid(), 0,1)
    #event_window.text("Usuario: ", 0, 2)
    #event_window.entry_box(0,3)
    #event_window.text("Contraseña: ", 0,4)
    #event_window.entry_box(0, 5)
    #event_window.show()

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

