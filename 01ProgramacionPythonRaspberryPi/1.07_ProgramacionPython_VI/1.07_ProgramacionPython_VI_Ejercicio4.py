#3. Devolver valores con una funcion
# definimos una función que calcula y devuelve el importe con el iva, 
# ambos valores los pasamos por parametro
def calcular_importe_iva(importe,iva):
    importe=(importe)+((importe*iva)/100)
    return(importe)

# llamamos a la funnción pasando importe 100 y iva 4 y lo asigamos a una variable
importe_total=calcular_importe_iva(100,4)
# mostramos el valor de la variable por pantalla
print(importe_total)