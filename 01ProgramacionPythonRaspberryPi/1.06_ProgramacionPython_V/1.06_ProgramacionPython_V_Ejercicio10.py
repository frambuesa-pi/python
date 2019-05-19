#1.4.3 Interrumpir bucle For
# Instruccion de bucle que se ejecuta mientras x esté en el rango de 1 a 10
for x in range(1,10):
    # linea para romper el bucle, si se cumple la condición salimos del bucle
    if x==5:
        break
    # linea que muestra por pantalla el valor de x
    print(x)