# importamos el modulo sys
import sys
# creamos bucle para mostrar los argumentos enviados
for (i,value) in enumerate (sys.argv):
    print("arg: %d %s " % (i,value))