class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def precio_final(self):
        return self.precio * 1.15

class Televisor(Producto):
    def __init__(self, nombre, precio, tamaño_pulgadas):
        super().__init__(nombre, precio)
        self.tamaño_pulgadas = tamaño_pulgadas

class Telefono(Producto):
    def __init__(self, nombre, precio, numero_sim):
        super().__init__(nombre, precio)
        self.numero_sim = numero_sim

class Laptop(Producto):
    def __init__(self, nombre, precio, ram):
        super().__init__(nombre, precio)
        self.ram = ram


if __name__ == "__main__":
    tv = Televisor("Samsung", 800, 55)
    celular = Telefono("iPhone", 1200, 1)
    laptop = Laptop("Lenovo", 950, "16GB")

    print(tv.nombre)
    print(f"Precio con IVA: {tv.precio_final()}", "\n")

    print(celular.nombre)
    print(f"Precio con IVA: {celular.precio_final()}", "\n")

    print(laptop.nombre)
    print(f"Precio con IVA: {laptop.precio_final()}", "\n")
