class MiembroUniversidad:
    def __init__(self, nombre, id_universitario, correo):
        self.nombre = nombre
        self.id_universitario = id_universitario
        self.correo = correo

    def mostrar_info(self):
        return f"{self.nombre}\nID: {self.id_universitario}\nCorreo: {self.correo}\n"

class Estudiante(MiembroUniversidad):
    def __init__(self, nombre, id_universitario, correo, carrera, promedio):
        super().__init__(nombre, id_universitario, correo)
        self.carrera = carrera
        self.promedio = promedio

    def mostrar_info(self):
        return super().mostrar_info() + f"Carrera: {self.carrera}\nPromedio: {self.promedio}\n"

class Docente(MiembroUniversidad):
    def __init__(self, nombre, id_universitario, correo, materia):
        super().__init__(nombre, id_universitario, correo)
        self.materia = materia

    def mostrar_info(self):
        return super().mostrar_info() + f"Materia: {self.materia}\n"

class Administrativo(MiembroUniversidad):
    def __init__(self, nombre, id_universitario, correo, departamento):
        super().__init__(nombre, id_universitario, correo)
        self.departamento = departamento

    def mostrar_info(self):
        return super().mostrar_info() + f"Departamento: {self.departamento}\n"


if __name__ == "__main__":
    estudiante = Estudiante("Alvarito", "20231001", "alvaritoalvarez@mail.com", "Ingenieria", 8.5)
    docente = Docente("Carlos", "10001", "carrilo@pycharm.com", "Matematicas")
    administrativo = Administrativo("Habibi", "30002", "habibi@utpl.edu.ec", "Finanzas")

    print(estudiante.mostrar_info())
    print(docente.mostrar_info())
    print(administrativo.mostrar_info())
