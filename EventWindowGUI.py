import sqlite3
import tkinter


import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import date



class EventWindow():
    
    def __init__(self,win):
        self.win=win
        self.event_window=Toplevel(self.win)
        self.event_window.title("Eventos")
        self.event_window.configure(bg="#D49FFF")
        self.event_window.geometry("675x600")
        self.logging_section()
        self.event_section()
        self.checkbox_section()
        self.solution_section()
        self.win.withdraw()

    def generator_dateID(self): 
        today=date.today() #Esto es para colocar la fecha en el formato correcto añomesdia.
        dateformat=today.strftime("%Y%m%d")
        #print(dateformat) #dateformat es un string

        connection = sqlite3.connect("C:/Users/Joel/Desktop/test_db/IT_database.db") #Comprobar que no haya entrada con la fecha 
        cursor = connection.cursor()
        x =cursor.execute("SELECT dateid FROM events WHERE dateid>="+dateformat+"00")
        check=x.fetchall()
        #print(check)
        #print("SELECT dateid FROM events WHERE dateid>="+dateformat+"00")

        if str(check) == "[]": #getID esto es para añadir dos digitos despues de la fecha añomesdia+00 inicializado en 1
            #print("Dentro del if")
            #print(int(dateformat))
            dateid= int(dateformat)*100+1
            #print(dateid)
            dateid_str=str(dateid)
            return dateid_str
        else:
            print("Dentro del else")
            check= int(str(check[-1])[1:-2])
            print(check)
            dateid=str(check+1)
            print(dateid)
            return dateid
    
    def logging_section (self):
        self.logging_frame= tk.Frame(self.event_window, padx=10, pady=10, bg="#D49FFF")
        self.logging_frame.pack(side="top", fill="both") #expand=True,

        label= tk.Label(self.logging_frame, text="Fecha-ID:", font=("Helvetica", 15), bg="#D49FFF", fg="#4D4D4D") ##F2F2F2
        label.grid(row= 0, column= 0)

        label_date= tk.Label(self.logging_frame, text= EventWindow.generator_dateID(self), font=("Helvetica", 15), bg="#D49FFF", fg="#4D4D4D") #EventWindow.getID()
        label_date.grid(row=0, column=1)
        #event_window.text(event_window.dateid(), 0,1)

        self.user= StringVar(self.logging_frame)
        self.user.set("Usuario")
        pullDown_menuUser = OptionMenu(self.logging_frame, self.user, "JAGM", "JCM", "Guest")
        pullDown_menuUser.grid(row=0, column= 2, padx=60)

        label_password = tk.Label(self.logging_frame, text="Contraseña", font=("Helvetica", 15), bg="#D49FFF", fg="#4D4D4D")
        label_password.grid(row=0, column=3)

        password_Entry = tk.Entry(self.logging_frame)
        password_Entry.grid(row= 0, column= 4)
    
    def event_section(self):
        
        self.event_frame=LabelFrame(self.event_window, text="EVENTO", bg="#D49FFF")
        self.event_frame.pack(side="top", expand=True, fill="both", padx = 10, pady = 10) #anchor= E
        self.event_text = tk.Text(self.event_frame, height = 5, width = 20)
        self.event_text.pack(expand=True, fill="both", padx= 5, pady=5)

    def get_input(self):

        user= self.user.get()
        print(user)

        input_event= self.event_text.get("1.0","end-1c")
        print(input_event)

        mx2w=self.mx2w.get()
        mx3w=self.mx3w.get()
        print(mx2w)
        print(mx3w)

        input_solution= self.solution_text.get("1.0","end-1c")
        print(input_solution)

                  
        connection = sqlite3.connect("C:/Users/Joel/Desktop/test_db/IT_database.db")
        cursor = connection.cursor()
        print('insert into EVENTS (DATEID, USERID, EVENT, SOLUTION) values ('+self.generator_dateID()+',"'+user+'","'+input_event+'","'+input_solution+'")')
        cursor.execute('insert into EVENTS(DATEID, USERID, EVENT, SOLUTION) values ("'+self.generator_dateID()+'","'+user+'","'+input_event+'","'+input_solution+'")')
        connection.commit() #descomentar esto para que surjan efecto mi el .execute de arrba
        #print('insert into EVENTS (DATEID, USERID, EVENT, SOLUTION) values ('+self.dateID()+',"'+user+'","'+input_event+'","'+input_solution+'")')
        #self.parent=update_table()
        self.event_window.destroy()
    
    def checkbox_section(self):

        self.event_window.checkbox_frame= tk.Frame(self.event_window, padx=10, pady=10, bg="#D49FFF")
        self.event_window.checkbox_frame.pack(side="top") #expand=True, fill="both"


        label_marks= tk.Label(self.event_window.checkbox_frame, text="MARCADORES", font=("Helvetica", 15), bg="#D49FFF",fg="#4D4D4D")
        label_marks.grid(row=0, column=1)
        label_mx2= tk.Label(self.event_window.checkbox_frame, text="MX2", bg="#D49FFF",fg="#4D4D4D") #font=("Helvetica", 15)
        label_mx2.grid(row=1, column=0)
        label_mx3= tk.Label(self.event_window.checkbox_frame, text="MX3", bg="#D49FFF",fg="#4D4D4D") #font=("Helvetica", 15)
        label_mx3.grid(row=1, column=2)
        

        self.mx2w=IntVar(self.event_window.checkbox_frame)
        checkbutton_mx2w = tk.Checkbutton(self.event_window.checkbox_frame, bg="#D49FFF" , variable=self.mx2w)
        checkbutton_mx2w.grid(row=2, column=0)
        label_weekly= tk.Label(self.event_window.checkbox_frame, text="SEMANAL", bg="#D49FFF",fg="#4D4D4D") #font=("Helvetica", 15)
        label_weekly.grid(row=2, column=1)
        self.mx3w=IntVar(self.event_window.checkbox_frame)
        checkbutton_mx3w = tk.Checkbutton(self.event_window.checkbox_frame, bg="#D49FFF", variable=self.mx3w)
        checkbutton_mx3w.grid(row=2, column=2)

        checkbutton_mx2s = tk.Checkbutton(self.event_window.checkbox_frame, bg="#D49FFF")
        checkbutton_mx2s.grid(row=3, column=0)
        label_semester= tk.Label(self.event_window.checkbox_frame, text="SEMESTRAL", bg="#D49FFF",fg="#4D4D4D") #font=("Helvetica", 15)
        label_semester.grid(row=3, column=1)
        checkbutton_mx3s = tk.Checkbutton(self.event_window.checkbox_frame, bg="#D49FFF")
        checkbutton_mx3s.grid(row=3, column=2)

        checkbutton_incmx2 = tk.Checkbutton(self.event_window.checkbox_frame, bg="#D49FFF")
        checkbutton_incmx2.grid(row=4, column=0)
        label_inc= tk.Label(self.event_window.checkbox_frame, text="INCIDENCIA", bg="#D49FFF",fg="#4D4D4D")
        label_inc.grid(row=4, column=1)
        checkbutton_incmx3 = tk.Checkbutton(self.event_window.checkbox_frame, bg="#D49FFF")
        checkbutton_incmx3.grid(row=4, column=2)

        checkbutton_att_incmx2 = tk.Checkbutton(self.event_window.checkbox_frame, bg="#D49FFF")
        checkbutton_att_incmx2.grid(row=5, column=0)
        label_attinc= tk.Label(self.event_window.checkbox_frame, text="ATENCION A INCIDENCIA", bg="#D49FFF",fg="#4D4D4D")
        label_attinc.grid(row=5, column=1)
        checkbutton_att_incmx3 = tk.Checkbutton(self.event_window.checkbox_frame, bg="#D49FFF")
        checkbutton_att_incmx3.grid(row=5, column=2)

        checkbutton_corr_mx2 = tk.Checkbutton(self.event_window.checkbox_frame, bg="#D49FFF")
        checkbutton_corr_mx2.grid(row=6, column=0)
        label_corr= tk.Label(self.event_window.checkbox_frame, text="CORRECTIVO", bg="#D49FFF",fg="#4D4D4D")
        label_corr.grid(row=6, column=1)
        checkbutton_corr_mx3 = tk.Checkbutton(self.event_window.checkbox_frame, bg="#D49FFF")
        checkbutton_corr_mx3.grid(row=6, column=2)

        checkbutton_ticket_mx2 = tk.Checkbutton(self.event_window.checkbox_frame, bg="#D49FFF")
        checkbutton_ticket_mx2.grid(row=7, column=0)
        label_ticket= tk.Label(self.event_window.checkbox_frame, text="TICKET", bg="#D49FFF",fg="#4D4D4D")
        label_ticket.grid(row=7, column=1)
        checkbutton_ticket_mx3 = tk.Checkbutton(self.event_window.checkbox_frame, bg="#D49FFF")
        checkbutton_ticket_mx3.grid(row=7, column=2)


        getInto_event= tk.Button(self.event_window.checkbox_frame, text="Ingresar", command= self.get_input)
        getInto_event.grid(row= 8, column= 1, pady=20)
    
    
    def solution_section(self):
        solution_frame = LabelFrame(self.event_window, text="SOLUCION", bg="#D49FFF")
        solution_frame.pack(side="top", expand=True, fill="both", padx = 10, pady = 10) #anchor= E
        self.solution_text = tk.Text(solution_frame)
        self.solution_text.pack(expand=True, fill="both", padx= 5, pady=5)



#def create_event_window():
    #from EventWindowGUI import EventWindow
    #event_window = EventWindow()
 #   event_window.logging_section()
  #  event_window.event_section()
  #  event_window.checkbox_section()
  #  event_window.solution_section()
  #  event_window.show()

#event_window = EventWindow()
#event_window.logging_section()
#event_window.event_section()
#event_window.checkbox_section()
#event_window.solution_section()
#event_window.show()