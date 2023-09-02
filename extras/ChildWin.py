import tkinter as tk
from tkinter import *

class create_child_window():
    def __init__(self,obj):
        #creating a child window
        self.padre=obj

        self.my_child_window=Toplevel(self.padre)
        self.my_child_window.geometry("200x200")
        self.my_child_window.title("child window")

        self.my_str1=tk.StringVar()
        self.label1=tk.Label(self.my_child_window, textvariable=self.my_str1)
        self.label1.grid(row=1, column=1)
        self.my_str1.set("Hi I am a child window")

        self.button_close = tk.Button(self.my_child_window, text="Close", command= self.appear_and_close) #my_child_window.destroy
        self.button_close.grid(row=2,column=1)     
        
        self.padre.withdraw()

    def appear_and_close(self): #Desaparecer Parent abriendo child y aparecer parent destruyendo child
        self.padre.deiconify()
        self.my_child_window.destroy()