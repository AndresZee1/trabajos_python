
from cuenta import Cuenta

def ejecutar_cuentas():
    cuentas = []
    while True:
        dni = input("DNI del cliente: ")
        saldo = float(input("Saldo inicial: "))
        interes = float(input("Interés anual (%): "))
        cuenta = Cuenta(dni, saldo, interes)
        cuentas.append(cuenta)

        cuenta.actualizar_saldo()
        cuenta.ingresar(100)
        cuenta.retirar(50)
        print(cuenta.mostrar_datos())

        cont = input("¿Desea ingresar otra cuenta? (s/n): ").lower()
        if cont != 's':
            break

ejecutar_cuentas()
