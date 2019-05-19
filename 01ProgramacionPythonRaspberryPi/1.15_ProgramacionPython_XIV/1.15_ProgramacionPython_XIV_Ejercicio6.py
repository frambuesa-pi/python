#1.7 Recuperar estructuras de datos de un fichero pickle.load
# importamos el módulo
import pickle
# abrimos un archivo para guardar los datos
fichero=open('/home/pi/Desktop/fichero_datos.txt','r+b')
# recuperamos los datos al fichero
nueva_lista=pickle.load(fichero)
# cerramos el fichero
fichero.close()
# mostramos el contenido recuperado
print(nueva_lista)
