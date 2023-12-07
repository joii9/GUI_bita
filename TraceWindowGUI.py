import tkinter
import sqlite3

import tkinter as tk
from tkinter import *
from tkinter import ttk

from date import generator_dateID

class traceWindow():
    
    def __init__(self, selection):

        self.selection=selection
        self.win= tkinter.Tk()
        self.win.title("SEGUIMIENTO")
        self.win.configure(bg="#D49FFF")
        self.win.geometry("500x400")
        self.put_label()
        self.update_event()
        self.checkbutton_button()
        self.win.mainloop()
    
    def put_label(self):#,selection)
        
        label= tk.Label(self.win, text=self.selection[0], font=("Helvetica", 15), fg="#4D4D4D")
        #print(selection[0])
        label.configure(bg="#D49FFF")
        label.pack()

        label1= tk.Label(self.win, text=self.selection[1], font=("Helvetica", 15), fg="#4D4D4D")
        label1.configure(bg="#D49FFF")
        label1.pack()

        label2= tk.Label(self.win, text=self.selection[2], font=("Helvetica", 15), fg="#4D4D4D")
        label2.configure(bg="#D49FFF")
        label2.pack()

        self.user= StringVar(self.win)
        self.user.set("Usuario")
        pullDown_menuUser = OptionMenu(self.win, self.user, "Coordinador", "Analista", "Invitado") #self.user
        pullDown_menuUser.pack()

    def update_event(self):

        self.update_frame=LabelFrame(self.win, text="ACTUALIZACION", bg="#D49FFF")
        self.update_frame.pack(side="top", expand=True, fill="both", padx = 10, pady = 10) #anchor= E
        self.event_text = tk.Text(self.update_frame, height = 5, width = 20)
        self.event_text.pack(expand=True, fill="both", padx= 5, pady=5)
    
    def checkbutton_button(self):

        label_attention_inc= tk.Label(self.win, text="ATENCION A INCIDENCIA.",fg="#4D4D4D" , bg="#D49FFF")#Podria necesitar cambiarlo a frame 
        label_attention_inc.pack()#row=3, column=4, padx=30
        self.attention_inc=IntVar(self.win)
        checkbutton_attention_inc = tk.Checkbutton(self.win, variable=self.attention_inc, bg="#D49FFF")
        checkbutton_attention_inc.pack()#row=4, column=4

        update_inc= tk.Button(self.win, text="ACTUALIZAR TICKET", command=self.update_ticket)
        update_inc.pack(pady=20)

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

        

        #Conexion con base de datos para comprobar el numero de ticket
        connection = sqlite3.connect("C:/Users/Joel/Desktop/GUI_bita/IT_database.db")
        cursor = connection.cursor()
        cursor.execute('select * from events where ticket="'+self.selection[0]+'"') #Comprobamos los eventos que hay en events con el numero de ticket correspondiente
        #Otro cursor execute ahora para marksmx2
        #rows= cursor.fetchall()
        #print(rows)
        rows=str(cursor.fetchall()).split(",")[0][2:]
        print("Rows= " +rows) #Mostramos el dateid que corresponda al ticket seleccionado
        

        cursor.execute('select * from marksmx2 where dateid="'+rows+'"') #Comprobaremos si existe un evento en MARKSMX2 con el dateid seleccionado
        markmx2=str(cursor.fetchall()).split(",")[0][2:]
        print("Estos son los indicadores de MARKSMX2")
        print(markmx2)

        cursor.execute('select * from marksmx3 where dateid="'+rows+'"') #Comprobaremos si existe un evento en MARKSMX2 con el dateid seleccionado
        markmx3=str(cursor.fetchall()).split(",")[0][2:]
        print("Estos son los indicadores de MARKSMX3")
        print(markmx3)
        
        if rows == markmx2:
            cursor.execute('insert into EVENTS(DATEID, USERID, EVENT, TICKET) values ('+generator_dateID()+',"'+user+'","'+input_trace+'","'+self.selection[0]+'")')
            cursor.execute('insert into MARKSMX2(DATEID, ATINCMX2) values ('+generator_dateID()+',"'+attention_incstr+'")')
            connection.commit()
            #print("Hay evento en MARKSMX2")
        elif rows == markmx3:
            cursor.execute('insert into EVENTS(DATEID, USERID, EVENT, TICKET) values ('+generator_dateID()+',"'+user+'","'+input_trace+'","'+self.selection[0]+'")')
            cursor.execute('insert into MARKSMX3(DATEID, ATINCMX3) values ('+generator_dateID()+',"'+attention_incstr+'")')
            connection.commit()
            #print("Hay evento en MARKSMX3")
        else:
            input_ticket= self.ticket.get()
            cursor.execute('insert into EVENTS(DATEID, USERID, EVENT, TICKET) values ('+generator_dateID()+',"'+user+'","'+input_trace+'","'+input_ticket+'")')
            connection.commit()
            #print("No hay eventos en MARKSMX2 ni en MARKSMX3")

        self.win.destroy()
        self.win.create_table()
