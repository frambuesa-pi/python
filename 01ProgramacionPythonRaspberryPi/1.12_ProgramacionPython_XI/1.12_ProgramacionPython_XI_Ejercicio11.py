#1.2.2 Mostrar el calendario del mes actual por pantalla con prmonth
# importamos el modulo datetime y calendar
import datetime
import calendar
# obetenemos el mes y año actuales
M=datetime.date.today().month
Y=datetime.date.today().year
# mostramos por pantalla el calendario del mes con prmonth()
calendar.prmonth(Y,M)
