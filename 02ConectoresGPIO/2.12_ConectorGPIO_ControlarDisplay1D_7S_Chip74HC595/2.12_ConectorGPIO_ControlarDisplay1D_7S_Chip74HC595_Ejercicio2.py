#############################################
#_____https://frambuesa-pi.blogspot.com/____#
#___https://github.com/frambuesa-pi/python__#
#############################################
# importamos libreria GPIO y time
import RPi.GPIO as GPIO
import time
# guardamos en variables los puertos GPIO que usaremos
DATASET=17 # Pin para entrada de datos
CLOCK=22 # Pin control de lectura de datos
LATCH=27 # Pin para mostrar datos almacenados
CLEAR=25 # Pin que controla el borrado datos
OE=11 # Pin Output enable Pin controla la salida de informacion
# guardamos en demora el tiempo de espera
demora=1
# definimos variables que guardan el valor hexadecimal para
# mostrar los números en el display.
cero=0xFC
uno=0x30
dos=0xDA
tres=0x7A
cuatro=0x36
cinco=0x6E
seis=0xEE
siete=0x38
ocho=0xFE
nueve=0x3E
#creamos una lista con las variables
letterrange=[cero,uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve]
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
    GPIO.output(OE,False)     # Output Enable para salida de datos

# definimos una funcion que apaga todos los segmentos
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
# encendido al chip para guardarlo en memoria
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
# veces (para cada pin de almacenamiento del chip)
# la orden shift para enviar el valor a
# guardar em cada pin
def writenumber(number):
    for x in range(0,8):
        # ejecuto la orden shift pasando a binario
        # el valor del segmento
        shift((number>>x)%2)

# Envia a los GPIO la orden para leer los datos
# guardados en el chip
# y que se refleje en el display
def writeout():
   # Activamos salida de datos guardados con LATCH
   GPIO.output(LATCH,GPIO.HIGH)
   #
   time.sleep(demora)
   # Finalizo la salida de datos guardados de LATCH
   GPIO.output(LATCH,GPIO.LOW)

# funcion que recibe la lista de numeros para recorrerlos       
def writerange(range):
    for x in range:
        writenumber(x)
        writeout()
    
# llamamos a la funcion que inicializa los GPIO
print("-->Inicializamos GPIO")
setup()

# usamos estructura de control de errores si presionamos CTRL+C
# se interrumpira la ejecución
try:
    print("-->Encendemos el display")
    # bucle infinito que llama a la funcion que enciende los segmentos
    while True:
        # llamamos a la funcion que activa el display
        writerange(letterrange)
        
# esto se ejecuta al presionar CTRL+C
except (KeyboardInterrupt, SystemExit):
    print("Exit...")
# una vez interumpido o finalizado el codigo ejecutamos cleanup()
finally:
    cleanup()