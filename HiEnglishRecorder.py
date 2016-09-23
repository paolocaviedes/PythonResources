from distutils.core import setup
import py2exe
import requests
import os
import time

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

clear = lambda: os.system('cls')

mitoken= "NzZhYjljMTktYTNmNi00MWFmLTg4ZmUtNzQ1OTE5ZDU5YjE4MDk4NDBkOGYtZTY1"

levelHiEnglish="Y2lzY29zcGFyazovL3VzL1JPT00vM2QxOTVjNDAtNGViOC0xMWU2LWFmODEtMDU0YjhhZWUyNzMz"
levelBeginner="Y2lzY29zcGFyazovL3VzL1JPT00vZDg3OGY5NzAtNWQ4MS0xMWU2LWFhZDctZmI3OTZkM2MzNDNl"
levelElementary="Y2lzY29zcGFyazovL3VzL1JPT00vZmViOGZmNDAtNWQ4MS0xMWU2LWFiNmUtYmQyYmIwZGI5OTc3"
levelIntermediate="Y2lzY29zcGFyazovL3VzL1JPT00vMDI5YTU4MjAtNWQ4Mi0xMWU2LTg0MWYtYzc2ZWQ1NjgyYzg0"
levelAdvanced="Y2lzY29zcGFyazovL3VzL1JPT00vMTYyYWUzYTAtNWQ4Mi0xMWU2LWFhZDctZmI3OTZkM2MzNDNl"

#   main   #
print "------------------- Welcome to Spark Recorder --------------------"
print "-                                                                -"
print "- Please select 1 option:                                        -"
print "-                                                                -"
print "- Opt 1 - Send message                                           -"
print "- Opt 2 - Cancel class                                           -"
print "------------------------------------------------------------------"
mainopt=int(raw_input(">>>   "))
#   validate option  #
while mainopt!=1 and mainopt!=2:
	clear()
	print "------------------- Welcome to Spark Recorder --------------------"
	print "-                                                                -"
	print "- Please select 1 option:                                        -"
	print "-                                                                -"
	print "- Opt 1 - Send message                                           -"
	print "- Opt 2 - Cancel class                                           -"
	print "------------------------------------------------------------------"
	print "                                                                  "
	print "Opcion invalida, favor reingrese"
	mainopt=int(raw_input(">>>   "))


#   main   #
print "-------------------      Spark Recorder       --------------------"
print "-                                                                -"
print "- Please select 1 option:                                        -"
print "-                                                                -"
print "- Opt 1 - HiEnglish                                              -"
print "- Opt 2 - Beginner                                               -"
print "- Opt 3 - Elementary                                             -"
print "- Opt 4 - Intermediate                                           -"
print "- Opt 5 - Advanced                                               -"
print "------------------------------------------------------------------"
opt=int(raw_input(">>>   "))

#   validate option  #
while opt!=1 and opt!=2 and opt!=3 and opt!=4 and opt!=5:
	clear()
	print "-------------------      Spark Recorder       --------------------"
	print "-                                                                -"
	print "- Please select 1 option:                                        -"
	print "-                                                                -"
	print "- Opt 1 - HiEnglish                                              -"
	print "- Opt 2 - Beginner                                               -"
	print "- Opt 3 - Elementary                                             -"
	print "- Opt 4 - Intermediate                                           -"
	print "- Opt 5 - Advanced                                               -"
	print "------------------------------------------------------------------"
	print "                                                                  "
	print "Opcion invalida, favor reingrese"
	opt=int(raw_input(">>>   "))

if opt==1:
	level=levelHiEnglish
elif opt==2:
	level=levelBeginner
elif opt==3:
	level=levelElementary
elif opt==4:
	level=levelIntermediate
elif opt==5:
	level=levelAdvanced

if mainopt==1:
	minutes=int(raw_input("Ingrese los minutos a empezar: "))

	msje="Dear participant, your coffee break starts in "+str(minutes)+" minutes. Ignore this message if you are ready with your coffee break today!"

elif mainopt==2:
	msje="no va la clase"


#print level


try:
	SendSparkMessage(mitoken,level,msje)
	print "Mensaje enviado correctamente, Adios"
	time.sleep(2)
except:
	print "Ups, mensaje no enviado, contacte a Paolo :)"
	time.sleep(2)
