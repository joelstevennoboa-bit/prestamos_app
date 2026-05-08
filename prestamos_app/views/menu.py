from utils.ui import *
from models.empleado import Empleado
from models.prestamo import Prestamo
from models.pago import Pago

from utils.validaciones import *
from utils.helpers import pedir_valor

from controllers.employee_controller import *
from controllers.loan_controller import *
from controllers.payment_controller import *
from controllers.statistics_controller import calcular_estadisticas
from core.json_manager import *


def pausa():
    input("\nPresione ENTER para continuar...")



# =========================
# EMPLEADO
# =========================

def pantalla_empleado():
    limpiar()
    titulo("REGISTRO DE EMPLEADO")
    print("ID: [AUTOMÁTICO]")

    nombre = pedir_valor("Nombre: ", validar_texto)
    cedula = pedir_valor("Cédula: ", validar_cedula)
    sueldo = float(pedir_valor("Sueldo: ", validar_numero_positivo))
    
    while True:
     print("\n¿Desea guardar?")
     print("1. Sí")
     print("2. No")

     op = input("Opción: ")

     if op == "1":
        emp = Empleado(nombre, cedula, sueldo)
        
        if  crear_empleado(emp):
            print("✔ Guardado")
        else:
            print("❌ Cédula ya existe")
        
        break

     elif op == "2":
        print("✖ Cancelado")
        break

     else:
        print("❌ Opción inválida")

    pausa()


# =========================
# PRESTAMO
# =========================

def pantalla_prestamo():
    limpiar()
    titulo("REGISTRO DE PRÉSTAMO")

    if not empleados:
        print("❌ No hay empleados registrados")
        pausa()
        return

    for e in empleados:
        print(e)

    # -------------------------
    emp = None

    while True:
        valor = input("ID empleado (0 para salir): ")

        if valor == "0":
            print("↩ Cancelando...")
            pausa()
            return

        try:
            id_emp = int(valor)
        except:
            print("❌ Debe ingresar un número")
            continue

        emp = next((e for e in empleados if e.id == id_emp), None)

        if emp is None:
            print("❌ Empleado no encontrado")
        else:
            break

    # -------------------------
    fecha = pedir_valor("Fecha (YYYY-MM-DD): ", validar_fecha)

    while True: 

      monto = float(pedir_valor("Monto: ", validar_numero_positivo))

      if validar_prestamo_por_sueldo(emp.sueldo, monto):
         break

      print("❌ El sueldo del empleado no permite solicitar ese monto")

    cuotas = int(pedir_valor("Número de cuotas: ", lambda x: x.isdigit() and int(x)>0))

    interes = monto * 0.15
    total = monto + interes
    
    print(f"Interés: $ {interes:.2f}")
    print(f"Total a pagar: $ {total:.2f}")
    print(f"Cuota: ${total/cuotas:.2f}")
    print(f"Saldo: ${monto:.2f}")

    # -------------------------
    while True:
        print("\n¿Guardar?")
        print("1. Sí")
        print("2. No")

        op = input("Opción: ")

        if op == "1":
            p = Prestamo(emp, fecha, monto, cuotas)
            crear_prestamo(p)
            print("✔ Guardado")
            break

        elif op == "2":
            print("✖ Cancelado")
            break

        else:
            print("❌ Opción inválida")

    pausa()


# =========================
# PAGO
# =========================

def pantalla_pago():
    limpiar()
    print("="*40)
    print("REGISTRO DE PAGO")
    print("="*40)
    print("ID: [AUTO]")

    for p in prestamos:
        print(p)

    prestamo = None

    while True:
        valor = input("ID préstamo (0 para salir): ")
         
        if valor == "0":
            print("✖ Registro cancelado")
            pausa()
            return

        try:
            id_p = int(valor)
        except:
            print("❌ Debe ingresar un número")
            continue

        prestamo = next((p for p in prestamos if p.id == id_p), None)

        if prestamo is None:
            print("❌ Préstamo no encontrado")
        else:
             if prestamo.saldo == 0:
                print("❌ Este préstamo ya está cancelado")
                pausa()
                return
             break

    print(f"Empleado: {prestamo.empleado.nombre}")
    print(f"Monto: $ {prestamo.monto}")
    print(f"Saldo actual: $ {prestamo.saldo}")

    valor = float(pedir_valor("Valor pago: ", validar_numero_positivo))

    if valor > prestamo.saldo:
        print("❌ Pago mayor al saldo")
        pausa()
        return

    print("-"*40)
    print(f"Saldo después: $ {prestamo.saldo - valor}")
    print("-"*40)

    while True:
        op = input("¿Confirmar? (1=Sí / 2=No): ")

        if op == "1":
            pago = Pago(prestamo, "hoy", valor)
            registrar_pago(pago)
            print("✔ Pago registrado")
            break

        elif op == "2":
            print("✖ Cancelado")
            break

        else:
            print("❌ Opción inválida")

    pausa()


