#5. Recorrer diccionarios
# definimos un diccionario
capitales={'España':'Madrid','Francia':'Paris','Alemania':'Berlin'}
# creamos un bucle que muestra las claves del diccionario
for clave in capitales:
    print(clave)

# definimos un diccionario
capitales={'España':'Madrid','Francia':'Paris','Alemania':'Berlin'}
# creamos un bucle que muestra las claves y valores del diccionario
for valor in capitales.items():
    print(valor)

# definimos un diccionario
capitales={'España':'Madrid','Francia':'Paris','Alemania':'Berlin'}
# creamos un bucle que muestra las claves y los valores del diccionario
for clave,valor in capitales.items():
    print(clave + ':' + valor)