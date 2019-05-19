#1.1 Condiciones
#Definimos la variable Edad con valor 5
Edad = 5
#Creamos una condición
if Edad > 65:
    #Linea que se ejecutará si se cumple la condición (con tabulación delante)
    print("Tercera edad")
elif Edad>20:
    #Linea que se ejecutará si se cumple Edad<15
    print("Adulto")
elif Edad>12:
    #Linea que se ejecutará si se cumple Edad<15
    print("Adolescente")
else:
    #Linea que se ejecutará si no se cumplen las dos condiciones anteriores
    print("Niño")