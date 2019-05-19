#1.1 crear un archivo y guardar datos
# abrimos el archivo asignándolo a una variable
archivo=open('/home/pi/Desktop/fichero.txt','w')
# escribimos en el fichero los datos
archivo.write('Primera línea del fichero\n')
archivo.write('Segunda línea del fichero\n')
# cerramos el fichero
archivo.close()
