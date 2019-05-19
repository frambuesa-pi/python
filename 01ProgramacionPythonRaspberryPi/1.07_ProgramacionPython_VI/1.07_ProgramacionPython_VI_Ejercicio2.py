#2. Enviar parametros a una funcion
# definimos una función que aplica un descuento a un importe que se pasa por parámetro
def aplicar_descuento_10 (importe):
    importe=(importe)-((importe*10)/100)
    print(importe)

# llamamos a la función pasando el importe de 100
aplicar_descuento_10(100)
# llamamos a la función pasando el importe de 150
aplicar_descuento_10(150)
# llamamos a la función pasando el importe de 200
aplicar_descuento_10(200)