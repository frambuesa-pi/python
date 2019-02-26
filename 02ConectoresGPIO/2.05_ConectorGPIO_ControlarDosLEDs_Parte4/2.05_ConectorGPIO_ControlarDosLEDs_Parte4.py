#############################################
#_____https://frambuesa-pi.blogspot.com/____#
#___https://github.com/frambuesa-pi/python__#
#############################################
# importamos la libreria GPIO
import RPi.GPIO as GPIO
# creamos una lista con los pines GPIO
pins=[18,23]
# creamos una lista con tres registros 0,1,2
# cada uno tiene dos valores el primero es el
# estado del pin1 (18) y el segundo, del pin2 (23)
pin_led_states=[[0,1], # A
                [1,0], # B
                [0,0], # apagado
                ]
# definimos el tipo de identificacion de los puertos GPIO
GPIO.setmode(GPIO.BCM)
# definimos una funcion para camnbiar el estado del GPIO
# recibe 2 parametros, el pin y el estado
def set_pin(pin_index,pin_state):
    # definimos el estado del pin como de salida
    GPIO.setup(pins[pin_index],GPIO.OUT)
    # cambiamos el estado del pin a 0 o 1
    GPIO.output(pins[pin_index],pin_state)
# definimos una funcion que recibe un parametro 0,1 o 2
def light_led(led_number):
    # bucle que recupera valores de la lista de pin_led_states
    for pin_index, pin_state in enumerate(pin_led_states[led_number]):
        # llamamos a la funcion que cambia el estado de los pines
        # activando o desactivando los leds
        set_pin(pin_index,pin_state)
# por defecto ponemos el pin 0 a estado 0
set_pin(0,0)
# por defecto ponemos el pin 1 a estado 0
set_pin(1,0)
# bucle que se repite indefinidamente
while True:
    # pedimos al usuario que introduzca un valor
    x=int(input("Pin (0 to 2):"))
    # llamamos a la funcion
    light_led(x)
