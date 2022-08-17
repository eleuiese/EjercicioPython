##Dependencias necesarias
import csv
import mysql.connector
from encodings import utf_8
import pandas as pd
import os

#Creación del archivo de salida en .csv para luego ser convertido a .xlsx
f = open('datos.csv', 'w')

#Lectura por lineas del archivo datos.txt
with open("datos.txt") as f:
    contents = f.readlines()

#Separación por vectores de las cadenas de texto separadas por espacios
str = contents[0]
arr0 = str.split(" ",1)
str = contents[1]
arr1 = str.split(" ",1)
str = contents[2]
arr2 = str.split(" ",1)
str = contents[11]
arr3 = str.split(" ",1)
str = contents[12]
arr4 = str.split(" ",1)
str = contents[13]
arr5 = str.split(" ",1)

#Extracción de los datos tipos JSON del archivo datos.txt y creación de dos nuevos archivos para procesamiento.
with open("data1.json",'w') as f:
    for line in contents[4:10]:
        f.write(line)

with open("data2.json",'w') as f:
    for line in contents[15:21]:
        f.write(line)

#Conversión de archivos JSON a .csv
pdObj = pd.read_json('data1.json', orient='index')
pdObj.to_csv('data1.txt', index=True)

pdObj = pd.read_json('data2.json', orient='index')
pdObj.to_csv('data2.txt', index=True)

#Lectura por líneas de los .csv obtenidos de los JSON anteriores
with open("data1.txt") as f:
    contents = f.readlines()
str = contents[1]
arr6 = str.split(",",1)
str = contents[2]
arr7 = str.split(",",1)
str = contents[3]
arr8 = str.split(",",1)
str = contents[4]
arr9 = str.split(",",1)

with open("data2.txt") as f:
    contents = f.readlines()
str = contents[1]
arr10 = str.split(",",1)
str = contents[2]
arr11 = str.split(",",1)
str = contents[3]
arr12 = str.split(",",1)
str = contents[4]
arr13 = str.split(",",1)


#Creación del header para el archivo .csv (nombres de las columnas)
header = [arr0[0], arr1[0], arr2[0], arr6[0], arr7[0], arr8[0], arr9[0]]

#Creacion de vector con datos procesados para almacenar en el .csv
daticos = [
   [arr0[1], arr1[1], arr2[1], arr6[1], arr7[1], arr8[1], arr9[1]],
   [arr3[1], arr4[1], arr5[1], arr10[1], arr11[1], arr12[1], arr13[1]]
         ]
#Escritura de datos en el .csv
with open('datos.csv', 'w', encoding='utf_8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(daticos)

#Conversión de .csv a .xlsx
read_file = pd.read_csv (r'datos.csv')
read_file.to_excel (r'datos.xlsx', index = None, header=True)

#Depuración de archivos auxiliares
os.remove("data1.txt")
os.remove("data2.json")
os.remove("data2.txt")
os.remove("data1.json")
os.remove("datos.csv")

#Conexión con base de datos local generada desde archivo docker-compose.yml 
conn = mysql.connector.connect(
   user='bdbuser', password='bdbroot', host='127.0.0.1', database='db')
cursor = conn.cursor()

#Creación de solicitud SQL mediante inserción dinámica 
insert_stmt = (
   "INSERT INTO Datos(Cedula, Nombres, Direccion, latitude, longitude, city, description)"
   "VALUES (%s, %s, %s, %s, %s, %s, %s)"
)

daticos1 = (arr0[1], arr1[1], arr2[1], arr6[1], arr7[1], arr8[1], arr9[1])
daticos2 = (arr3[1], arr4[1], arr5[1], arr10[1], arr11[1], arr12[1], arr13[1])

#Ejecución del comando SQL
try:
   cursor.execute(insert_stmt, daticos1)
   cursor.execute(insert_stmt, daticos2)

   #Confirmación de la inserción sobre la base de datos
   
   conn.commit()

except:

   #Excepción del proceso en caso de error
   conn.rollback()

#Notificación de inserción exitosa
print("Data inserted")

#Cierre de la conexión
conn.close()