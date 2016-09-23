import mysql.connector

cnx = mysql.connector.connect(user='ZEUS',password='zeus', database='casys')

"""
#funcion de realiza la insercion a la tabla localizacion
def insertIntoLocalizacion(localidad,direccion,lat,lon,pais,region):
	cursor = cnx.cursor()
	add_localizacion = ("INSERT INTO localizacion "
	               "(localidad, direccion, lat, lon, pais, region) "
	               "VALUES (%s, %s, %s, %s, %s, %s)")

	data_localizacion = (localidad, direccion, lat, lon, pais,region)

	# Insert new employee
	cursor.execute(add_localizacion, data_localizacion)
	emp_no = cursor.lastrowid

	# Make sure data is committed to the database
	cnx.commit()
	cursor.close()
#no retorna nada

#lectura del archivo con las sucursales
archivo=open("fuenteparainsercion.csv","r")
for linea in archivo:
	lista=linea.strip().split(";")
	insertIntoLocalizacion(lista[1],lista[2],lista[3],lista[4],lista[5],lista[6])

"""

cnx.close()