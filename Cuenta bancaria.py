from os import system

class Persona:
    def __init__(self,nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

class Cliente(Persona):
    def __int__(self, nombre, apellidos, cuenta, balance=0):
      super().__init__(nombre, apellidos)
      self.cuenta = cuenta
      self.balance = balance

    def __str__(self):
        return f'Cliente: {self.nombre} {self.apellidos}\n Cuenta:{self.cuenta} ${self.balance}'

    def depositar (self,monto_ingresar):
        self.balance+=monto_ingresar
        print(f'Balance actual: {self.balance}')

    def retirar (self,monto_retirar):
        if self.balance >= monto_retirar:
            self.balance-=monto_retirar
            print(f'Retiro correcto, balance actual: {self.balance} ')
        else:
            print('No hay fondos sufiecientes')

def crear_cliente():
    nombre_cliente = input ('Ingrese nombre: ')
    apellidos_cliente = input ('Ingrese apellidos: : ')
    numero_cuenta = input ('Ingrese su numero de cuenta: ')
    cliente = Cliente(nombre_cliente, apellidos_cliente, numero_cuenta)
    return cliente

def inicio():
    mi_cliente=crear_cliente()
    print(mi_cliente)


    while opcion!=0:
        print('Menu:\n 1 para ingresar dinero\n 2 para retirar\n 0 para salir de la operacion')
        opcion = int(input('Elija una opcion: '))

        match opcion:
            case 1:
                monto_dep = float(input('Monto a depositar'))
                mi_cliente.depositar(monto_dep)
            case 2:
                monto_ret = float(input('Monto a depositar'))
                mi_cliente.retirar(monto_ret)

            case 0:
                system('cls')


        print(mi_cliente)


    print('Gracias por operar en banco Python')

inicio()



