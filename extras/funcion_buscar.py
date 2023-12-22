import sqlite3
import webbrowser

texto='"%izopsws%"'
print(texto)

connection = sqlite3.connect("C:/Users/Joel/Desktop/GUI_bita/IT_database.db")
cursor = connection.cursor()
#print(f"SELECT DATEID, TICKET, USERID, EVENT FROM EVENTS WHERE EVENT LIKE {texto}")
cursor.execute(f"SELECT DATEID, TICKET, USERID, EVENT FROM EVENTS WHERE EVENT LIKE {texto}")
rows= cursor.fetchall()
print(rows)

print("LISTA rows[0]")
print(rows[0])
#print("STRING rows[0]")
#print(str(rows[0]))

#chain=str(rows[0]).split(",")
#print("Y ESTE?")
#print(chain[0])

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

f = open("extras/table.html", "w")
f.write(head+text+end)
#f.close

f = open("extras/table.html", "r")
print(f.read())

webbrowser.open("C:/Users/Joel/Desktop/GUI_bita/extras/table.html")