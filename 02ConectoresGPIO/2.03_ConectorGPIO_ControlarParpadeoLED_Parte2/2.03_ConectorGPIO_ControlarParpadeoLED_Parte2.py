#############################################
#_____https://frambuesa-pi.blogspot.com/____#
#___https://github.com/frambuesa-pi/python__#
#############################################
# importamos la libreria GPIO
import RPi.GPIO as GPIO
# importamos la libreria time
import time
# desactivamos mensajes de error
GPIO.setwarnings(False)
# indicamos el uso de la identificacion BCM para los GPIO
GPIO.setmode(GPIO.BCM)
# indicamos que el GPIO18 es de salida de corriente
GPIO.setup(18,GPIO.OUT)
# bucle que se repetira hasta finalizar el programa
while(True):
    # damos salida de corriente al pin GPIO18
    GPIO.output(18,True)
    # esperamos medio segundo
    time.sleep(0.5)
    # finalizamos la salida de corriente del pin GPIO18
    GPIO.output(18,False)
    # esperamos medio segundo
    time.sleep(0.5)