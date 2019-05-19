#1.1.4 Operaciones con fechas
# importamos el modulo datetime
import datetime
# creamos la variable fecha_actual y guardamos la fecha del sistema
fecha_actual=datetime.datetime.now()
# sumamos a fecha_actual 2 millones de segundos
fecha_actual_mas2mlls=fecha_actual+datetime.timedelta(seconds=2000000)
# sumamos a la fecha acctual 10 horas
fecha_actual_mas10h=fecha_actual+datetime.timedelta(hours=10)
# mostramos los valores por pantalla
print("fecha actual: ",fecha_actual)
print("fecha actual mas 2 millones de segundos: ",fecha_actual_mas2mlls)
print("fecha actual mas 10 horas: ",fecha_actual_mas10h)