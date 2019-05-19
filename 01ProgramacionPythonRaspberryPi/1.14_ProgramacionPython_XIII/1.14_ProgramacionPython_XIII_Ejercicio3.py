#1.2 Estructura para controlar un error determinado
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
except IndexError:
    # codigo que se ejecuta si se produce un error IndexError
    print("Se ha producido un error, IndexError")
except IOError:
    # codigo que se ejecuta si se produce un error IOErrors
    print("Se ha producido un error, IOError")
except:
   # codigo que se ejecuta si se produce un error distinto de IndexError o IOError
    print("Se ha producido un error")
    
