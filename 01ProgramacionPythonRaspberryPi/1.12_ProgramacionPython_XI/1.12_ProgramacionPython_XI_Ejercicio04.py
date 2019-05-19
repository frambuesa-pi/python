#1.1.3 Generar una fecha concreta
# importamos el modulo datetime
import datetime
# guardamos en una variable la fecha actual
fecha_actual=datetime.datetime.now()
# guardamos en una variable la fecha de vuestro nacimiento
fecha_nacimiento=datetime.datetime(1976, 8, 5, 0 , 0, 0)
# restamos las dos fechas y guardamos el valor en una variable
diferencia_fechas=fecha_actual-fecha_nacimiento
# mostramos por pantalla la fecha inicial y la de nacimiento
print("fecha actual: ",fecha_actual)
print("fecha_nacimiento: ",fecha_nacimiento)
# mostramos por pantalla la diferencia entre las dos fechas
print("diferencia_fechas: ",diferencia_fechas)
# diferencia en días
print("diferencia en días: ",diferencia_fechas.days)
# diferencia en segundos
print("diferencia en segundos: ",diferencia_fechas.seconds)