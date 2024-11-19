import tkinter
import sqlite3

import tkinter as tk
from tkinter import *
from tkinter import ttk

from miscellaneous import *

class traceWindow():
    
    def __init__(self, selection, main_window):

        #self.win=main_window.win
        self.main_window=main_window
        self.selection=selection
        #self.trace_window=Toplevel(main_window.win)
        self.trace_window= tkinter.Tk()
        self.trace_window.title("SEGUIMIENTO")
        self.trace_window.configure(bg="#D49FFF")
        self.trace_window.geometry("500x500")
        #self.trace_window.resizable()
        self.put_label()
        self.update_event()
        self.checkbutton_button()
        #self.trace_window.deiconify()
        #self.trace_window.mainloop()
    
    def put_label(self):#,selection)
        
        label= tk.Label(self.trace_window, text=self.selection[1], font=("Helvetica", 12), fg="#4D4D4D")
        #print(selection[0])
        label.configure(bg="#D49FFF")
        label.pack()

        label1= tk.Label(self.trace_window, text=self.selection[2], font=("Helvetica", 12), fg="#4D4D4D")
        label1.configure(bg="#D49FFF")
        label1.pack()

        label2= tk.Label(self.trace_window, text=self.selection[3], font=("Helvetica", 12), fg="#4D4D4D", wraplength=480, justify=LEFT)
        label2.configure(bg="#D49FFF")
        label2.pack()

        self.user= StringVar(self.trace_window)
        self.user.set("Usuario")
        pullDown_menuUser = OptionMenu(self.trace_window, self.user, "Coordinador", "Analista", "Invitado") #self.user
        pullDown_menuUser.pack()

    def update_event(self):

        self.update_frame=LabelFrame(self.trace_window, text="ACTUALIZACION", bg="#D49FFF")
        self.update_frame.pack(side="top", expand=True, fill="both", padx = 10, pady = 10) #anchor= E
        self.event_text = tk.Text(self.update_frame, height = 5, width = 20)
        self.event_text.pack(expand=True, fill="both", padx= 5, pady=5)
    
    def checkbutton_button(self):

        
        self.corrective=IntVar(self.trace_window)
        checkbutton_corrective= tk.Checkbutton(self.trace_window, variable=self.corrective, bg="#D49FFF", text="Correctivo")
        checkbutton_corrective.pack()
        #label_attention_inc= tk.Label(self.trace_window, text="ATENCION A INCIDENCIA.",fg="#4D4D4D" , bg="#D49FFF")#Podria necesitar cambiarlo a frame 
        #label_attention_inc.pack()#row=3, column=4, padx=30
        self.attention_inc=IntVar(self.trace_window)
        checkbutton_attention_inc = tk.Checkbutton(self.trace_window, variable=self.attention_inc, bg="#D49FFF", text="Atención a Incidencia")
        checkbutton_attention_inc.pack()#row=4, column=4
        
        update_inc= tk.Button(self.trace_window, text="ACTUALIZAR TICKET", command=self.update_ticket)
        update_inc.pack(pady=20)

    def validation(self):

        user= self.user.get()
        input_trace= str(self.event_text.get("1.0","end-1c"))

        if hasattr(self, 'message_user'):
            self.message_user.destroy()

        if user == "Usuario":
            print("hey")
            self.message_user= Message(self.trace_window, text="Primero debes seleccionar un usuario", bg="red", width=1000)  
            self.message_user.pack()
        elif input_trace == "":
            self.message_user= Message(self.trace_window, text="¿Cual es la actualización?", bg="red", width=1000)
            self.message_user.pack()
        else:
            return True
        return False
    
    def update_ticket(self):
        
        #We get the value of user
        user=self.user.get()
        print(user)


        #We get the text
        input_trace=self.event_text.get("1.0","end-1c")
        print("ACTUALIZACION DEL EVENTO: " +input_trace)

        #We get the value of checkbutton
        attention_inc=self.attention_inc.get()
        attention_incstr=str(attention_inc) #This is for marks either for one or another
        print("Checkbutton " +attention_incstr)

        corrective=self.corrective.get()
        corrective_str=str(corrective)
        #print(corrective_str)

        

        #Conexion con base de datos para comprobar el numero de ticket
        connection = sqlite3.connect(path)
        cursor = connection.cursor()
        print("self.selection[1]")
        print(self.selection[1])
        cursor.execute('select * from events where ticket="'+self.selection[1]+'"') #Comprobamos los eventos que hay en events con el numero de ticket correspondiente
        #Otro cursor execute ahora para marksmx2
        #rows= cursor.fetchall()
        #print(rows)
        rows=str(cursor.fetchall()).split(",")[0][2:]
        print("Rows= " +rows) #Mostramos el dateid que corresponda al ticket seleccionado
        

        cursor.execute('select * from marksmx2 where dateid="'+rows+'"') #Comprobaremos si existe un evento en MARKSMX2 con el dateid seleccionado
        markmx2=str(cursor.fetchall()).split(",")[0][2:]
        print("Estos son los indicadores de MARKSMX2")
        print(markmx2)

        cursor.execute('select * from marksmx3 where dateid="'+rows+'"') #Comprobaremos si existe un evento en MARKSMX3 con el dateid seleccionado
        markmx3=str(cursor.fetchall()).split(",")[0][2:]
        print("Estos son los indicadores de MARKSMX3")
        print(markmx3)
        
        #bug:Cuando seleccionamos las casillas corrective and atencion inc y el evento no fue marcado como mx2 o mx3 de todos modos mete estas dos casillas a mx2
        if self.validation() == True:
            if rows == markmx2:
                cursor.execute('insert into EVENTS(DATEID, USERID, EVENT, TICKET) values ('+generator_dateID()+',"'+user+'","'+input_trace+'","'+self.selection[1]+'")')
                cursor.execute('insert into MARKSMX2(DATEID, WEEKLY, SEMESTER, INCMX2, ATINCMX2, CORRMX2) values ('+generator_dateID()+',"0","0","0","'+attention_incstr+'","'+corrective_str+'")')
                connection.commit()
            #print("Hay evento en MARKSMX2")
            elif rows == markmx3:
                cursor.execute('insert into EVENTS(DATEID, USERID, EVENT, TICKET) values ('+generator_dateID()+',"'+user+'","'+input_trace+'","'+self.selection[1]+'")')
                cursor.execute('insert into MARKSMX3(DATEID, WEEKLY, SEMESTER, INCMX3, ATINCMX3, CORRMX3) values ('+generator_dateID()+',"0","0","0","'+attention_incstr+'","'+corrective_str+'")')
                connection.commit()
            #print("Hay evento en MARKSMX3")
            else:
            #input_ticket= self.ticket.get()
                cursor.execute('insert into EVENTS(DATEID, USERID, EVENT, TICKET) values ('+generator_dateID()+',"'+user+'","'+input_trace+'","None")')
                connection.commit()
            #print("No hay eventos en MARKSMX2 ni en MARKSMX3")

            self.trace_window.destroy()
        #self.win.deiconify()
        self.main_window.create_table()
