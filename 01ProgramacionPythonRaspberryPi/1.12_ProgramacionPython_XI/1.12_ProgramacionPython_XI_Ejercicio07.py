#1.1.4 Operaciones con fechas
# importamos el modulo datetime
import datetime
# guardamos una variable con una hora inicial 10:05:00
hora_inicial=datetime.time(10,5,0)
# guardamos una variable con una hora final 23:15:00
hora_final=datetime.time(23,15,0)
if hora_inicial<hora_final:
    print("hora inicial ", hora_inicial, " anterior a hora final ", hora_final)
# guardamos en una varibale la fecha actual
fecha_actual=datetime.datetime.now()
#guaradamos en una variable otra fecha
fecha_anterior=datetime.datetime(1976,8,1,0,0,0)
if fecha_actual>fecha_anterior:
    print("fecha actual ", fecha_actual, " mayor que fecha anterior ", fecha_anterior)