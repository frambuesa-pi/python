#11. Recortar una lista
# importamos la libreria copy
import copy #definimos una lista que asignamos a una variable
lista_1=['coche','manzana','zanahoria','rueda','nieve']
# asignamos a una variable nueva la lista truncada
lista_2=lista_1[1:3]
# recorremos la lista truncada y mostramos por pantalla los elementos y la posición
for (i,x) in enumerate(lista_2):
    print(i,x)