import sqlite3
import tkinter


import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import date

from common import GUI


class EventWindow(GUI):
    
    def __init__(self):
        title = "Eventos"
        configure = "#D49FFF"
        geometry = "650x600"
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
        self.event_text = tk.Text(event_frame, height = 5, width = 20)
        self.event_text.pack(expand=True, fill="both", padx= 5, pady=5)

    def get_input(self):
        input_event= self.event_text.get("1.0","end-1c")
        print(input_event)

        x=self.mx2w.get()
        print(x)

        y=str(x)
        print(y)

        input_solution= self.solution_text.get("1.0","end-1c")
                  
        connection = sqlite3.connect("C:/Users/Joel/Escritorio/test_db/IT_database.db")
        cursor = connection.cursor()
        cursor.execute('insert into events(EVENT, SOLUTION) values ("'+input_event+'","'+input_solution+'")')
        connection.commit()
        print('insert into EVENTS (EVENT, SOLUTION) values ("'+input_event+'","'+input_solution+'")')
            #cursor.execute('insert into events(EVENT, SOLUTION) values ("'+input_event+'","'+input_solution+'");')    


    def checkbox(self):

        self.checkbox_frame= tk.Frame(self.win, padx=10, pady=10, bg="#D49FFF")
        self.checkbox_frame.pack(side="top") #expand=True, fill="both"


        label_marks= tk.Label(self.checkbox_frame, text="MARCADORES", font=("Helvetica", 15), bg="#D49FFF",fg="#4D4D4D")
        label_marks.grid(row=0, column=1)
        label_mx2= tk.Label(self.checkbox_frame, text="MX2", bg="#D49FFF",fg="#4D4D4D") #font=("Helvetica", 15)
        label_mx2.grid(row=1, column=0)
        label_mx3= tk.Label(self.checkbox_frame, text="MX3", bg="#D49FFF",fg="#4D4D4D") #font=("Helvetica", 15)
        label_mx3.grid(row=1, column=2)
        

        self.mx2w=IntVar(self.checkbox_frame)
        checkbutton_mx2w = tk.Checkbutton(self.checkbox_frame, bg="#D49FFF" , variable=self.mx2w)
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


        getInto_event= tk.Button(self.checkbox_frame, text="Ingresar", command= self.get_input)
        getInto_event.grid(row= 8, column= 1, pady=20)


    def solution(self):
        solution_frame = LabelFrame(self.win, text="SOLUCION", bg="#D49FFF")
        solution_frame.pack(side="top", expand=True, fill="both", padx = 10, pady = 10) #anchor= E
        self.solution_text = tk.Text(solution_frame)
        self.solution_text.pack(expand=True, fill="both", padx= 5, pady=5)