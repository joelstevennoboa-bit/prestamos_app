from core.decorators import log_action
from core.json_manager import guardar_datos, db, empleados, prestamos

@log_action
def crear_empleado(e):

    for emp in empleados:
        if emp.cedula == e.cedula:
            return False

    empleados.append(e)

    guardar_datos(db)

    return True

@log_action
def eliminar_empleado(id_emp):

    global empleados, prestamos

    for p in prestamos:
        if p.empleado.id == id_emp and p.saldo > 0:
            return False

    empleados[:] = [e for e in empleados if e.id != id_emp]

    guardar_datos(db)

    return True