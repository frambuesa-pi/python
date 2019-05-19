#1.7 determinar la posicion de una cadena o caracter dentro de una cadena
# Definimos una variable con una cadena
var_Cadena="Esta es una frase corta"
# Asignamos a una variable la longitud total de la variable
var_Longitud=len(var_Cadena)
print(var_Longitud)
# Buscamos la posición inicial de la palabra frase dentro de la cadena
var_Posicion1=var_Cadena.find("frase")
print(var_Posicion1)

# Definimos una variable con una cadena
var_Cadena="Esta es una frase corta"
# Buscamos la posición inicial de la primera letra t dentro de la cadena
var_Posicion2=var_Cadena.find("t")
print(var_Posicion2)