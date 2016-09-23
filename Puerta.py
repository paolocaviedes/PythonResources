#SMARTDOOR

#Seccion de importacion de librerias.
import time
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

while True:

   LCD.lcd_string(" SMARTDOOR ",LCD.LINE_1)
   LCD.lcd_string(" rele puerta ",LCD.LINE_2)
   GPIO.output(PUERTA,True)
   time.sleep(3)
   GPIO.output(PUERTA,False)

   LCD.lcd_string(" SMARTDOOR ",LCD.LINE_1)
   LCD.lcd_string(" Transistor porton ",LCD.LINE_2)
   GPIO.output(PORTON,True)
   time.sleep(3)
   GPIO.output(PORTON,False)   

   LCD.lcd_string(" SMARTDOOR ",LCD.LINE_1)
   LCD.lcd_string(" led ",LCD.LINE_2)
   GPIO.output(LED,True)
   time.sleep(3)
   GPIO.output(LED,False)

   LCD.lcd_string(" LA HORA ES: ",LCD.LINE_1)
   LCD.lcd_string(str(time.strftime(" %H:%M:%S ")),LCD.LINE_2)

   time.sleep(3)


   flag = 1

   while flag:
      LCD.lcd_string(" PRESIONE Y MAN- ",LCD.LINE_1)
      LCD.lcd_string(" TENGA UN BOTON ",LCD.LINE_2)

      if GPIO.input(SW1) == 0:
         while GPIO.input(SW1) == 0:
            LCD.lcd_string(" BOTON PRESIONADO ",LCD.LINE_1)
            LCD.lcd_string("   Switch 1 ",LCD.LINE_2)
            GPIO.output(BUZZER,True)
         flag = 0
         GPIO.output(BUZZER,False)

      if GPIO.input(SW2) == 0:
         while GPIO.input(SW2) == 0:
            LCD.lcd_string(" BOTON PRESIONADO ",LCD.LINE_1)
            LCD.lcd_string("   Switch 2 ",LCD.LINE_2)
            GPIO.output(BUZZER,True)
         flag = 0
         GPIO.output(BUZZER,False)

      if GPIO.input(SW3) == 0:
         while GPIO.input(SW3) == 0:
            LCD.lcd_string(" BOTON PRESIONADO ",LCD.LINE_1)
            LCD.lcd_string("   Switch 3 ",LCD.LINE_2)
            GPIO.output(BUZZER,True)
         flag = 0
         GPIO.output(BUZZER,False)

   time.sleep(1)




GPIO.cleanup()