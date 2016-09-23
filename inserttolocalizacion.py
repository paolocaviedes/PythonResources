#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost", user="root",passwd="innovacion", db="casys")
cursor = db.cursor()

try:
	recs=cursor.execute("INSERT INTO localizacion (localidad, direccion, lat, lon, pais, region) VALUES('San Javier','Arturo Prat 2662, local A y B','-35.5944255','-71.736929','Chile','Region del Maule');")
	print "Query Ok"
except:
	print "no resulto"
raw_input()