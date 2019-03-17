#############################################
#_____https://frambuesa-pi.blogspot.com/____#
#___https://github.com/frambuesa-pi/python__#
#############################################
# importamos libreria GPIO y time
import RPi.GPIO as GPIO
import time
# guardamos en variables los puertos GPIO que usaremos con el Chip
DATASET=17 # Pin para entrada de datos DS
CLOCK=22 # Pin control de lectura de datos SHCP
LATCH=27 # Pin para mostrar datos almacenados STCP
CLEAR=25 # Pin que controla el borrado datos MR
OE=11 # Pin Output enable Pin controla la salida de informacion OE
# guardamos en demora el tiempo de espera
demora=1
# definimos variables que guardan el valor hexadecimal para
# iluminar cada uno de los segmentos, al lado os pongo el
# equivalente en binario para ver la equivalencia, que
# luego guardaremos en cada pin de salida del chip 
# para activar los diferentes segmentos (los 8 valores
# son los que se guardan y activan-desactivan los segmentos)
segmentoA=0x08  #00001000
segmentoB=0x10  #00011000
segmentoC=0x20  #00111000
segmentoD=0x40  #01111000
segmentoE=0x80  #11111000
segmentoF=0x04  #11111100
segmentoG=0x02  #11111110
segmentoDP=0x01 #11111111
# creamos una lista con las variables
ledrange=[segmentoA, segmentoB, segmentoC, segmentoD, segmentoE, segmentoF, segmentoG, segmentoDP]
# funcion para inicializar los GPIO
def setup():
    # desactivamos mensajes error GPIO
    GPIO.setwarnings(False)
    # indicamos el uso de  la identificacion BCM para los GPIO
    GPIO.setmode(GPIO.BCM)
    # inicializamos GPIO
    GPIO.cleanup()
    # indicamos los GPIO que usaremos como salida
    GPIO.setup(DATASET,GPIO.OUT)
    GPIO.setup(CLOCK,GPIO.OUT)
    GPIO.setup(LATCH,GPIO.OUT)
    GPIO.setup(CLEAR,GPIO.OUT)
    GPIO.setup(OE,GPIO.OUT)
    # indicamos a cada GPIO el estado inicial
    GPIO.output(DATASET,False) # Se usa para introducir los datos
    GPIO.output(CLOCK,False)  # controla la entrada de datos
    GPIO.output(LATCH,False)  # Muestra los datos almacenados
    GPIO.output(CLEAR,True)   # El valor False borra todos los datos
    GPIO.output(OE,False)     # Output Enable, para salida de datos
    
# definimos una funcion que apaga el display
def cleanup():
    #
    writenumber(0)
    #
    writeout()
    #
    writeout()
    time.sleep(0.7)
    GPIO.cleanup()

# Funciones para activar segmentos del display

# Envia por el GPIO si el valor input es = 1 o <> 1
# al chip para guardarlo en memoria del chip
def shift(input):
    if input == 1:
        input=True
    else:
        input=False
    # enviamos un valor al pin de datos DATASET
    GPIO.output(DATASET,input)
    # activo el pin de lectura para leer el valor CLOCK
    GPIO.output(CLOCK,GPIO.HIGH)
    # desactivo el pin e lectura
    GPIO.output(CLOCK,GPIO.LOW)
    # finalizo en envio del dato al pin DATASET
    GPIO.output(DATASET,GPIO.LOW)

# writenumber recoge el valor del segmento que
# queremos activar o desactivar, y ejecuta 8
# veces (para cada valor de almacenamiento del chip)
# la orden shift para enviar el valores a guardar
def writenumber(number):
    for x in range(0,8):
        # ejecuto la orden shift pasando a binario
        # el valor del segmento
        shift((number>>x)%2)

# Envia a los GPIO la orden para mostrar los datos
# guardados en el chip
# y que se refleje en el display
def writeout():
   # Activamos salida de datos guardados con LATCH
   GPIO.output(LATCH,GPIO.HIGH)
   #
   time.sleep(demora)
   # Finalizo la salida de datos guardados de LATCH
   GPIO.output(LATCH,GPIO.LOW)

# funcion que recibe la lista de segmentos para recorrerlos
def writexorrange(range):
    # con esta orden evitamos que 'character' provoque un error
    character=range[0]&range[-1]
    # recorremos las 8 variables para activar los segmentos
    for x in range:
        character^=x
        writenumber(character)
        writeout()
    # recorremos las 8 variables para apagar los segmentos
    for x in range:
        character^=x
        writenumber(character)
        writeout()
    # recorremos las 8 variables a la inversa para activar los segmentos
    for x in reversed(range):
        character^=x
        writenumber(character)
        writeout()
    # recorremos las 8 variables a la inversa para apagar los segmentos
    for x in reversed(range):
        character^=x
        writenumber(character)
        writeout()

# llamamos a la funcion que inicializa los GPIO
print("-->Inicializamos GPIO")
setup()

# usamos estructura de control de errores si presionamos CTRL+C
# se interrumpira la ejecuciÃ³n
try:
    print("-->Encendemos el display")
    # bucle infinito que llama a la funcion que enciende los segmentos
    while True:
        # llamamos a la funciÃ³n que activa el display
        writexorrange(ledrange)

# esto se ejecuta al presionar CTRL+C
except (KeyboardInterrupt, SystemExit):
    print("Exit...")
# si interrumpimos el codigo ejecutamos cleanup()
finally:
    # apagamos el display
    cleanup()