import sqlite3
import tkinter

import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import date

from miscellaneous import *
#from date import generator_dateID


class EventWindow():
    
    def __init__(self,main_window): #Creamos un constructor que recibe objeto, ya que estamos declarando el main_window en toplevel
        self.win=main_window.win #A la variable self.win recibe del objeto solo win
        self.main_window=main_window #self.obj recibe el objeto entero, en esta linea recibe el objeto main_window con todas las funciones miembro
        #self.event_window=Toplevel(self.win)
        self.event_window=tkinter.Tk()
        self.event_window.title("Eventos")
        self.event_window.configure(bg="#D49FFF")
        self.event_window.geometry("675x500")
        self.logging_section()
        self.event_section()
        self.checkbox_section()
        #self.validation()
        #self.solution_section()
        #self.win.deiconify() #witthdraw()
        #self.win.destroy()
    
    def logging_section (self):
        self.logging_frame= tk.Frame(self.event_window, bg="#D49FFF", padx=10, pady=10)
        self.logging_frame.pack(side="top", fill="both") #expand=True,

        label= tk.Label(self.logging_frame, text="Fecha-ID:", font=("Helvetica", 15), bg="#D49FFF", fg="#4D4D4D")
        label.grid(row= 0, column= 0)

        label_date= tk.Label(self.logging_frame, text= generator_dateID(), font=("Helvetica", 15), bg="#D49FFF", fg="#4D4D4D") 
        label_date.grid(row=0, column=1)

        self.user= StringVar(self.logging_frame)
        self.user.set("Usuario")
        pullDown_menuUser = OptionMenu(self.logging_frame, self.user, "Coordinador", "Analista", "invitado")
        pullDown_menuUser.grid(row=0, column= 2, padx=50) 

    
    def event_section(self):
        
        self.event_frame=LabelFrame(self.event_window, text="EVENTO", bg="#D49FFF")
        self.event_frame.pack(side="top", expand=True, fill="both", padx = 10, pady = 10) #anchor= E
        self.event_text = tk.Text(self.event_frame, height = 5, width = 20)
        self.event_text.pack(expand=True, fill="both", padx= 5, pady=5)

    
    def checkbox_section(self):

        self.event_window.checkbox_frame= tk.Frame(self.event_window, bg="#D49FFF", padx=10, pady=10)
        self.event_window.checkbox_frame.pack(side="top") #expand=True, fill="both"

        self.MX=IntVar(self.event_window.checkbox_frame) #self.mx2
        checkbutton_mx2=tk.Radiobutton(self.event_window.checkbox_frame, variable=self.MX, value=2, indicatoron=0, text="MX2", bg="#949426") #self.mx2 bg="#D49FFF"
        checkbutton_mx2.grid(column=0, row=0, pady=20)

        label_satelites= tk.Label(self.event_window.checkbox_frame, text="    Satélite", font=("Helvetica", 15), fg="#4D4D4D", bg="#D49FFF")
        label_satelites.grid(column=1, columnspan=2, row=0, pady= 10)

        checkbutton_mx3=tk.Radiobutton(self.event_window.checkbox_frame, variable=self.MX, value=3, indicatoron= 0, text="MX3", bg="#408080") #self.mx3 bg="#D49FFF"
        checkbutton_mx3.grid(column=3, row=0)

        label_marks= tk.Label(self.event_window.checkbox_frame, text="    MARCADORES", font=("Helvetica", 15),fg="#4D4D4D", bg="#D49FFF") #
        label_marks.grid(column=1, columnspan=2, row=1, pady=5)
        
        label_daily= tk.Label(self.event_window.checkbox_frame, text="DIARIO",fg="#4D4D4D", bg="#D49FFF") #font=("Helvetica", 15)
        label_daily.grid(column=0, row=3, padx=30)
        self.daily=IntVar(self.event_window.checkbox_frame)
        checkbutton_daily = tk.Checkbutton(self.event_window.checkbox_frame, variable=self.daily, bg="#D49FFF")
        checkbutton_daily.grid(column=0, row=4)
        
        label_weekly= tk.Label(self.event_window.checkbox_frame, text="SEMANAL",fg="#4D4D4D", bg="#D49FFF") #font=("Helvetica", 15)
        label_weekly.grid(column=1, row=3, padx=30)
        self.weekly=IntVar(self.event_window.checkbox_frame)
        checkbutton_weekly = tk.Checkbutton(self.event_window.checkbox_frame, variable=self.weekly, bg="#D49FFF")
        checkbutton_weekly.grid(column=1, row=4)

        label_semester= tk.Label(self.event_window.checkbox_frame, text="SEMESTRAL", fg="#4D4D4D", bg="#D49FFF") #, bg="#D49FFF" SEMESTRAL
        label_semester.grid(column=2, row=3 , padx=10)
        self.semester=IntVar(self.event_window.checkbox_frame)
        checkbutton_semester = tk.Checkbutton(self.event_window.checkbox_frame, variable=self.semester, bg="#D49FFF")
        checkbutton_semester.grid(column=2, row=4)

        label_incidence= tk.Label(self.event_window.checkbox_frame, text="INCIDENCIA",fg="#4D4D4D", bg="#D49FFF") 
        label_incidence.grid(column=3, row=3)
        self.incidence=IntVar(self.event_window.checkbox_frame)
        checkbutton_incidence = tk.Checkbutton(self.event_window.checkbox_frame, variable=self.incidence,bg="#D49FFF") 
        checkbutton_incidence.grid(column=3, row=4, padx=0)

        label_corrective= tk.Label(self.event_window.checkbox_frame, text="CORRECTIVO",fg="#4D4D4D", bg="#D49FFF")
        label_corrective.grid(column=0, row=5)
        self.corrective=IntVar(self.event_window.checkbox_frame)
        checkbutton_corrective = tk.Checkbutton(self.event_window.checkbox_frame, variable=self.corrective, bg="#D49FFF")
        checkbutton_corrective.grid(column=0, row=6)
        
        label_attention_inc= tk.Label(self.event_window.checkbox_frame, text="ATENCION A INC.",fg="#4D4D4D", bg="#D49FFF")
        label_attention_inc.grid(column=3, row=5, padx=30)
        self.attention_inc=IntVar(self.event_window.checkbox_frame)
        checkbutton_attention_inc = tk.Checkbutton(self.event_window.checkbox_frame, variable=self.attention_inc, bg="#D49FFF") 
        checkbutton_attention_inc.grid(column=3, row=6)
        
        label_ticket= tk.Label(self.event_window.checkbox_frame, text="#-TICKET", fg="#4D4D4D", bg="#D49FFF")
        label_ticket.grid(column=1, columnspan=2, row=5, pady=10)
        self.ticket=tk.Entry(self.event_window.checkbox_frame)
        self.ticket.grid(column=1, columnspan=2, row=6)

        getInto_event= tk.Button(self.event_window.checkbox_frame, text="Ingresar", command= self.get_input)
        getInto_event.grid(column= 1, columnspan=2, row= 13, pady=20)

    
    def validation(self):

            if hasattr(self, 'message_user'):
                self.message_user.destroy()
            
            if len(self.input_ticket)>0:
                connection = sqlite3.connect(path)
                cursor = connection.cursor()
                cursor.execute('SELECT ticket from events WHERE ticket="'+self.input_ticket+'"')
                ticket_equals=cursor.fetchall()
                print("YOU ARE IN VALIDATION FUNCTION")
                print(ticket_equals)
            else:
                ticket_equals=[]
    
            if self.input_user == "Usuario":
                self.message_user= Message(self.logging_frame, text="Primero debes seleccionar un usuario", bg="red", width=1000)  
                self.message_user.grid(row=0, column=3)
            elif self.input_event == "":
                self.message_user= Message(self.logging_frame, text="¿Cual es el evento?", bg="red", width=1000)
                self.message_user.grid(row=0, column=3)
            elif self.input_MX == 2 or self.input_MX == 3:
                if self.input_daily == 0 and self.input_weekly == 0 and self.input_semester == 0 and self.input_incidence == 0 and self.input_corrective == 0 and self.input_attention_inc == 0:
                    self.message_user= Message(self.logging_frame, text="Tienes que seleccionar el tipo de evento", bg="red", width=1000)
                    self.message_user.grid(row=0, column=3)
                elif self.input_incidence == 1 and self.input_ticket == "" :
                    self.message_user= Message(self.logging_frame, text="¿Cual es el #-TICKET?", bg="red", width=1000)
                    self.message_user.grid(row=0, column=3)
                elif len(ticket_equals)>0: 
                    self.message_user= Message(self.logging_frame, text="#-TICKET existente. VERIFICA", bg="red", width=1000)
                    self.message_user.grid(row=0, column=3)
                else:
                    return True
            else:
                return True
            
            return False

    def get_input(self):


        self.input_user= str(self.user.get()) #user
        self.input_event= str(self.event_text.get("1.0","end-1c"))

        self.input_MX=self.MX.get()
        
        self.input_daily=self.daily.get()
        self.input_weekly=self.weekly.get()
        self.input_semester=self.semester.get()
        self.input_corrective=self.corrective.get()
        self.input_incidence=self.incidence.get()
        self.input_attention_inc=self.attention_inc.get()

        self.input_ticket= self.ticket.get()
        self.input_ticket= self.input_ticket.replace(" ","")


        dailystr=str(self.input_daily)
        weeklystr=str(self.input_weekly)
        semesterstr=str(self.input_semester)
        incidencestr=str(self.input_incidence)
        correctivestr=str(self.input_corrective)
        attention_incstr=str(self.input_attention_inc)


        if self.validation() == True:
            if self.input_MX == 2:
                connection = sqlite3.connect(path)
                cursor = connection.cursor()
                cursor.execute('insert into EVENTS(DATEID, USERID, EVENT, TICKET) values ('+generator_dateID()+',"'+self.input_user+'","'+self.input_event.replace('"',"''")+'","'+self.input_ticket+'")')
                cursor.execute('insert into MARKSMX2(DATEID, WEEKLY, SEMESTER, INCMX2, ATINCMX2, CORRMX2, DAILY) values ('+generator_dateID()+',"'+weeklystr+'","'+semesterstr+'","'+incidencestr+'","'+attention_incstr+'","'+correctivestr+'","'+dailystr+'")')
                connection.commit()    
            elif self.input_MX == 3:
                connection = sqlite3.connect(path)
                cursor = connection.cursor()
                cursor.execute('insert into EVENTS(DATEID, USERID, EVENT, TICKET) values ('+generator_dateID()+',"'+self.input_user+'","'+self.input_event.replace('"',"''")+'","'+self.input_ticket+'")')
                cursor.execute('insert into MARKSMX3(DATEID, WEEKLY, SEMESTER, INCMX3, ATINCMX3, CORRMX3, DAILY) values ('+generator_dateID()+',"'+weeklystr+'","'+semesterstr+'","'+incidencestr+'","'+attention_incstr+'","'+correctivestr+'","'+dailystr+'")')
                connection.commit()
            else:
                connection = sqlite3.connect(path)
                cursor = connection.cursor()
                cursor.execute('insert into EVENTS(DATEID, USERID, EVENT) values ('+generator_dateID()+',"'+self.input_user+'","'+self.input_event.replace('"',"''")+'")')#Borre el atributo TICKET en esta linea, ya que no es necesario
                connection.commit()
            self.event_window.destroy() #Aquí destruimos event_window
            #self.win.deiconify() #Aparecemos al padre, self.win
            self.main_window.create_table() #Ejecutamos la función create_table para el objeto, de esta manera actualizamos el treeview con los datos obtenidos de esta funcion get_input
        
        
        
    




