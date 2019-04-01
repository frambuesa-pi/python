# importamos la libreria GPIO
import RPi.GPIO as  GPIO
# desactivamos mensajes error de GPIO
GPIO.setwarnings(False)
# importamos las librerias necesarias para trabajar con
# la matriz led 8x8
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi
from luma.core.render import canvas
# importamos la libreria time
import time
# inicializamos los objetos para el dispositivo
serial=spi(port=0,device=0)
device=max7219(serial)
# mostramos un recuadro con el borde iluminado
with canvas(device) as draw:
    draw.rectangle(device.bounding_box,outline="white", fill="black")
# tiempo espera de dos segundos
time.sleep(2)
# mostramos un recuadro con el interior iluminado
with canvas(device) as draw:
    draw.rectangle(device.bounding_box,outline="black", fill="white")