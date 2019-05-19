#1.5 Mas informacion sobre los errores
# guardamos en una variable una lista de elementos
lista_numeros=[0,1,2,3,4,5,6,7,8]
# iniciamos el código con control de errores con try
try:
    # mostramos por pantalla el elemento 2 de la lista
    print(lista_numeros[2])
    # mostramos por pantalla el elemento 10 de la lista que no existe
    print(lista_numeros[10])
    # mostramos por pantalla el elemento 6 de la lista
    print(lista_numeros[6])
# iniciamos bloque except
except Exception as e:
    # codigo que se ejecutara si se produce una excepcion
    print("Se ha producido un error")
    # codigo que muestra la descripcion del error
    print(e)
    