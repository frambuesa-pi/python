#1.1.2 Determinar la longitud de un numero
# asignamos a una variable un número de punto flotante
numero_pi=3.1416
# asignamos a la variable numero_final un número de punto flotante
# con dos decimales pero indicando que la longitud total debe tener 7 caracteres
numero_final="{:7.2f}".format(numero_pi)
# mostramos por pantalla el número final
print(numero_final)