import re
import sqlite3
import subprocess

from tkinter import messagebox
from datetime import date

file = open("paths.txt", "r")

str_file=file.read()
#print(file.read())

path= re.findall("[A-Z].*db", str_file)[0]
search= re.findall("[A-Z].*html", str_file)[0]
ind= re.findall("[A-Z].*sql", str_file)[0]


text_about= """
BITÁCORA DE SISTEMAS 
Versión 1.10.0
2024

Sistema Satelital Mexicano
MEXSAT

Gerencia del Centro de Control Satelital Iztapalapa
Coordinación de Sistemas


DESARROLLO

Ing. Joel Carbajal Muñoz


AGRADECIMIENTOS

Ing. Andrea Mijaru Sánchez Hernández

Ing. Roberto Cadena Vega

M. en C. Jorge Tlacaelel Cruz García

América Citlalli Hernández Vargas

"""
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
En el menú Archivo > Indicadores se exporta un archivo Excel
con todos los eventos en la bitácora de la base de datos.

Nota: Si la bitácora ya cuenta con demasiados registros
esto podría causar que la aplicación se bloquee, ya que
no se está delimitando el periodo.
Para ello se pensó en un formato para delimitar el periodo
de tiempo que se desea exportar.

FORMATO PARA HACER EXPORTACIONES

Desde la barra de Búsqueda se pueden exportar los indicadores en lapsos de tiempo. 
El formato correcto para hacer una exportación es el siguiente:

ind: YYYYMMDDII - YYYYMMDDII

ind: - Indica a la bitácora que solicita INDICADORES:
YYYY - AÑO
MM - MES
DD  - DÍA 
II     - IDENTIFICADOR

Hay consideraciones que se deben de tener en cuenta cuando se utiliza esta función de la bitácora.
Para hacer exportaciones es necesario contar con un 
periodo de tiempo (limite inferior - limite superior).
Ejemplo: ind: 2023000000 - 2024000000 
Resultado: Eventos del año 2023
Ejemplo: ind: 2023010000 - 2023020000 
Resultado: Eventos del año 2023 mes de enero

Considerando los ejemplos, se pueden variar los lapsos de tiempo que el usuario necesite.

Recuerdatorio: Respeta el espacio después de ind: y los espacios en el guion medio -
"""

View_TV= """VISUALIZACIÓN
En la tabla principal se puede observar los cinco eventos más recientes.

1.er Columna - Fecha en formato YY.MM.DD(ID)
        Y - Year
      M - Month
       D - Day
    (ID) - Identifier per day
Lo que significa que el identificador incrementará en un mismo día.
Reiniciando el identificador en un día diferente.

2.da Columna - Ticket en formato ###-YY 
     ### - Número consecutivo, completando con 0 (ceros) 
               las posiciones a la izquierda. Ejemplo para el primer 
               ticket del año 001.
        YY - Year. Dos posiciones para el año en curso 26 = 2026.
               El ticket es asignado por el usuario y es 
               indispensable que el usuario sepa cuál fue 
               el último número de ticket utilizado para asignar él 
               consecutivo a la nueva incidencia.

3.er Columna - Usuario
El usuario es seleccionado desde la ventana de Eventos. El cual cuenta con tres opciones:
     -Coordinaror
     -Analista
     -Invitado

4.a Columna - Evento
Breve visualización del evento

Si el usuario desea visualizar más eventos solo tiene que localizarse dentro de la tabla y "scrollear" hacia abajo. Los eventos en la tabla principal cubren el año en curso y el anterior.
Todos los eventos se encuentran en la base de datos de sistemas.
"""

Search= """Para realizar una búsqueda se necesita escribir una palabra clave en la barra de Búsqueda de la ventana principal.
Dado que la visualización de eventos en la tabla principal está limitada. El usuario puede hacer búsquedas por año directamente en la barra de Búsqueda.
Si el usuario conoce el identificador completo, como lo es:
YY.MM.DD(ID) 
También se puede buscar por el formato completo de identificador. El cual es:
YYYYMMDDID
Si el usuario desease visualizar todos los eventos registrados en la bitácora solo tiene que dar click en el botón de Buscar con el campo de búsqueda en blanco.
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
     
