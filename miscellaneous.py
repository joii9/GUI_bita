import sqlite3

from datetime import date

path="C:/Users/Joel/Desktop/GUI_bita/IT_database.db"

def generator_dateID(): 
        today=date.today() #Esto es para colocar la fecha en el formato correcto añomesdia.
        dateformat=today.strftime("%Y%m%d")
        #print(dateformat) #dateformat es un string

        connection = sqlite3.connect("C:/Users/Joel/Desktop/GUI_bita/IT_database.db") #Comprobar que no haya entrada con la fecha 
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


texto="FILTRO"

connection = sqlite3.connect("C:/Users/Joel/Desktop/GUI_bita/IT_database.db")
cursor = connection.cursor()
cursor.execute("Select DATEID, TICKET, USERID, EVENT from EVENTS ")
rows= cursor.fetchall()
print(rows)

print("LISTA rows[0]")
print(rows[0])


head="""
    <body bgcolor="black">
    <body text="white">
    <h1>CONSULTA DE EVENTOS</h1>

    <h2>Filtro: <em>"""+texto+"""</em> </h2> <!-- texto va a ser el filtro de busqueda en los querys-->

    <table bgcolor="white">
        <tr bgcolor="black">
            <th width=150>FECHAID</th>
            <th width=150>TICKET</th>
            <th width=150>USUARIO</th>
            <th width=1300>EVENTO</th>
        </tr>
        

    """

def generating_file(rows):
    
    table= """
        <tr bgcolor="black" align="center">
            <td>"""+str(rows[0])+"""</td> 
            <td>"""+str(rows[1])+"""</td>
            <td>"""+str(rows[2])+"""</td>
            <td align="left">"""+rows[3]+"""</td>
        </tr>
            """
    print(table)
    return table

end= "</table>"

text=""
for row in rows:
    text+=generating_file(row)
#print(text)

print("INICIO")
print(head+text+end)