#1.4 Definir un metodo en una clase
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
    # definimos una funcion que devuelve el nombre completo
    def nombre_completo(self):
        return self.nombre + ' ' + self.apellido1 + ' ' + self.apellido2
    # definimos una funcion que muestra por pantalla el nombre completo
    def imprimir_nombre(self):
        print(self.nombre_completo())
    #
    # creamos un objeto de la clase agendaClientes y asignamos valores
objetoAgenda=agendaClientes('Juan','Sanchez','Ortega','Avda. Los Pajaritos, 6')
# llamamos a la funcion imprimir_nombre
objetoAgenda.imprimir_nombre()
