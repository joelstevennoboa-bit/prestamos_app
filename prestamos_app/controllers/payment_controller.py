from core.json_manager import guardar_datos, db, prestamos, pagos

def registrar_pago(p):
    p.prestamo.saldo -= p.valor
    pagos.append(p)
    guardar_datos(db)

