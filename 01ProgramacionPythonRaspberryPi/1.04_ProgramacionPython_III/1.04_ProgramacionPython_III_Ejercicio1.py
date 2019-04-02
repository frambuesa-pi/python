# Guardamos en una variable la temperatura que introduce el usuario
var_Centigrados=input("Introduzca la temperatura en grados centígrados: ")
# Calculamos y guardamos en una variable la temperatura en grados Kelvin
var_Kelvin=(int(var_Centigrados))+273.15
# Mostramos por pantalla los grados Kelvin (antes pasamos a cadena la variable)
print("grados Kelvin: " + str(var_Kelvin))
# Calculamos y guardamos en una variable la temperatura en grados Farenheit
var_Farenheit=(int(var_Centigrados)*9)/5+32
# Mostramos por pantalla los grados Farenheit (antes pasamos a cadena la variable)
print("grados Farenheit: " + str(var_Farenheit))