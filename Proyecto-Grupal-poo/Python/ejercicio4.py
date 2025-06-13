class Cuenta:
    def __init__(self, numero_cuenta, saldo):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def mostrar_info(self):
        return f"Cuenta: {self.numero_cuenta}\nSaldo: {self.saldo}"

class CuentaAhorro(Cuenta):
    def __init__(self, numero_cuenta, saldo, tasa_interes):
        super().__init__(numero_cuenta, saldo)
        self.tasa_interes = tasa_interes

class CuentaCorriente(Cuenta):
    def __init__(self, numero_cuenta, saldo, sobregiro_permitido):
        super().__init__(numero_cuenta, saldo)
        self.sobregiro_permitido = sobregiro_permitido

class CuentaInversion(Cuenta):
    def __init__(self, numero_cuenta, saldo, rendimiento):
        super().__init__(numero_cuenta, saldo)
        self.rendimiento = rendimiento


if __name__ == "__main__":
    ahorro = CuentaAhorro("001", 1500, 0.03)
    corriente = CuentaCorriente("002", 800, 500)
    inversion = CuentaInversion("003", 10000, 0.08)

    print(ahorro.mostrar_info())
    print(f"Tasa de interes: {ahorro.tasa_interes}", "\n")

    print(corriente.mostrar_info())
    print(f"Sobregiro permitido: {corriente.sobregiro_permitido}", "\n")

    print(inversion.mostrar_info())
    print(f"Rendimiento: {inversion.rendimiento}", "\n")
