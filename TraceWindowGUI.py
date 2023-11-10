import tkinter
#import sqlite3

import tkinter as tk
from tkinter import *
from tkinter import ttk

from EventWindowGUI import EventWindow

class traceWindow():
    
    def __init__(self, selection):
        self.win= tkinter.Tk()
        self.win.title("SEGUIMIENTO")
        self.win.configure(bg="#D49FFF")
        self.win.geometry("500x400")
        self.put_label(selection)
        self.update_event()
        self.checkbutton_button()
        #self.update_ticket()
        #print(selection)
        self.win.mainloop()
    
    def put_label(self, selection):
        
        label= tk.Label(self.win, text=selection[0], font=("Helvetica", 15), fg="#4D4D4D")
        label.configure(bg="#D49FFF")
        label.pack()

        label1= tk.Label(self.win, text=selection[1], font=("Helvetica", 15), fg="#4D4D4D")
        label1.configure(bg="#D49FFF")
        label1.pack()

        label2= tk.Label(self.win, text=selection[2], font=("Helvetica", 15), fg="#4D4D4D")
        label2.configure(bg="#D49FFF")
        label2.pack()

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
        
        input_trace=self.event_text.get("1.0","end-1c")
        print(input_trace)

        attention_inc=self.attention_inc.get()
        print(attention_inc)
        aux=EventWindow(self)
        #aux1=aux.generator_dateID()
        #aux.destroy()

        #print

        #Conexion con base de datos para actualizar
        connection = sqlite3.connect("C:/Users/Joel/Desktop/GUI_bita/IT_database.db")
        cursor = connection.cursor()
        cursor.execute('insert into EVENTS(DATEID, USERID, EVENT, TICKET) values ('+aux1+',"'+user+'","'+input_trace+'","'+attention_ticket+'")')
            



    


#traceWindow=traceWindow()