import sqlite3

from datetime import date

path="C:/Users/Joel/Desktop/GUI_bita/IT_database.db"

text_about= """
BITACORA DE SISTEMAS 
Version 1.0
2024

Sistema Satelital Mexicano
MEXSAT

Gerencia del Centro del Control Satelital Iztpalapa
Cordinación de Sistemas


DESARROLLO

Ing. Joel Carbajal Muñoz


AGRADECIMIENTOS

Ing. Andrea Mijaru Sanchez Hernandez

Ing. Roberto Cadena Vega

M. en C. Jorge Tlacaelel Cruz Garcia

C. America Citlalli Hernandez Vargas

"""

def generator_dateID(): 
        today=date.today() #Esto es para colocar la fecha en el formato correcto añomesdia.
        dateformat=today.strftime("%Y%m%d")
        #print(dateformat) #dateformat es un string

        connection = sqlite3.connect(path) #Comprobar que no haya entrada con la fecha 
        cursor = connection.cursor()
        x =cursor.execute("SELECT dateid FROM events WHERE dateid>="+dateformat+"00")
        check=x.fetchall()
        #print(check)
        #print("SELECT dateid FROM events WHERE dateid>="+dateformat+"00")

        if str(check) == "[]": #getID esto es para añadir dos digitos despues de la fecha añomesdia+00 inicializado en 1
            #print("Dentro del if")
            #print(int(dateformat))
            dateid= int(dateformat)*100+1
            print(dateid)
            dateid_str=str(dateid)
            return dateid_str
        else:
            print("Dentro del else")
            check= int(str(check[-1])[1:-2])
            print(check)
            dateid=str(check+1)
            print(dateid)
            return dateid