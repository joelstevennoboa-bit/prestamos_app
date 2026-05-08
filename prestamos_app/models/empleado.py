from core.mixins import SerializableMixin
from models.base import BaseModel

class Empleado(SerializableMixin):
    contador = 1

    def __init__(self, nombre, cedula, sueldo):
        self.id = Empleado.contador
        Empleado.contador += 1
        self.nombre = nombre
        self.cedula = cedula
        self.sueldo = sueldo

    def __str__(self):
        return f"{self.id} - {self.nombre}"
