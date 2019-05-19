#1.1.2 Aplicar un formato largo a la fecha y la hora 
# importamos el modulo datetime
import datetime
# guardamos en una variable la fecha y hora actual
fecha_actual=datetime.datetime.now()
# guardamos en una variable la fecha con formato largo
fecha_actual_formateada=datetime.datetime.ctime(fecha_actual)
# mostramos por pantalla la fecha en formato largo
print("fecha actual formateada: ",fecha_actual_formateada)