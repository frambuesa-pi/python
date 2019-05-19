#1.2.3 Cambiar el primer dia de la semana del calendario
# importamos el modulo datetime y calendar
import datetime
import calendar
# obetenemos el año actual
Y=datetime.date.today().year
# guardamos en una variable la matriz del calendario con la configuración
calendario=calendar.TextCalendar(0).formatyear(Y,1,1,1,2)
# mostramos por pantalla el calendario
print(calendario)