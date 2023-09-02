import tkinter as tk
from tkinter import *
from ChildWin import *

my_window = tk.Tk()
my_window.geometry("400x400")
my_window.title("PARENT WINDOW")

#creating a label
my_str= tk.StringVar()
label1= tk.Label(my_window, textvariable=my_str)
label1.grid(row=1, column=2)
my_str.set("Hi I am main window")

#add a button
button=tk.Button(my_window, text="Click me to open a child window", command= lambda:create_child_window(my_window))
button.grid(row=2, column=2)
#button_withdraw=tk.Button(my_window, text="Dissapear parent", command=my_window.withdraw)
#button_withdraw.grid(row=3, column=1)


    
    
my_window.mainloop()