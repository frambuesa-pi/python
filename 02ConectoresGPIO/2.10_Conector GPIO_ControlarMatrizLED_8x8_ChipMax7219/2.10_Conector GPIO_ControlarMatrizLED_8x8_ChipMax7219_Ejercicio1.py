# importamos la libreria GPIO
import RPi.GPIO as  GPIO
# desactivamos mensajes error de GPIO
GPIO.setwarnings(False)
# importamos las librerias necesarias para trabajar con
# la matriz led 8x8
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi
from luma.core.legacy import show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
# inicializamos los objetos para el dispositivo
serial=spi(port=0,device=0)
device=max7219(serial)
# guardamos en una variable el texto que queremos mostrar
msg = "frambuesa-pi.blogspot.com.es"
# mostramos el texto en la matriz led 8x8 con fuente CP437
show_message(device, msg, fill="white", font=proportional(CP437_FONT))
# mostramos el texto en la matriz led 8x8 con fuente LCD_FONT
show_message(device, msg, fill="white", font=proportional(LCD_FONT))
# mostramos el texto en la matriz led 8x8 con fuente SINCLAIR_FONT
show_message(device, msg, fill="white", font=proportional(SINCLAIR_FONT))
# mostramos el texto en la matriz led 8x8 con fuente TINY_FONT
show_message(device, msg, fill="white", font=proportional(TINY_FONT))