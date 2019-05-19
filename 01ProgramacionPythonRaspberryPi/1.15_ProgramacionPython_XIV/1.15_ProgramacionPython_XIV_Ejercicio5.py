#1.6 Guardar estructuras de datos en un fichero pickle.dump
# importamos el módulo
import pickle
# guardamos en una variable una lista compleja
lista_compleja=['texto',100,200,[10,20,30,False,'Frank']]
# abrimos un archivo para guardar los datos
fichero=open('/home/pi/Desktop/fichero_datos.txt','w+b')
# añadimos los datos al fichero
pickle.dump(lista_compleja,fichero)
# cerramos el fichero
fichero.close()

