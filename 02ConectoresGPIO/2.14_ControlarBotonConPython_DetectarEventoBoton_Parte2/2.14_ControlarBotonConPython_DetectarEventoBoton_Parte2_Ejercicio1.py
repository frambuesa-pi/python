# importamos librerias
import RPi.GPIO as GPIO
import time
# indicamos el uso de  la identificacion BCM para los GPIO
GPIO.setmode(GPIO.BCM)
# configuramos el pin 18 como entrada y activamos 
# la resistencia de activacion del pin 18 con PUD_UP
# esto hará que al presionar el botón se interrumpe
# la tensión de 3,3V del pin
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)
# bucle infinito que recoge el estado de la resistencia
# del pin18, si el estado es Falso (interrupción 3,3V) 
# mostramos el texto boton presionado
while True:
    input_state=GPIO.input(18)
    if input_state==False:
        print('Boton presionado')
        time.sleep(0.2)