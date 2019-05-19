#1.1.2 Aplicar un formato a la fecha y la hora
# importamos el modulo datetime
import datetime
# guardamos en la variable instante la fecha y hora actual
instante=datetime.datetime.now()
# mostramos la fecha y hora en formato original
print(instante)
# mostramos la fecha y hora con formato dd-mm-aaaa hh:mm:ss
instante_formateado=instante.strftime("%d-%m-%Y %H:%M:%S")
# mostramos por pantalla la fecha y la hora con el nuevo formato
print(instante_formateado)