#1.2.4 Obtener la matriz del calendario
# importamos el modulo datetime y calendar
import datetime
import calendar
# obetenemos el mes y año actuales
M=datetime.date.today().month
Y=datetime.date.today().year
# guardamos en una variable la matriz del calendario
calendario=calendar.Calendar()
# mostramos por pantalla los elementos de la matriz con un bucle
for elemento in calendario.monthdayscalendar(Y,M):
    print(elemento)
    