#print(str(int(generator_dateID()[:4])-1)+"000000")
QUERY_TV="""   SELECT EVENTS.DATEID, EVENTS.TICKET, EVENTS.USERID, EVENTS.EVENT, MARKSMX2.ATINCMX2, MARKSMX3.ATINCMX3 
                    FROM EVENTS
                    LEFT JOIN MARKSMX2 
                    ON EVENTS.DATEID = MARKSMX2.DATEID 
                    LEFT JOIN MARKSMX3 
                    ON EVENTS.DATEID = MARKSMX3.DATEID
                    WHERE EVENTS.DATEID >="""+str(int(generator_dateID()[:4])-1)+"000000"";"  #<-- Delimitar los años en el treeview



def exporting ():
        subprocess.call(["sqlite3", "IT_database.db", ". read QUERY_TO_EXPORT.sql"], shell=True)

def ind_info ():
        messagebox.showinfo("INFORMACIÓN DE INDICADORES", Ind_Info)


################################################## FSS #############################################
def fss():
     return subprocess.Popen(r'explorer "Z:\Documentation Library\Subsystem Engineering Training\"')


####################################### MSS ###########################################################
def mss():
     return subprocess.Popen(r'explorer "Z:\Documentation Library\Subsystem Engineering System-MSS"')


################################# EPOCH T&C #########################################################
def epoch_t_and_c():
     return subprocess.Popen(r'explorer Z:\Documentation Library\ISI\EPOCH\EPOCH T&C Server 4.12.3.1\"')


################################# EPOCH USER TRAINING ################################################
def epoch_user_training():
     return subprocess.Popen(r'explorer "Z:\Documentation Library\ISI\MEXSAT\Training\2012-04 EPOCH User Training\slides"')


############################ EPOCH MAINTENANCE TRAINING ###############################################
def epoch_maintenance_training():
     return subprocess.Popen(r'explorer "Z:\Documentation Library\ISI\MEXSAT\Training\2012-05 EPOCH Maintenance Training"')


#################################### ARES ###########################################################
def ares():
     return subprocess.Popen(r'explorer "Z:\Documentation Library\ISI\EPOCH\ARES 4.12.3.0"')


################################### SERVIDORES #####################################################
def servidores():
     return subprocess.Popen(r'explorer "Z:\Documentation Library\Documentacion Servidores"')


########################################## ARCHIVE MANAGER ########################################################################
def archive_manager():
     return subprocess.Popen(r"Z:\Documentation Library\ISI\EPOCH\Archive Manager 4.12.0\Archive Manager 4.12.3.0.pdf",shell=True)


############################### TASK INITIATOR ########################################################
def task_initiator():
     return subprocess.Popen(r'explorer "Z:\Documentation Library\ISI\EPOCH\Task Initiator 4.12.0"')


############################ SYSTEM DOCUMENTS ###########################################################
def system_documents():
     return subprocess.Popen(r'explorer "Z:\Documentation Library\ISI\MEXSAT\System Documents"')


########################################## COMPASS ##################################################
def compass():
     return subprocess.Popen(r'explorer "Z:\Documentation Library\Compass"')


############################# ENCRIPTORES #########################################################################
def encriptores():
     return subprocess.Popen(r"Z:\Documentation Library\Encriptores\Centurion encryptor key loading.pdf",shell=True)


######################################### 3COM #####################################################
def three_com():
     return subprocess.Popen(r'explorer "Z:\Documentation Library\3com"')


##################################### Tree View Info ########################################################
def TV_info ():
        messagebox.showinfo("Visualización de eventos en la tabla principal", View_TV)


##################################### Search ########################################################
def Search_info ():
        messagebox.showinfo("Busquedas", Search)