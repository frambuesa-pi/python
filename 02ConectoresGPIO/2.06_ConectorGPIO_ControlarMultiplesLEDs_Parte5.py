#############################################
#_____https://frambuesa-pi.blogspot.com/____#
#___https://github.com/frambuesa-pi/python__#
#############################################
# importamos la libreria GPIO
import RPi.GPIO as GPIO
# creamos una lista con los pines GPIO
pins=[18,23,24]
# creamos una lista con los estados que 
# pueden tener los 3 pines (18,23 i 24)
pin_led_states=[[1,0,-1], # A
                [0,1,-1], # B
                [-1,1,0], # C
                [-1,0,1], # D
                [1,-1,0], # E
                [0,-1,1], # F
                [0,0,0]   # apagar
                ]
# definimos el tipo de identificacion de los puertos GPIO
GPIO.setmode(GPIO.BCM)
# definimos una funcion para cambiar el estado del GPIO
# recibe dos parametros, el pin y el estado
def set_pin(pin_index,pin_state):
    # si el estado es -1, el puerto es de Entrada
    if pin_state==-1:
        GPIO.setup(pins[pin_index],GPIO.IN)
        # si el estado es 0 o 1 el puerto es de salida
    else:
        GPIO.setup(pins[pin_index],GPIO.OUT)
        GPIO.output(pins[pin_index],pin_state)
# definimos una funcion que recibe un parametro 1,2,3,4,5 o 6
def light_led(led_number):
    # bucle que recupera los valores de la lista de pin_led_states
    for pin_index, pin_state in enumerate(pin_led_states[led_number]):
        # llamamos ala funcion que cambia el estado de los pines
        # actvando o desactivando los leds
        set_pin(pin_index,pin_state)
# por defecto ponemos los tres pines a -1
set_pin(0,-1)
set_pin(1,-1)
set_pin(2,-1)
# bucle que se repite indefinidamente
while True:
    # pedimos al usuario que introduzca un valor
    x=int(input("Pin (0 to 6):"))
    # llamamos a la funcion

    light_led(x)