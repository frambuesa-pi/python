#1.1.5 Obtener el dia de la semana de una fecha
# importamos modulo datetime
import datetime
# guardamos en una variable la fecha de vuestro nacimiento
fecha_nacimiento=datetime.datetime(1976, 8, 1, 0, 0, 0)
# guardamos en una variable el día de la semana de la fecha
dia_semana=datetime.datetime.weekday(fecha_nacimiento)
# mostramos por pantalla el resultado
print("fecha nacimiento: ", fecha_nacimiento, "- día de la semana: ", dia_semana)
