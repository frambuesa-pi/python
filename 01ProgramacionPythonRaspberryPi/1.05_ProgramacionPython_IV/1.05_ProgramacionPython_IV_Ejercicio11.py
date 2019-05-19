#1.8 Extraer caracteres de una cadena
# Definimos una variable con una cadena
var_Cadena="zyxwvutsrqpo"
# Guardamos en una segunda variable la extracción omitiendo la primera variable
var_CadenaExtraida1=var_Cadena[:5]
# Mostramos por pantalla la cadena extraída
print(var_CadenaExtraida1)
# Guardamos en una tercera variable la extracción omitiendo la segunda variable
var_CadenaExtraida2=var_Cadena[1:]
# Mostramos por pantalla la cadena extraída
print(var_CadenaExtraida2)
# Guardamos en una cuarta variable la extracción omitiendo las dos variables
var_CadenaExtraida3=var_Cadena[:]
# Mostramos por pantalla la cadena extraída
print(var_CadenaExtraida3)