# =========================
# ELIMINAR
# =========================

def pantalla_eliminar():
    while True:
        limpiar()
        titulo("ELIMINAR")

        print("1. Eliminar empleado")
        print("2. Eliminar préstamo")
        print("3. Volver")

        op = input("Opción: ")

        # ------------------------
        if op == "1":
            if not empleados:
                print("❌ No hay empleados")
                pausa()
                continue

            for e in empleados:
                print(e)

            while True:
                valor = input("ID empleado (0 para cancelar): ")

                if valor == "0":
                    break

                try:
                    id_emp = int(valor)
                except:
                    print("❌ Número inválido")
                    continue

                if eliminar_empleado(id_emp):
                    print("✔ Empleado eliminado")
                else:
                    print("❌ No se puede eliminar (tiene préstamos o no existe)")
                break

            pausa()

        # ------------------------
        elif op == "2":
            if not prestamos:
                print("❌ No hay préstamos")
                pausa()
                continue

            for p in prestamos:
                print(p)

            while True:
                valor = input("ID préstamo (0 para cancelar): ")

                if valor == "0":
                    break

                try:
                    id_p = int(valor)
                except:
                    print("❌ Número inválido")
                    continue

                eliminar_prestamo(id_p)
                print("✔ Préstamo eliminado")
                break

            pausa()

        # ------------------------
        elif op == "3":
            break

        else:
            print("❌ Opción inválida")
            pausa()


# =========================
# CONSULTAS
# =========================

def pantalla_consultas():
    while True:
        limpiar()
        titulo("CONSULTAS")

        print("1. Ver empleados")
        print("2. Buscar empleado por ID")
        print("3. Ver préstamos")
        print("4. Buscar préstamo por ID")
        print("5. Volver")

        op = input("Opción: ")

        # --------------------
        if op == "1":
            if not empleados:
                print("❌ No hay empleados")
            else:
                for e in empleados:
                    print(e)
            pausa()

        # --------------------
        elif op == "2":
            try:
                id_emp = int(input("ID empleado: "))
            except:
                print("❌ Número inválido")
                pausa()
                continue

            emp = next((e for e in empleados if e.id == id_emp), None)

            if emp:
                print("\n DATOS DEL EMPLEADO")
                print(f"ID: {emp.id}")
                print(f"Nombre: {emp.nombre}")
                print(f"Cédula: {emp.cedula}")
                print(f"Sueldo: {emp.sueldo}")
            else:
                print("❌ No encontrado")

            pausa()

        # --------------------
        elif op == "3":
            if not prestamos:
                print("❌ No hay préstamos")
            else:
                for p in prestamos:
                    print(p)
            pausa()

        # --------------------
        elif op == "4":
            try:
                id_p = int(input("ID préstamo: "))
            except:
                print("❌ Número inválido")
                pausa()
                continue

            p = next((p for p in prestamos if p.id == id_p), None)

            if p:
                print("\n DETALLE DEL PRÉSTAMO")
                print(f"ID: {p.id}")
                print(f"Empleado: {p.empleado.nombre}")
                print(f"Monto: {p.monto}")
                print(f"Saldo: {p.saldo}")
                print(f"Cuotas: {p.cuotas}")

                cuota = p.monto / p.cuotas
                print(f"Cuota: {cuota:.2f}")
            else:
                print("❌ No encontrado")

            pausa()

        # --------------------
        elif op == "5":
            break

        else:
            print("❌ Opción inválida")
            pausa()


# =========================
# ESTADISTICAS
# =========================

def pantalla_estadisticas():
    limpiar()
    print("="*40)
    print("ESTADÍSTICAS")
    print("="*40)

    datos = calcular_estadisticas()

    print(f"Total préstamos: {datos['total_prestamos']}")
    print(f"Total pagos: {datos['total_pagos']}")
    print(f"Monto total: $ {datos['total']}")
    print(f"Promedio: $ {datos['promedio']:.2f}")
    print(f"Máximo: $ {datos['maximo']}")
    print(f"Mínimo: $ {datos['minimo']}")
    print(f"Pendientes: {datos['pendientes']}")
    print(f"Pagados: {datos['pagados']}")
    print(f"Saldo total pendiente: $ {datos['saldo_total']}")

    pausa()

# =========================
# MENU 
# =========================

def menu():
    while True:
        limpiar()
        titulo("SISTEMA DE PRESTAMOS")

        print("1. Crear empleado")
        print("2. Crear prestamo")
        print("3. Registrar pago")
        print("4. Consultas")
        print("5. Eliminar")
        print("6. Estadisticas")
        print("7. Salir")

        op = input("Seleccione: ")

        if op == "1": 
          pantalla_empleado()
        elif op == "2": 
          pantalla_prestamo()
        elif op == "3": 
          pantalla_pago()
        elif op == "4":
            pantalla_consultas()
        elif op == "5":
          pantalla_eliminar()
        elif op == "6":
          pantalla_estadisticas()
        elif op == "7": 
            break
          
