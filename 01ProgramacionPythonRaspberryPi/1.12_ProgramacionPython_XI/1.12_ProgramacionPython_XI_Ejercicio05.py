#1.1.4 Operaciones con fechas
# importamos el modulo datetime
import datetime
# creamos la variable fecha_actual y guardamos la fecha del sistema
fecha_actual=datetime.datetime.now()
fecha_ayer=fecha_actual-datetime.timedelta(days=1)
fecha_manana=fecha_actual+datetime.timedelta(days=1)
# mostramos por pantalla las tres fechas
print("print fecha actual: ", fecha_actual)
print("print fecha ayer: ", fecha_ayer)
print("print fecha mañana: ", fecha_manana)