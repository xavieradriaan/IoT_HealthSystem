class Paciente:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

class Cita:
    def __init__(self, dni, fecha, motivo):
        self.dni = dni
        self.fecha = fecha
        self.motivo = motivo
