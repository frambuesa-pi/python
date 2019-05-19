#3.1 Devolver multiples valores con una funcion
# definimos una función que recibe el importe y el iva y devuelve el importe+iva, 
# y el importe del iva por separado
def calcular_importe_iva(importe,iva):
    importe_total=(importe)+((importe*iva)/100)
    importe_iva=((importe*iva)/100)
    return(importe_total,importe_iva)

# llamamos a la funnción pasando importe 100 y iva 4 y asignamos los valores devueltos
precio_total,precio_iva=calcular_importe_iva(100,4)
print(precio_total)
print(precio_iva)