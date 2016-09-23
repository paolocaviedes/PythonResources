archivo=open("nuevo.txt","r")
archivo2=open("TablaLocalizacion.csv","w")

conjuntofinal=set()

count=0
for linea in archivo:
	count+=1
	lista=linea.strip().split(";")
	sucursal=lista[0]
	direccion=lista[1]
	atencion=lista[2]
	lat=lista[3].split(",")[0]
	lon=lista[3].split(",")[1]
	localidad=lista[6]
	region=lista[7]
	tupla=(sucursal,localidad,direccion,lat,lon,"Chile",region)
	conjuntofinal.add(tupla)

archivo2.write("sucursal;localidad;address;lat;lon;pais;region\n")
for (suc,loc,addr,lat,lon,country,reg) in conjuntofinal:
	archivo2.write(suc+";"+loc+";"+addr+";"+lat+";"+lon+";"+country+";"+reg+"\n")

archivo.close()
archivo2.close()