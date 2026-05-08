def validar_texto(txt):
    txt = txt.strip()
    return all(p.isalpha() for p in txt.split()) and len(txt) >= 3

def validar_numero_positivo(valor):
    try:
        valor = float(valor)
        return 400 <= valor <= 50000
    except:
        return False
    

def validar_cedula(cedula):
    if not cedula.isdigit() or len(cedula) != 10:
        return False

    provincia = int(cedula[:2])
    if provincia < 1 or provincia > 24:
        return False

    coef = [2,1,2,1,2,1,2,1,2]
    suma = 0

    for i in range(9):
        v = int(cedula[i]) * coef[i]
        if v >= 10:
            v -= 9
        suma += v

    digito = (10 - (suma % 10)) % 10
    return digito == int(cedula[9])

from datetime import datetime

def validar_fecha(fecha):
    try:
        fecha_ingresada = datetime.strptime(fecha, "%Y-%m-%d").date()
        fecha_actual = datetime.now().date()

        if fecha_ingresada != fecha_actual:
            print("❌ Solo se permite la fecha actual")
            return False

        return True

    except:
        print("❌ Formato inválido. Use YYYY-MM-DD")
        return False
    
def validar_prestamo_por_sueldo(sueldo, monto):

    sueldo = float(sueldo)
    monto = float(monto)

    if 300 <= sueldo <= 500:
        return monto <= 8000

    elif 501 <= sueldo <= 1000:
        return monto <= 20000

    elif sueldo > 1000:
        return monto <= 50000

    return False
