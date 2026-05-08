from core.mixins import SerializableMixin
from models.base import BaseModel

class Prestamo(BaseModel, SerializableMixin):
    contador = 1

    def __init__(self, empleado, fecha, monto, cuotas):
        self.id = Prestamo.contador
        Prestamo.contador += 1
        self.empleado = empleado
        self.fecha = fecha
        self.monto = monto
        self.cuotas = cuotas
        self.saldo = monto

    def __str__(self):
        return f"{self.id} - {self.empleado.nombre} - ${self.saldo}"

