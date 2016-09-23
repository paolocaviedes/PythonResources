import requests
import time

#ip 192.168.29.79

def pausa(sec):
	time.sleep(sec)

def moverCamara(ip,Idcam,zoom,pan,tilt):

	url = "http://"+str(ip)+"/putxml"

	payload = "<Command>\r\n<Camera>\r\n<PositionSet command=\"True\">\r\n<CameraId>"+str(Idcam)+"</CameraId>\r\n<Zoom>"+str(zoom)+"</Zoom>\r\n<Pan>"+str(pan)+"</Pan>\r\n<Tilt>"+str(tilt)+"</Tilt>\r\n</PositionSet>\r\n</Camera>\r\n</Command>"
	headers = {
	    'content-type': "text/xml",
	    'authorization': "Basic YWRtaW46MTIzNDU=",
	    'cache-control': "no-cache",
	    'postman-token': "6a4759eb-ccfc-8f79-c828-770e0b326486"
	    }

	response = requests.request("POST", url, data=payload, headers=headers)

	return(response.text)

def desplazarCamara(ip,Idcam,direccion,tiempo):
	counter=0
	flagpan=False
	flagtilt=False
	flagmove=True

	comando=direccion.lower().capitalize()
	print comando

	if comando=="Left" or comando=="Right":
		leftright=comando
		updown=""
		flagpan=True
	elif comando=="Up" or comando=="Down":
		updown=comando
		leftright=""
		flagtilt=True

	while counter<tiempo+1:
		if flagmove:
			url = "http://"+str(ip)+"/putxml"
			if flagpan:
				payload = "<Command>\r\n<Camera>\r\n<Ramp command=\"True\">\r\n<CameraId>"+str(Idcam)+"</CameraId>\r\n<Pan>"+str(leftright)+"</Pan>\r\n</Ramp>\r\n</Camera>\r\n</Command>"
			
			headers = {
			    'content-type': "text/xml",
			    'authorization': "Basic YWRtaW46MTIzNDU=",
			    'cache-control': "no-cache",
			    'postman-token': "6a4759eb-ccfc-8f79-c828-770e0b326486"
			    }

			response = requests.request("POST", url, data=payload, headers=headers)
			flagmove=False
			print (response.text)
		counter+=1
		pausa(1)

	url = "http://"+str(ip)+"/putxml"
	payload = "<Command>\r\n<Camera>\r\n<Ramp command=\"True\">\r\n<CameraId>"+str(Idcam)+"</CameraId>\r\n<Pan>Stop</Pan>\r\n</Ramp>\r\n</Camera>\r\n</Command>"
		
	headers = {
		'content-type': "text/xml",
		'authorization': "Basic YWRtaW46MTIzNDU=",
		'cache-control': "no-cache",
		'postman-token': "6a4759eb-ccfc-8f79-c828-770e0b326486"
		}

	response = requests.request("POST", url, data=payload, headers=headers)

	print (response.text)
	return "OK"
	




	



print "Ingrese posicion\n"
zoom=(raw_input("Ingrese zoom: "))
pan=(raw_input("Ingrese pan: "))
tilt=(raw_input("Ingrese tilt: "))
print moverCamara(1,zoom,pan,tilt)

"""
while zoom>-1:
	zoom=(raw_input("Ingrese zoom: "))
	if zoom!=-1:
		pan=(raw_input("Ingrese pan: "))
		tilt=(raw_input("Ingrese tilt: "))
		print moverCamara(1,zoom,pan,tilt)
"""

"""
#modificar enteros a flotantes
desplazarCamara(1,"left",1)
"""