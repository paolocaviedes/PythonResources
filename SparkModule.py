import requests

def SendSparkMessage(Token,IdRoom,Message):
	url = "https://api.ciscospark.com/v1/messages"

	payload = "{\r\n  \"roomId\" : \""+str(IdRoom)+"\",\r\n  \"text\": \""+str(Message)+"\"\r\n}"
	headers = {
	    'authorization': "Bearer "+str(Token),
	    'content-type': "application/json",
	    'cache-control': "no-cache",
	    'postman-token': "8851d330-8954-e2d0-5b6a-9f07cbf8b34c"
	    }

	response = requests.request("POST", url, data=payload, headers=headers)
	return response

def SeeSparkRooms(Token):
	listaRooms=[]
	url = "https://api.ciscospark.com/v1/rooms"

	headers = {
	    'authorization': "Bearer "+str(Token),
	    'content-type': "application/json",
	    'cache-control': "no-cache",
	    'postman-token': "3b06edb2-fbdd-0d52-c3ae-1e9dc60b2698"
	    }


	response = requests.request("GET", url, headers=headers)

	json= response.json()


	listaValues=json.values()[0]
	for dictRoom in listaValues:
		for Key,Value in dictRoom.items():
			if Key=="title":
				listaRooms.append(Value.encode("utf-8"))
	return listaRooms

def SeeSparkTokens(Token):
	listaRooms=[]
	url = "https://api.ciscospark.com/v1/rooms"

	headers = {
	    'authorization': "Bearer "+str(Token),
	    'content-type': "application/json",
	    'cache-control': "no-cache",
	    'postman-token': "3b06edb2-fbdd-0d52-c3ae-1e9dc60b2698"
	    }


	response = requests.request("GET", url, headers=headers)

	json= response.json()


	listaValues=json.values()[0]
	for dictRoom in listaValues:
		flagTitulo=False
		flagIdentifier=False
		for Key,Value in dictRoom.items():
			if Key=="title":
				titulo=Value
				flagTitulo=True
			if Key=="id":
				identifier=Value
				flagIdentifier=True
			if flagIdentifier and flagTitulo:
				listaRooms.append((titulo,identifier))
				
	return listaRooms


def listSparkMessages(Token,Tokendestino):
	url = "https://api.ciscospark.com/v1/messages"

	querystring = {"roomId":Tokendestino}

	payload = "{\n    \"title\":\"Probando API2\"\n}"
	headers = {
	    'authorization': "Bearer "+Token,
	    'content-type': "application/json",
	    'cache-control': "no-cache",
	    'postman-token': "331372b2-e3cf-8b54-bcc4-e83eea6ce920"
	    }

	response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
	json=response.json()
	listaValues=json["items"]
	listaMessages=[]
	for dictMessage in listaValues:
			message=(dictMessage["id"],dictMessage["personEmail"],dictMessage["created"],dictMessage["text"])
			listaMessages.append(message)
	return listaMessages

def seeMessagesId(Token,Tokendestino):
	url = "https://api.ciscospark.com/v1/messages"

	querystring = {"roomId":Tokendestino}

	payload = "{\n    \"title\":\"Probando API2\"\n}"
	headers = {
	    'authorization': "Bearer "+Token,
	    'content-type': "application/json",
	    'cache-control': "no-cache",
	    'postman-token': "331372b2-e3cf-8b54-bcc4-e83eea6ce920"
	    }

	response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
	json=response.json()
	listaValues=json["items"]
	listaMessages=[]
	for dictMessage in listaValues:
			message=(dictMessage["personEmail"],dictMessage["id"])
			listaMessages.append(message)
	return listaMessages

#funca
def deleteMessage(token,mssgeID):

	url = "https://api.ciscospark.com/v1/messages/"+mssgeID

	headers = {
	    'authorization': "Bearer "+token,
	    'cache-control': "no-cache",
	    'postman-token': "48203a80-e4c7-e79b-c65e-ee8aa3532114"
	    }

	response = requests.request("DELETE", url, headers=headers)

	print(response.text)
