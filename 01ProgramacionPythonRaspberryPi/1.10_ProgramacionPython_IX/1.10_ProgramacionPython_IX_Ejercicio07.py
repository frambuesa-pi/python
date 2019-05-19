#1.1.4 Añadir texto al formateo de un numero
# asignamos a una variable un número de punto flotante
numero_pi=3.1416
# asignamos a la variable numero_final un número de punto flotante
# con dos decimales que formateamos con la 
# instrucción "numero_formateado={:.2f}"
numero_final="numero_formateado={:.2f}".format(numero_pi)
# mostramos por pantalla el número final formateado
print(numero_final)