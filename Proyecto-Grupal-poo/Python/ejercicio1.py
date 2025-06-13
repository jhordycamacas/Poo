class Animal:
    def __init__(self, nombre, edad, tipo_alimentacion):
        self.nombre = nombre
        self.edad = edad
        self.tipo_alimentacion = tipo_alimentacion

    def mostrar_info(self):
        return f"{self.nombre}\nEdad: {self.edad}\nAlimentacion: {self.tipo_alimentacion}"

class Ave(Animal):
    def volar(self):
        return f"{self.nombre} esta volando"

class Mamifero(Animal):
    def amamantar(self):
        return f"{self.nombre} esta amamantando a sus crias"

class Reptil(Animal):
    def reptar(self):
        return f"{self.nombre} esta reptando."


if __name__ == "__main__":
    loro = Ave("Loro", 3, "herbivoro")
    leon = Mamifero("Leon", 5, "carnivoro")
    iguana = Reptil("Iguana", 2, "omnivoro")

    print(loro.mostrar_info())
    print(loro.volar(),"\n")

    print(leon.mostrar_info())
    print(leon.amamantar(),"\n")

    print(iguana.mostrar_info())
    print(iguana.reptar(),"\n")
