
from core.json_manager import *

def calcular_estadisticas():
    total_prestamos = len(prestamos)
    total_pagos = len(pagos)

    montos = [p.monto for p in prestamos]

    if montos:
        total = sum(montos)
        promedio = total / len(montos)
        maximo = max(montos)
        minimo = min(montos)
    else:
        total = promedio = maximo = minimo = 0

    pendientes = len([p for p in prestamos if p.saldo > 0])
    pagados = len([p for p in prestamos if p.saldo == 0])
    saldo_total = sum(p.saldo for p in prestamos)

    return {
        "total_prestamos": total_prestamos,
        "total_pagos": total_pagos,
        "total": total,
        "promedio": promedio,
        "maximo": maximo,
        "minimo": minimo,
        "pendientes": pendientes,
        "pagados": pagados,
        "saldo_total": saldo_total
    }