#9. Enumerar los elementos de una lista
# definimos una lista que asignamos a una variable
lista_1=[18,'Alex','2016',True,3.1416]
# recorremos la lista con un bucle for y mostramos por pantalla los elementos y la posición
for (i,x) in enumerate(lista_1):
    print(i,x)