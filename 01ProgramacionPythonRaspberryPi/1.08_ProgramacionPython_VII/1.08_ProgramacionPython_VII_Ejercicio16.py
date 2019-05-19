#10. Ordenar una lista
# importamos la libreria copy para poder usar el comando
import copy
# definimos una lista que asignamos a una variable
lista_1=['coche','manzana','zanahoria','rueda','nieve']
# copiamos la lista
lista_2=copy.copy(lista_1)
# ordenamos la nueva lista creada
lista_2.sort()
# recorremos la lista ordenada y mostramos por pantalla los elementos y la posición
print('Lista ordenada:')
for (i,x) in enumerate(lista_2):
    print(i,x)
# recorremos la lista original y mostramos por pantalla los elementos y la posición
print('Lista original:')
for (i,x) in enumerate(lista_1):
    print(i,x)