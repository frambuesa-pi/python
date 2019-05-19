#1.2.3 Cambiar el primer dia de la semana del calendario
# importamos el modulo datetime y calendar
import datetime
import calendar
# obetenemos el mes y año actuales
M=datetime.date.today().month
Y=datetime.date.today().year
# cambiamos el primer dia de la semana a martes asignándolo a una variable
calendario=calendar.TextCalendar(1)
# mostramos por pantalla el calendario del mes con prmonth()
calendario.prmonth(Y,M)
