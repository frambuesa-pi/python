#############################################
#_____https://frambuesa-pi.blogspot.com/____#
#___https://github.com/frambuesa-pi/python__#
#############################################
# importamos libreria time
import time
# importamos libreria GPIO
import RPi.GPIO as GPIO
#
# configuracion para los GPIO
# usaremos la identificacion BCM para los GPIO
GPIO.setmode(GPIO.BCM)
# desactivamos mensajes de error
GPIO.setwarnings(False)
# indicamos los puertos de salida GPIO
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
#
# definimos funcion que apaga o enciende todos los
# segmentos del display según el parametro
# que enviamos 0=apagar 1=encender
def INICIALIZAR_DISPLAY(estado):
    # si enviamos 0 apagamos los segmentos
    if estado == 0:
        GPIO.output(14, False)
        GPIO.output(15, False)
        GPIO.output(18, False)
        GPIO.output(23, False)
        GPIO.output(24, False)
        GPIO.output(25, False)
        GPIO.output(8, False)
        GPIO.output(7, False)
    else: # si enviamos 1 encendemos los segmentos
        GPIO.output(14, True)
        GPIO.output(15, True)
        GPIO.output(18, True)
        GPIO.output(23, True)
        GPIO.output(24, True)
        GPIO.output(25, True)
        GPIO.output(8, True)
        GPIO.output(7, True)
#
# definimos funcion para hacer un test del display
# enciende uno a uno los segmentos con un
# retraso indicado por el parametro demora
def TEST_DISPLAY(demora):
    # aparagamos todos los segmentos
    INICIALIZAR_DISPLAY(0)
    # los encendemos uno a uno
    GPIO.output(14, True)
    time.sleep(demora)
    GPIO.output(15, True)
    time.sleep(demora)
    GPIO.output(18, True)
    time.sleep(demora)
    GPIO.output(23, True)
    time.sleep(demora)
    GPIO.output(24, True)
    time.sleep(demora)
    GPIO.output(25, True)
    time.sleep(demora)
    GPIO.output(8, True)
    time.sleep(demora)
    GPIO.output(7, True)
#
# definimos funcion que recibe un parametro que debe ser
# un número o un punto y enciende los segmentos
# correspondientes del display
def PRINT_DISPLAY(digito):
    INICIALIZAR_DISPLAY(0) # apagamos todos los segmentos
    # activamos los segmentos para cada número
    if digito== "0": # numero 0
        GPIO.output(14, True) # segmento a
        GPIO.output(15, True) # segmento b
        GPIO.output(18, True) # segmento c
        GPIO.output(23, True) # segmento d
        GPIO.output(24, True) # segmento e
        GPIO.output(25, True) # segmento f
    elif digito== "1": # numero 1
        GPIO.output(15, True) # segmento b
        GPIO.output(18, True) # segmento c
    elif digito== "2": # numero 2
        GPIO.output(14, True) # segmento a
        GPIO.output(15, True) # segmento b
        GPIO.output(23, True) # segmento d
        GPIO.output(24, True) # segmento e
        GPIO.output(8, True) # segmento g
    elif digito== "3": # numero 3
        GPIO.output(14, True) # segmento a
        GPIO.output(15, True) # segmento b
        GPIO.output(18, True) # segmento c
        GPIO.output(23, True) # segmento d
        GPIO.output(8, True) # segmento g
    elif digito== "4": # numero 4
        GPIO.output(15, True) # segmento b
        GPIO.output(18, True) # segmento c
        GPIO.output(25, True) # segmento f
        GPIO.output(8, True) # segmento g
    elif digito== "5": # numero 5
        GPIO.output(14, True) # segmento a
        GPIO.output(18, True) # segmento c
        GPIO.output(23, True) # segmento d
        GPIO.output(25, True) # segmento f
        GPIO.output(8, True) # segmento g
    elif digito== "6": # numero 6
        GPIO.output(14, True) # segmento a
        GPIO.output(18, True) # segmento c
        GPIO.output(23, True) # segmento d
        GPIO.output(24, True) # segmento e
        GPIO.output(25, True) # segmento f
        GPIO.output(8, True) # segmento g
    elif digito== "7": # numero 7
        GPIO.output(14, True) # segmento a
        GPIO.output(15, True) # segmento b
        GPIO.output(18, True) # segmento c
    elif digito== "8": # numero 8
        GPIO.output(14, True) # segmento a
        GPIO.output(15, True) # segmento b
        GPIO.output(18, True) # segmento c
        GPIO.output(23, True) # segmento d
        GPIO.output(24, True) # segmento e
        GPIO.output(25, True) # segmento f
        GPIO.output(8, True) # segmento g
    elif digito== "9": # numero 9
        GPIO.output(14, True) # segmento a
        GPIO.output(15, True) # segmento b
        GPIO.output(18, True) # segmento c
        GPIO.output(23, True) # segmento d
        GPIO.output(25, True) # segmento f
        GPIO.output(8, True) # segmento g
    elif digito== ".": # DP (punto decimal)
        GPIO.output(7, True) # segmento DP
#
# Codigo para ejecutar las funciones
# con la siguiente funcion encendemos todos segmentos
INICIALIZAR_DISPLAY(1)
# damos un tiempo de espera
time.sleep(0.5)
# con la siguiente funcion apagamos todos los segmentos
INICIALIZAR_DISPLAY(0)
#damos un tiempo de espera
time.sleep(0.5)
# llamamos a la funcion que enciende los segmentos
# uno a uno con un tiempo de espera
TEST_DISPLAY(0.2)
#damos un tiempo de espera de un segundo
time.sleep(1)
# con la siguiente funcion apagamos todos los segmentos
INICIALIZAR_DISPLAY(0)
# con el siguente bucle infinito podemos introducir un
# numero o un punto y al hacer intro aparecera en el
# display
while (True):
    # mensaje para el usuario
    tecla=input("introduzca un número o punto y presione Intro en el teclado: ")
    # llamamos a la funcion que ilumina los segmentos
    PRINT_DISPLAY(tecla)