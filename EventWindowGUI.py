import sqlite3
import tkinter


import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import date

#from bita import update_table

class EventWindow():
    
    def __init__(self,obj): #Creamos un constructor que recibe objeto, ya que estamos declarando el main_window en toplevel
        self.win=obj.win #A la variable self.win recibe del objeto solo win
        self.obj=obj #self.obj recibe el objeto entero, en esta linea recibe el objeto main_window con todas las funciones miembro
        self.event_window=Toplevel(self.win)
        self.event_window.title("Eventos")
        self.event_window.configure(bg="#D49FFF")
        self.event_window.geometry("675x400")
        self.logging_section()
        self.event_section()
        self.checkbox_section()
        #self.solution_section()
        self.win.withdraw()

    def generator_dateID(self): 
        today=date.today() #Esto es para colocar la fecha en el formato correcto añomesdia.
        dateformat=today.strftime("%Y%m%d")
        #print(dateformat) #dateformat es un string

        connection = sqlite3.connect("C:/Users/SOC/Desktop/test_db/IT_database.db") #Comprobar que no haya entrada con la fecha 
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
        pullDown_menuUser = OptionMenu(self.logging_frame, self.user, "Coordinador", "Analista", "Guest") #self.user
        pullDown_menuUser.grid(row=0, column= 2, padx=340)

        #label_password = tk.Label(self.logging_frame, text="Contraseña", font=("Helvetica", 15), bg="#D49FFF", fg="#4D4D4D")
        #label_password.grid(row=0, column=3)

        #password_Entry = tk.Entry(self.logging_frame)
        #password_Entry.grid(row= 0, column= 4)
    
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
        #input_solution= self.solution_text.get("1.0","end-1c")

        mx2=self.mx2.get()
        mx3=self.mx3.get()
        weekly=self.weekly.get()
        semester=self.semester.get()
        corrective=self.corrective.get()
        incidence=self.incidence.get()
        attention_inc=self.attention_inc.get()
        print(mx2)
        print(mx3)
        print(weekly)
        print(semester)
        print(corrective)
        print(incidence)
        print(attention_inc)
        
        weeklystr=str(weekly)
        semesterstr=str(semester)
        correctivestr=str(corrective)
        incidencestr=str(incidence)
        attention_incstr=str(attention_inc)

        
        if mx2 == 1 and mx3==0:
            connection = sqlite3.connect("C:/Users/SOC/Desktop/test_db/IT_database.db")
            cursor = connection.cursor()
            cursor.execute('insert into EVENTS(DATEID, USERID, EVENT) values ('+self.generator_dateID()+',"'+user+'","'+input_event+'")')
            cursor.execute('insert into MARKSMX2(DATEID, WEEKLY, SEMESTER, INCMX2, ATINCMX2, CORRMX2) values ('+self.generator_dateID()+',"'+weeklystr+'","'+semesterstr+'","'+incidencestr+'","'+attention_incstr+'","'+correctivestr+'")')
            connection.commit()
        elif mx2 == 0 and mx3 == 1:
            connection = sqlite3.connect("C:/Users/SOC/Desktop/test_db/IT_database.db")
            cursor = connection.cursor()
            cursor.execute('insert into EVENTS(DATEID, USERID, EVENT) values ('+self.generator_dateID()+',"'+user+'","'+input_event+'")')
            cursor.execute('insert into MARKSMX3(DATEID, WEEKLY, SEMESTER, INCMX3, ATINCMX3, CORRMX3, TICKETMX3) values ('+self.generator_dateID()+',1,1,1,1,1,1)')
            connection.commit()
        else:
            connection = sqlite3.connect("C:/Users/SOC/Desktop/test_db/IT_database.db")
            cursor = connection.cursor()
            cursor.execute('insert into EVENTS(DATEID, USERID, EVENT) values ('+self.generator_dateID()+',"'+user+'","'+input_event+'")')
            connection.commit()
        

        self.event_window.destroy() #Aquí destruimos event_window
        self.win.deiconify() #Aparecemos al padre, self.win
        self.obj.create_table() #Ejecutamos la función create_table para el objeto, de esta manera actualizamos el treeview con los datos obtenidos de esta funcion get_input
    
    def checkbox_section(self):

        self.event_window.checkbox_frame= tk.Frame(self.event_window, padx=10, pady=10, bg="#D49FFF")
        self.event_window.checkbox_frame.pack(side="top") #expand=True, fill="both"

        
        label_marks= tk.Label(self.event_window.checkbox_frame, text="MARCADORES", font=("Helvetica", 15), bg="#D49FFF",fg="#4D4D4D")
        label_marks.grid(row=0, column=2)
        
        label_mx2= tk.Label(self.event_window.checkbox_frame, text="MX2", bg="#D49FFF",fg="#4D4D4D") #font=("Helvetica", 15)
        label_mx2.grid(row=1, column=1)
        self.mx2=IntVar(self.event_window.checkbox_frame)
        checkbutton_mx2=tk.Checkbutton(self.event_window.checkbox_frame, bg="#D49FFF", variable=self.mx2)
        checkbutton_mx2.grid(row=2, column=1)

        label_mx3= tk.Label(self.event_window.checkbox_frame, text="MX3", bg="#D49FFF",fg="#4D4D4D") #font=("Helvetica", 15)
        label_mx3.grid(row=1, column=3)
        self.mx3=IntVar(self.event_window.checkbox_frame)
        checkbutton_mx3=tk.Checkbutton(self.event_window.checkbox_frame, bg="#D49FFF", variable=self.mx3)
        checkbutton_mx3.grid(row=2, column=3)
        

        label_weekly= tk.Label(self.event_window.checkbox_frame, text="SEMANAL", bg="#D49FFF",fg="#4D4D4D") #font=("Helvetica", 15)
        label_weekly.grid(row=3, column=0, padx=30)
        self.weekly=IntVar(self.event_window.checkbox_frame)
        checkbutton_weekly = tk.Checkbutton(self.event_window.checkbox_frame, bg="#D49FFF" , variable=self.weekly)
        checkbutton_weekly.grid(row=4, column=0)
        

        label_semester= tk.Label(self.event_window.checkbox_frame, text="SEMESTRAL", bg="#D49FFF",fg="#4D4D4D") #font=("Helvetica", 15)
        label_semester.grid(row=3, column=1, padx=10)
        self.semester=IntVar(self.event_window.checkbox_frame)
        checkbutton_semester = tk.Checkbutton(self.event_window.checkbox_frame, bg="#D49FFF", variable=self.semester)
        checkbutton_semester.grid(row=4, column=1)
        
    
        label_corrective= tk.Label(self.event_window.checkbox_frame, text="CORRECTIVO", bg="#D49FFF",fg="#4D4D4D")
        label_corrective.grid(row=3, column=2)
        self.corrective=IntVar(self.event_window.checkbox_frame)
        checkbutton_corrective = tk.Checkbutton(self.event_window.checkbox_frame, bg="#D49FFF", variable=self.corrective)
        checkbutton_corrective.grid(row=4, column=2)
        

        label_incidence= tk.Label(self.event_window.checkbox_frame, text="INCIDENCIA", bg="#D49FFF",fg="#4D4D4D")
        label_incidence.grid(row=3, column=3)
        self.incidence=IntVar(self.event_window.checkbox_frame)
        checkbutton_incidence = tk.Checkbutton(self.event_window.checkbox_frame, bg="#D49FFF", variable=self.incidence)
        checkbutton_incidence.grid(row=4, column=3, padx=0)
        
        
        label_attention_inc= tk.Label(self.event_window.checkbox_frame, text="ATENCION A INC.", bg="#D49FFF",fg="#4D4D4D")
        label_attention_inc.grid(row=3, column=4, padx=30)
        self.attention_inc=IntVar(self.event_window.checkbox_frame)
        checkbutton_attention_inc = tk.Checkbutton(self.event_window.checkbox_frame, bg="#D49FFF", variable=self.attention_inc)
        checkbutton_attention_inc.grid(row=4, column=4)
        

        getInto_event= tk.Button(self.event_window.checkbox_frame, text="Ingresar", command= self.get_input)
        getInto_event.grid(row= 13, column= 2, pady=20)
        print(dir(self))




