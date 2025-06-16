
class Cuenta:
    contador_cuentas = 100001

    def __init__(self, dni='', saldo=0.0, interes_anual=0.0):
        self.numero_cuenta = Cuenta.contador_cuentas
        Cuenta.contador_cuentas += 1
        self.dni = dni
        self.saldo = saldo
        self.interes_anual = interes_anual

    def actualizar_saldo(self):
        interes_diario = self.interes_anual / 365
        self.saldo += self.saldo * (interes_diario / 100)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad

    def mostrar_datos(self):
        return f"Número de cuenta: {self.numero_cuenta}\nDNI: {self.dni}\nSaldo actual: {self.saldo:.2f}\nInterés anual: {self.interes_anual}%"
