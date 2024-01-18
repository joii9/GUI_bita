import tkinter

from tkinter import *

from miscellaneous import *

class AboutWindow():
    
    def __init__(self):
        self.about=tkinter.Tk()
        self.about.title("Acerca de...")
        self.about.configure(bg="#D49FFF")
        self.about.geometry("300x400")
        self.creating_text()
    
    def creating_text(self):

        text_ver= Label(self.about, text=text_about, wraplength=500, bg="#D49FFF")
        text_ver.pack()


       