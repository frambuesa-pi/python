#1.2 Leer un archivo read
# abrimos el archivo asignandolo a una variable
archivo=open('/home/pi/Desktop/fichero.txt','r')
# leemos el contenido del archivo
contenido=archivo.read()
# mostramos por pantalla el contenido
print(contenido)
# cerramos el archivo
archivo.close()
