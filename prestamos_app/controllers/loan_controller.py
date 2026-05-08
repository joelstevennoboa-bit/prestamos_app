from core.json_manager import guardar_datos, db, prestamos, pagos

def crear_prestamo(p):
    prestamos.append(p)
    guardar_datos(db)


def eliminar_prestamo(id_p):

    # eliminar pagos relacionados
    pagos[:] = [p for p in pagos if p.prestamo.id != id_p]
    
    # eliminar préstamo
    prestamos[:] = [p for p in prestamos if p.id != id_p]

    guardar_datos(db)
    return True