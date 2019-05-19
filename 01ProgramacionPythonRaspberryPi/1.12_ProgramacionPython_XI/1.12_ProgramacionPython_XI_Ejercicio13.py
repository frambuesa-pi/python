#1.2.3 Cambiar el primer dia de la semana del calendario
# importamos el modulo datetime y calendar
import datetime
import calendar
# obetenemos el mes y año actuales
M=datetime.date.today().month
Y=datetime.date.today().year
# guardamos en una variable la matriz del calendario
calendario=calendar.TextCalendar(0)
calendario.pryear(Y)
