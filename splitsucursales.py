archivo=open("fuentesucursales.txt","r")
archivo2=open("lista.txt","w")
count=0
for linea in archivo:
	cadena=""
	for i in range(len(linea)):		
		if linea[i]=="|" and linea[i+1]=="#" and linea[i+2]=="|":
			archivo2.write(cadena+"\n")
			cadena=""
		else:
			cadena+=str(linea[i])
archivo.close()
archivo2.close()


