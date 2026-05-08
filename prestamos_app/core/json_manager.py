import json
import os

from models.empleado import Empleado
from models.prestamo import Prestamo
from models.pago import Pago

BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

archivo_empleados = os.path.join(BASE_DIR, "empleados.json")
archivo_prestamos = os.path.join(BASE_DIR, "prestamos.json")
archivo_pagos = os.path.join(BASE_DIR, "pagos.json")

def cargar_datos():

    # --------------------------
    # EMPLEADOS
    empleados = []

    if os.path.exists(archivo_empleados):

        with open(archivo_empleados, "r", encoding="utf-8") as f:

            data_empleados = json.load(f)

            for e in data_empleados:

                emp = Empleado(
                    e["nombre"],
                    e["cedula"],
                    e["sueldo"]
                )

                emp.id = e["id"]

                empleados.append(emp)

    # --------------------------
    # PRESTAMOS
    prestamos = []

    if os.path.exists(archivo_prestamos):

        with open(archivo_prestamos, "r", encoding="utf-8") as f:

            data_prestamos = json.load(f)

            for p in data_prestamos:

                emp = next(
                    (e for e in empleados if e.id == p["empleado"]["id"]),
                    None
                )

                if emp:

                    pr = Prestamo(
                        emp,
                        p["fecha"],
                        p["monto"],
                        p["cuotas"]
                    )

                    pr.id = p["id"]
                    pr.saldo = p["saldo"]

                    prestamos.append(pr)

    # --------------------------
    # PAGOS
    pagos = []

    if os.path.exists(archivo_pagos):

        with open(archivo_pagos, "r", encoding="utf-8") as f:

            data_pagos = json.load(f)

            for p in data_pagos:

                pr = next(
                    (x for x in prestamos if x.id == p["prestamo"]["id"]),
                    None
                )

                if pr:

                    pago = Pago(
                        pr,
                        p["fecha"],
                        p["valor"]
                    )

                    pago.id = p["id"]

                    pagos.append(pago)

    return {
        "empleados": empleados,
        "prestamos": prestamos,
        "pagos": pagos
    }


def guardar_datos(db):

    data = {

        "empleados": [
            {
                "id": e.id,
                "nombre": e.nombre,
                "cedula": e.cedula,
                "sueldo": e.sueldo
            }
            for e in db["empleados"]
        ],

        "prestamos": [
            {
                "id": p.id,
                "fecha": p.fecha,
                "monto": p.monto,
                "cuotas": p.cuotas,
                "saldo": p.saldo,
                "empleado": {
                    "id": p.empleado.id
                }
            }
            for p in db["prestamos"]
        ],

        "pagos": [
            {
                "id": p.id,
                "fecha": p.fecha,
                "valor": p.valor,
                "prestamo": {
                    "id": p.prestamo.id
                }
            }
            for p in db["pagos"]
        ]
    }

    with open(archivo_empleados, "w", encoding="utf-8") as f:
        json.dump(data["empleados"], f, indent=4)

    with open(archivo_prestamos, "w", encoding="utf-8") as f:
        json.dump(data["prestamos"], f, indent=4)

    with open(archivo_pagos, "w", encoding="utf-8") as f:
        json.dump(data["pagos"], f, indent=4)


db = cargar_datos()

empleados = db["empleados"]
prestamos = db["prestamos"]
pagos = db["pagos"]