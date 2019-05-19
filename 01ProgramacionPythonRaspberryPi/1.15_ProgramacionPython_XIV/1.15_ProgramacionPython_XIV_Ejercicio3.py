#1.3 Leer un archivo linea a linea
# abrimos el archivo asignandolo a una variable
archivo=open('/home/pi/Desktop/fichero.txt','r')
# leemos el contenido del archivo
contenido1=archivo.readline()
contenido2=archivo.readline()
# mostramos por pantalla el contenido
print(contenido1)
print(contenido2)
# cerramos el archivo
archivo.close()
