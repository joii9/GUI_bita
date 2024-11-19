import re
import sqlite3

from datetime import date

file = open("paths.txt", "r")

str_file=file.read()
#print(file.read())

path= re.findall("[A-Z].*db", str_file)[0]
search= re.findall("[A-Z].*html", str_file)[0]
ind= re.findall("[A-Z].*sql", str_file)[0]


text_about= """
BITACORA DE SISTEMAS 
Version 2.2.1
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
QUERY_TV="""   SELECT EVENTS.DATEID, EVENTS.TICKET, EVENTS.USERID, EVENTS.EVENT, MARKSMX2.ATINCMX2, MARKSMX3.ATINCMX3 
                    FROM EVENTS 
                    LEFT JOIN MARKSMX2 
                    ON EVENTS.DATEID = MARKSMX2.DATEID 
                    LEFT JOIN MARKSMX3 
                    ON EVENTS.DATEID = MARKSMX3.DATEID;"""

Info="""El formato correcto es:

ind: YYYYMMDDII - YYYYMMDDII

YYYY cuatro digitos para el año
MM dos digitos para el mes
DD  dos digitos para el día
II      dos digitos para el identificador

Respeta el espacio depues de ind: y los espacios en el guion medio -

Consulta la información de indicadores en el menú
Help > Info. indicadores
"""

Ind_Info="""INDICADORES
En el menú File > Indicadores se exporta un archivo excel
con todos los eventos en la bitacora de la base de datos.

Nota: Si la bitacora ya cuenta con demasiados registros
esto podria causar que la aplicación se bloquee ya que
no se esta delimitando el periodo.
Para ello se pensó en un formato para delimitar el periodo
de tiempo que se desea exportar.

FORMATO PARA HACER EXPORTACIONES

Desde la barra de BUSQUEDA se pueden exportar los indicadores en lapsos de tiempo. 
El formato correcto para hacer una exportación es el siguiente:

ind: YYYYMMDDII - YYYYMMDDII

ind: - Indica a la bitacora que solicita INDICADORES:
YYYY - AÑO
MM - MES
DD  - DÍA 
II     - IDENTIFICADOR

Hay consideraciones que se deben de tener en cuenta cuando se utiliza esta función de la bitacora.
Para hacer exportaciones es necesario contar con un 
periodo de tiempo (limite inferior - limite superior).
Ejemplo: ind: 2023000000 - 2024000000 
Resultado: Eventos del año 2023
Ejemplo: ind: 2023010000 - 2023020000 
Resultado: Eventos del año 2023 mes de enero

Considerando los ejemplos, se pueden variar los lapsos de tiempo que el usuario necesite.

Recuerdatorio: Respeta el espacio depués de ind: y los espacios en el guion medio -
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