from core.mixins import SerializableMixin
from models.base import BaseModel

class Pago(BaseModel, SerializableMixin):
    contador = 1

    def __init__(self, prestamo, fecha, valor):
        self.id = Pago.contador
        Pago.contador += 1
        self.prestamo = prestamo
        self.fecha = fecha
        self.valor = valor

    def __str__(self):
        return f"Pago {self.id}"
