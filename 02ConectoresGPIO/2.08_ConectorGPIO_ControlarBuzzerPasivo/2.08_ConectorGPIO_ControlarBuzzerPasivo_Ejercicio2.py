#############################################
#_____https://frambuesa-pi.blogspot.com/____#
#___https://github.com/frambuesa-pi/python__#
#############################################
# importamos librerias necesarias
import RPi.GPIO as GPIO
import time
# definimos variable con el identificador del pin GPIO
Buzzer = 18
# Creamos listas para guardar las notas
# Lista con frecuencia en Hz de las notas bajas 
CL = [0, 131, 147, 165, 175, 196, 211, 248]
# Lista con frecuencia en Hz de las notas medias
CM = [0, 262, 294, 330, 350, 393, 441, 495]
# Lista con frecuencia en Hz de las notas altas
CH = [0, 525, 589, 661, 700, 786, 882, 990]
# Notas cancion 1
song_1 = [CM[3], CM[5], CM[6], CM[3], CM[2], CM[3], CM[5], CM[6],
          CH[1], CM[6], CM[5], CM[1], CM[3], CM[2], CM[2], CM[3],
          CM[5], CM[2], CM[3], CM[3], CL[6], CL[6], CL[6], CM[1],
          CM[2], CM[3], CM[2], CL[7], CL[6], CM[1], CL[5]]
# duracion de las notas cancion 1
beat_1 = [1, 1, 3, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 3, 1,
          1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 3]
# Notas cancion 2
song_2 = [CM[1], CM[1], CM[1], CL[5], CM[3], CM[3], CM[3], CM[1],
          CM[1], CM[3], CM[5], CM[5], CM[4], CM[3], CM[2], CM[2],
          CM[3], CM[4], CM[4], CM[3], CM[2], CM[3], CM[1], CM[1],
          CM[3], CM[2], CL[5], CL[7], CM[2], CM[1]]
# Duracion de las notas cancion 2
beat_2 = [1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 3, 1, 1, 2,
          2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 3]
#
# definimos funcion que inicializa el puerto GPIO18
def setup():
    # desactivamos mensajes de error
    GPIO.setwarnings(False)
    # indicamos el uso de  la identificacion BCM para los GPIO
    GPIO.setmode(GPIO.BCM)
    # indicamos que el GPIO18 es de salida de corriente
    GPIO.setup(Buzzer, GPIO.OUT)
    # definimos variable global para guardar el PWM del GPIO
    global Buzz # Assign a global variable to replace GPIO.PWM
    # asignamos a la variable la frecuencia inicial de salida (440)
    Buzz = GPIO.PWM(Buzzer, 440)
    # iniciamos la salida al 50%
    Buzz.start(50)
#
# definimos bucle que hace sonar las canciones
def loop():
    while True:
        print ('\n    Cancion 1...')
        # for que recorre las notas de la cancion 1
        for i in range(1, len(song_1)):
            # cambiamos la frecuencia con las notas de la cancion
            Buzz.ChangeFrequency(song_1[i])
            # tiempo de espera para la siguiente nota
            time.sleep(beat_1[i] * 0.5)
            #
            time.sleep(5) # esperamos 5 segundos para la cancion 2
        print ('\n\n    Cancion 2...')
        # for que recorre las notas de la cancion 2
        for i in range(1, len(song_2)):
            # cambiamos la frecuencia con las notas de la cancion
            Buzz.ChangeFrequency(song_2[i])
            # tiempo de espera para la siguiente nota
            time.sleep(beat_2[i] * 0.5)
#
# funcion que para la ejecucion del programa
def destory():
    # paramos el buzzer
    Buzz.stop()
    GPIO.output(Buzzer, 1)
    GPIO.cleanup()
# inicio del programa
if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt: # Presionar CTRL+C para finalizar programa.
        destory()