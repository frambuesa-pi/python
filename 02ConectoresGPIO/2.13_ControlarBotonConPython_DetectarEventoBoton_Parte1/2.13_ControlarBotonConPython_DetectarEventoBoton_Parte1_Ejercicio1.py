# importamos la librerias necesarias
import RPi.GPIO as GPIO
import time
# indicamos el uso de  la identificacion BCM para los GPIO
GPIO.setmode(GPIO.BCM)
# definimos una funcion que al ejecutarla muestra un texto
def boton_press(channel):
    print('Boton presionado')
# configuramos el pin 18 como de entrada y activamos la
# resistencia de activacion del pin 18 con PUD_UP
# esto hace que al presionar el boton se interrumpa la
# tension de 3,3V del pin
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)
# con el siguiente evento detectamos si hemos presionado el
# boton y ejecutamos la funcion
GPIO.add_event_detect(18,GPIO.FALLING,callback=boton_press)
# creamos un bucle que muestra los segundos trasncurridos
# i detiene la ejecucion un segundo
i=0
while True:
    i=i+1
    print(i)
    time.sleep(1)