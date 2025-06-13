class Habitacion:
    def __init__(self, numero, precio_noche):
        self.numero = numero
        self.precio_noche = precio_noche

    def mostrar_info(self):
        return f"Habitacion: {self.numero}\nPrecio por noche: {self.precio_noche}"

class Suite(Habitacion):
    def __init__(self, numero, precio_noche, jacuzzi):
        super().__init__(numero, precio_noche)
        self.jacuzzi = jacuzzi

class HabitacionFamiliar(Habitacion):
    def __init__(self, numero, precio_noche, capacidad_niños):
        super().__init__(numero, precio_noche)
        self.capacidad_niños = capacidad_niños

class HabitacionEstandar(Habitacion):
    def __init__(self, numero, precio_noche, vista):
        super().__init__(numero, precio_noche)
        self.vista = vista


if __name__ == "__main__":
    suite = Suite("101", 150, True)
    familiar = HabitacionFamiliar("102", 120, 3)
    estandar = HabitacionEstandar("103", 90, False)

    print(suite.mostrar_info())
    print(f"Jacuzzi: {'si' if suite.jacuzzi else 'no'}", "\n")

    print(familiar.mostrar_info())
    print(f"Capacidad de niños: {familiar.capacidad_niños}", "\n")

    print(estandar.mostrar_info())
    print(f"Vista al mar: {'si' if estandar.vista else 'no'}", "\n")
