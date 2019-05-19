#1.5 Herencia de clases
# definimos el nombre de la classe
class agendaClientes:
    # linea de documentacion de la clase
    '''Esta clase representa a un objeto de cliente'''
    # metodo constructor de la clase
    def __init__(self,nombre,ape1,ape2,direccion):
        self.nombre=nombre
        self.ape1=ape1
        self.ape2=ape2
        self.direccion=direccion
    # definimos una funcion que devuelve el nombre completo
    def nombre_completo(self):
        return self.nombre + ' ' + self.ape1 + ' ' + self.ape2
    # definimos una funcion que muestra por pantalla el nombre completo
    def imprimir_nombre(self):
        print(self.nombre_completo())

# definimos una subclase heredada de agendaClientesVIP
class agendaClientesVIP (agendaClientes):
    # linea de documentacion de la clase
    ''''Esta es la subclase de clientes VIP'''
    # metodo constructor de la clase agendaClientesVIP
    def __init__(self,nombre,ape1,ape2,direccion,numeroCliente,empresaCliente):
        # metodo constructor de la clase principal agendaClientes
        super().__init__(nombre,ape1,ape2,direccion)
        # definición de las propiedades particulares de la clase agendaClientesVIP
        self.numeroCliente=numeroCliente
        self.empresaCliente=empresaCliente
#
# creamos el objeto clienteVIP de la clase agendaClientesVIP
clienteVIP=agendaClientesVIP('','','','','','')
# añadimos valor a las propiedades de la clase
clienteVIP.nombre='Juan'
clienteVIP.ape1='Soto'
clienteVIP.ape2='Romero'
clienteVIP.direccion='Calle del bosque, 23'
clienteVIP.numeroCliente='00024'
clienteVIP.empresaCliente='Limpiezas SoRo SA'
# llamamos a un método de la clase
clienteVIP.imprimir_nombre()