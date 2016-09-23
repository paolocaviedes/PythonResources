#SMARTDOOR

#Seccion de importacion de librerias.
from SparkModule import SendSparkMessage,SeeSparkTokens,listSparkMessages
import time
import re
import LCDLIB16x2 as LCD
import RPi.GPIO as GPIO

#Limpieza de puerto GPIO
#GPIO.cleanup() 

#Definicion de pines de GPIO
LED = 4
BUZZER = 22
SW1 = 11
SW2 = 9
SW3 = 10
PORTON = 17
PUERTA = 27

LCD_RS = 14
LCD_E = 15
LCD_D4 = 18
LCD_D5 = 23
LCD_D6 = 24
LCD_D7 = 25


GPIO.setmode(GPIO.BCM)

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(SW1, GPIO.IN)   # Configuracion Push-down
GPIO.setup(SW2, GPIO.IN)   # Configuracion Push-down
GPIO.setup(SW3, GPIO.IN)   # Configuracion Push-down
GPIO.setup(PORTON, GPIO.OUT)
GPIO.setup(PUERTA, GPIO.OUT)

# Inicializa Display LCD

LCD.lcd_init()


#definicion de fecha del sistema
FechaHora=time.strftime("%Y%m%d-%H%M%S")

SmartDoor="ZTBhM2FiYzctNTRlMi00NjkzLThiZGQtMjgzNDAwZmY1MmZlMWJiZTJmMjMtM2I5"

log=open("LogdeIngreso"+FechaHora+".csv","w")
log.write("Fecha-Hora;User;Pass;Response;\n")


flag=True
estado=0

while flag:
	time.sleep(1)
	Rooms=SeeSparkTokens(SmartDoor)
	for (rmte,room) in Rooms:
		try:
			print "escuchando"
			LCD.lcd_string(" SMARTDOOR ",LCD.LINE_1)
			LCD.lcd_string(" Listening... ", LCD.LINE_2)

			LastMsje=listSparkMessages(SmartDoor,room)[0]
			Remitente=LastMsje[1]
			#print Remitente
			Msje=LastMsje[3]
			Hora=LastMsje[2]
			if Remitente!="smartdoor@sparkbot.io":

				busqueda=re.search("[a-zA-z.]*@",Remitente)
				acierto=busqueda.group(0)[:-1].split(".")
				nombre=acierto[0].capitalize()+" "+acierto[1].capitalize()
				busqueda2=re.search("@[A-Za-z]*.cl",Remitente)
				acierto2=busqueda2.group(0)[1:]
				mail=acierto2

				SendSparkMessage(SmartDoor,room,"Mensaje Recibido, la solicitud esta siendo procesada.")

				if mail=="hiway.cl":

					if Msje=="Puerta":
								
						SendSparkMessage(SmartDoor,room,"Correcto, Bienvenido "+nombre+". Abriendo Puerta")
						#log.write(FechaHora,Remitente,Msje,"Abriendo Puerta")
						print "abrete Puerta"

						LCD.lcd_string(" Abriendo Puerta ",LCD.LINE_1)
						LCD.lcd_string(" - ", LCD.LINE_2)
						time.sleep(1)
						LCD.lcd_string(" "+ nombre.split(" ")[0]+" ",LCD.LINE_1)
						LCD.lcd_string(" "+ nombre.split(" ")[1]+" ", LCD.LINE_2)
						print "abriendo puerta"

						GPIO.output(LED,True)
						GPIO.output(PUERTA,True)
   						time.sleep(3)
   						GPIO.output(PUERTA,False)
   						GPIO.output(LED,False)

						LCD.lcd_string(" SMARTDOOR ",LCD.LINE_1)
						LCD.lcd_string(" - ", LCD.LINE_2)
						

					elif Msje=="Porton":

						SendSparkMessage(SmartDoor,room,"Correcto, Bienvenido "+nombre+". Abriendo Porton")
						#log.write(FechaHora,Remitente,Msje,"Abriendo Porton")

						LCD.lcd_string(" Abriendo Porton ",LCD.LINE_1)
						LCD.lcd_string(" - ", LCD.LINE_2)
						time.sleep(1)
						LCD.lcd_string(" "+ nombre.split(" ")[0]+" ",LCD.LINE_1)
						LCD.lcd_string(" "+ nombre.split(" ")[1]+" ", LCD.LINE_2)
						print "abriendo porton"

						GPIO.output(LED,True)
						GPIO.output(PORTON,True)
   						time.sleep(3)
   						GPIO.output(PORTON,False)
   						GPIO.output(LED,False) 

						LCD.lcd_string(" SMARTDOOR ",LCD.LINE_1)
						LCD.lcd_string(" - ", LCD.LINE_2)
						#abrete Porton
						
					else:
						SendSparkMessage(SmartDoor,room,"Mensaje Invalido, Reintente")
						#log.write(FechaHora,Remitente,Msje,"Incorrecto")

						LCD.lcd_string(" Intento ",LCD.LINE_1)
						LCD.lcd_string(" erroneo ", LCD.LINE_2)
						time.sleep(1)
						LCD.lcd_string(" "+ nombre.split(" ")[0]+" ",LCD.LINE_1)
						LCD.lcd_string(" "+ nombre.split(" ")[1]+" ", LCD.LINE_2)

						time.sleep(3)
						LCD.lcd_string(" SMARTDOOR ",LCD.LINE_1)
						LCD.lcd_string(" - ", LCD.LINE_2)

				else:
					SendSparkMessage(SmartDoor,room,"Cuenta Invalida, contacte mesa de servicio")
			else:
				continue
		except:
			continue
