#1.1.1 Obtener la fecha y hora actual
# importamos el modulo datetime
import datetime
# guardamos en la variable instante la fecha y hora actual
instante=datetime.datetime.now()
# mostramos por pantalla la fecha y hora actuales en formato UTC
print("fecha y hora en formato UTC: ",instante.utcnow())
# mostramos solo el año
print("año actual: ",instante.year)
# mostramos solo el mes
print("mes actual: ",instante.month)
# mostramos solo el dia
print("dia actual: ",instante.day)
# mostramos solo la hora
print("hora actual: ",instante.hour)
# mostramos solo los minutos
print("minutos actuales: ",instante.minute)
# mostramos solo los segundos
print("segundos actuales: ",instante.second)
# mostramos solo los milisegundos
print("milisegundos actuales: ",instante.microsecond)