#5.3 añadir los elementos de una lista a otra lista
# definimos una lista de valores y los asignamos a la variable lista_1
lista_1=[18,'Alex']
# definimos otra lista de valores y los asignamos a la variable lista_2
lista_2=[True,3.1416]
# al final de la lista_1 le añadimos los valores de la lista_2
lista_1.extend(lista_2)
# accedemos al los diferentes valores de lista_1 y los mostramos por pantalla
print(lista_1[0])
print(lista_1[1])
print(lista_1[2])
print(lista_1[3])