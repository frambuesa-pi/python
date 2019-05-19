#10. Ordenar una lista
# definimos una lista que asignamos a una variable
lista_1=['coche','manzana','zanahoria','rueda','nieve']
# ordenamos la lista
lista_1.sort()
# recorremos la lista y mostramos los elementos ordenados y la posición
for (i,x) in enumerate(lista_1):
    print(i,x)