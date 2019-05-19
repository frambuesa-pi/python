#1.5 Control de errores con archivos
# iniciamos bloque try con el código a ejecutar
try:
    # abrimos el archivo asignandolo a una variable
    archivo=open('/home/pi/Desktop/fichero_error.txt','r')
    # leemos el contenido del archivo
    contenido=archivo.read()
    # mostramos por pantalla el contenido
    print(contenido)
    # cerramos el archivo
    archivo.close()
# iniciamos bloque except 
except IOError:
    # codigo que se ejecutara si se porduce un error al abrir el archivo
    print('No se puede abrir el archivo')
    