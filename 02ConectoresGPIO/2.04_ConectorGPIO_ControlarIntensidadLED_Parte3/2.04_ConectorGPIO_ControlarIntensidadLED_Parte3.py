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
# en una variable guardamos el valor de PWM para el GPIO18
pwm_led=GPIO.PWM(18,500)
# iniciamos el led con longitud de pulso 100
pwm_led.start(100)
# bucle que se repetira hasta finalizar el programa
while(True):
    # disminuimos longitud del pulso
    pwm_led.ChangeDutyCycle(25)
    # esperamos medio segundo
    time.sleep(0.5)
    # aumentamos longitud del pulso
    pwm_led.ChangeDutyCycle(100)
    # esperamos medio segundo
    time.sleep(0.5)