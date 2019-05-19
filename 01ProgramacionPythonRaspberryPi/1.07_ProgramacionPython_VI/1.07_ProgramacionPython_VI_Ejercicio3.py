#2.1 Enviar a una funcion multiples parametros
# definimos una función que calcula el importe con el iva, 
# ambos valores los pasamos por parametro
def calcular_importe_iva(importe,iva):
    importe=(importe)+((importe*iva)/100)
    print(importe)

# llamamos a la funnción pasando importe 100 y iva 4
calcular_importe_iva(100,4)
# llamamos a la funnción pasando importe 200 y iva 12
calcular_importe_iva(200,12)
# llamamos a la funnción pasando importe 300 y iva 21
calcular_importe_iva(300,21)