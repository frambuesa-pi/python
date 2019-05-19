#1.6 Generar un orden aleatorio para una lista de valores shuffle
# importamos el modulo random
import random
# guardamos en una variable una lista de elementos
lista=[1,2,3,4,5,6,7,8,9,0]
# modificamos el orden de los elementos
random.shuffle(lista)
# mostramos por pantalla el nuevo orden de los elementos
print(lista)