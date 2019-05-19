#1.2 Definir una clase
# definimos el nombre de la classe
class agendaClientes:
    # linea de documentacion de la clase
    '''Esta clase representa a un objeto de cliente'''
    # metodo constructor de la clase
    def __init__(self,nombre,apellido1,apellido2,direccion):
        self.nombre=nombre
        self.apellido1=apellido1
        self.apellido2=apellido2
        self.direccion=direccion
#1.3 Llamar a una clase
print(agendaClientes.__doc__)
#
# creamos un objeto de la clase agendaClientes y asignamos valores
objetoAgenda=agendaClientes('Juan','Sanchez','Ortega','Avda. Los Pajaritos, 6')
# mostramos por pantalla el valor de las propiedddes del objeto
print(objetoAgenda.nombre)
print(objetoAgenda.apellido1)
print(objetoAgenda.apellido2)
print(objetoAgenda.direccion)
#
# creamos un objeto de la clase agendaClientes
objetoAgenda2=agendaClientes('','','','')
# asignamos valor a las propiedades  del objeto
objetoAgenda2.nombre='Maria'
objetoAgenda2.apellido1='Garcia'
objetoAgenda2.apellido2='Requena'
objetoAgenda2.direccion='Calle del sol, 201'
# mostramos por pantalla el valor de las propiedades del objeto
print(objetoAgenda2.nombre)
print(objetoAgenda2.apellido1)
print(objetoAgenda2.apellido2)
print(objetoAgenda2.direccion)