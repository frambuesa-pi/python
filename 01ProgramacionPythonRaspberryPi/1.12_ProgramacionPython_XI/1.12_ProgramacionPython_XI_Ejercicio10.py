#1.2.1 Mostrar el calendario del mes actual por pantalla con print()
# importamos el modulo datetime y calendar
import datetime
import calendar
# obetenemos el mes y año actuales
M=datetime.date.today().month
Y=datetime.date.today().year
# guardamos en una variable el calendario del mes
calendario=calendar.month(Y,M)
# mostramos el calendario por pantalla
print(calendario)
