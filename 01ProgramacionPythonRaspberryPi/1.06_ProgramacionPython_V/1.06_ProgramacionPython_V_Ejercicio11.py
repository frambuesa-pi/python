#1.4.3 Interrumpir bucle While
# Definimos la variable x igual a 0
x=1
# Instrucción while, indica la repetición de instrucciones mientras x sea menor que 10
while x<10:
    # linea que muestra por pantalla el valor de x
    print(x)
    # linea que aumenta en una unidad el valor de x
    x=x+1
     # linea para romper el bucle, si se cumple la condición salimos del bucle
    if x==5:
        break