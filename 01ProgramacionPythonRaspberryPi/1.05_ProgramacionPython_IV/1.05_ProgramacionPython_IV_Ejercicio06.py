#1.5 convertir cadenas en numeros
# Variable de texto con un número
var_Texto1="1024"
# Variable de texto con un número negativo
var_Texto2="-1024"
# Variable de texto con un número decimal (hay que usar el punto no la coma)
var_Texto3="0.016"
# Transformacion de las cadenas en números
var_Numero1=int(var_Texto1)
var_Numero2=int(var_Texto2)
var_Numero3=float(var_Texto3)
# Sumamos todos los valores
var_Total=var_Numero1 + var_Numero2 + var_Numero3
# Mostramos el valor total (antes lo transformamos en cadena)
print (str(var_Total))