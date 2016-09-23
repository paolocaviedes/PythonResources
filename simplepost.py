import requests

def movercam(id,direccion):
	url = "http://192.168.29.79/putxml"

	payload = "<Command>\r\n<Camera>\r\n<Ramp>\r\n<CameraId>"+str(id)+"</CameraId>\r\n<Pan>"+str(direccion)+"</Pan>\r\n<PanSpeed>15</PanSpeed>\r\n</Ramp>\r\n</Camera>\r\n</Command>"
	headers = {
	    'content-type': "text/xml",
	    'authorization': "Basic YWRtaW46MTIzNDU=",
	    'cache-control': "no-cache",
	    'postman-token': "38400a68-77c1-b8a3-e494-6c3257b5b0dd"
	    }

	response = requests.request("POST", url, data=payload, headers=headers)

	print(response.text)


direccion=str(raw_input("ingrese direccion:"))
movercam(1,direccion)
while direccion!="0":
	direccion=str(raw_input("ingrese direccion:"))
	movercam(1,direccion)
