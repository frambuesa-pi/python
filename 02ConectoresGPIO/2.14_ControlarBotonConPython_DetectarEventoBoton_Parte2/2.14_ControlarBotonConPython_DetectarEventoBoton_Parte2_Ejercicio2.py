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
#  configuramos el pin 23 como salida para el led
GPIO.setup(23,GPIO.OUT)
# definimos dos variables para guardar el estado del led
# por defecto el estado del led es False (apagado)
switch_state=False
# por defecto el estado anterior es True (encendido)
old_input_state=True # activada
# bucle infinito que recoge el estado del pin18
# cada vez que presionamos el botón,el estado del switch
# alterna entre True/False
while True:
    # guardo en una variable el estado del pin
    new_input_state=GPIO.input(18)
    # si el estado es False (presionado),y el estado
    # anterior es True cambiamos el valor del switch
    if new_input_state==False and old_input_state==True:
        switch_state=not switch_state
        # tiempo de demora para evitar rebote
        time.sleep(0.3)
    # guardamos el estado actual del GPIO18
    old_input_state=new_input_state
    # modificamos el estado del led
    GPIO.output(23,switch_state)