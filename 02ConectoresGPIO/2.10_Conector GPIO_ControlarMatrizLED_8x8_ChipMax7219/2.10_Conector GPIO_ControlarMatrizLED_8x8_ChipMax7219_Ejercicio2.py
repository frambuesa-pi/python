# importamos la libreria GPIO
import RPi.GPIO as  GPIO
# desactivamos mensajes de error GPIO
GPIO.setwarnings(False)
# importamos las librerias necesarias para trabajar con
# la matriz led 8x8
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi
from luma.core.legacy import text
# importamos libreria time
import time
# inicializamos los objetos para el dispositivo
serial=spi(port=0,device=0)
device=max7219(serial)
# guardamos en una variable el texto que queremos mostrar
msg = "X"
# mostramos un texto fijo en la matriz led
with canvas(device) as draw:
    text(draw, (0, 0), msg, fill="white")
# creamos doble bucle que aumenta el brillo del texto
for x in range(5):
    for intensity in range(16):
        device.contrast(intensity * 16)
        time.sleep(0.5)