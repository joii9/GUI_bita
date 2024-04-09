import sqlite3

from datetime import date

path="C:/Users/Joel/Desktop/GUI_bita/IT_database.db"
search_path="C:/Users/Joel/Desktop/GUI_bita/extras/table.html"


QUERY_TV="""   SELECT EVENTS.DATEID, EVENTS.TICKET, EVENTS.USERID, EVENTS.EVENT, MARKSMX2.ATINCMX2, MARKSMX3.ATINCMX3 
                    FROM EVENTS 
                    LEFT JOIN MARKSMX2 
                    ON EVENTS.DATEID = MARKSMX2.DATEID 
                    LEFT JOIN MARKSMX3 
                    ON EVENTS.DATEID = MARKSMX3.DATEID;"""

text_about= """
BITACORA DE SISTEMAS 
Version 1.3.3
2024

Sistema Satelital Mexicano
MEXSAT

Gerencia del Centro de Control Satelital Iztpalapa
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