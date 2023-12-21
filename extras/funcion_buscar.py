import sqlite3

texto="FILTRO"

connection = sqlite3.connect("C:/Users/Joel/Desktop/GUI_bita/IT_database.db")
cursor = connection.cursor()
cursor.execute("Select DATEID, TICKET, USERID, EVENT from EVENTS ")
rows= cursor.fetchall()
print(rows)

print("LISTA rows[0]")
print(rows[0])
#print("STRING rows[0]")
#print(str(rows[0]))

#chain=str(rows[0]).split(",")
#print("Y ESTE?")
#print(chain[0])

def generating_file(rows):
    #print(rows)
    #print(type(rows[0]))
    #chain=str(rows[0])                   #.split(",")
    #print(chain)
    
    head_filter= """
    <body bgcolor="black">
    <body text="white">
    <h1>CONSULTA DE EVENTOS</h1>

    <h2>Filtro: <em>"""+texto+"""</em> </h2> <!-- texto va a ser el filtro de busqueda en los querys-->

    """
    
    table= """
    <table bgcolor="white">
        <tr bgcolor="black">
            <th width=150>FECHAID</th>
            <th width=150>TICKET</th>
            <th width=150>USUARIO</th>
            <th width=1300>EVENTO</th>
        </tr>
        <tr bgcolor="black" align="center">
            <td>"""+str(rows[0])+"""</td> 
            <td>"""+str(rows[1])+"""</td>
            <td>"""+str(rows[2])+"""</td>
            <td align="left">"""+rows[3]+"""</td>
            </tr>
        </table>
    """
    print(head_filter+table)
    return head_filter+table

text=""
for row in rows:
    text+=generating_file(row)
print(text)