#1.3 Excepciones con bloque else
# guardamos en una variable una lista de elementos
lista_numeros=[0,1,2,3,4,5,6,7,8]
# iniciamos el código con control de errores con try
try:
    # mostramos por pantalla el elemento 2 de la lista
    print(lista_numeros[2])
    # mostramos por pantalla el elemento 6 de la lista
    print(lista_numeros[6])
# iniciamos bloque except
except IndexError:
    # codigo que se ejecuta si se produce un error IndexError
    print("Se ha producido un error, IndexError")
# iniciamos bloque else
else:
    # codigo que se ejecuta si no se produce un error
    print("Índice correcto")
    