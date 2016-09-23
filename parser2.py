archivo=open("TablaLocalizacion.csv","r")
archivo2=open("toychato.csv","w")
for linea in archivo:
	lista=linea.strip().split(";")
	archivo2.write(lista[0]+";"+lista[1]+";"+lista[2]+";#"+lista[3]+"#;#"+lista[4]+"#;"+lista[5]+";"+lista[6]+";"+"\n")
archivo2.close()
archivo.close()