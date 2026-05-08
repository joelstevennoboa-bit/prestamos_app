# Sistema de Préstamos con JSON

Aplicación de consola en Python que permite gestionar **empleados**, **préstamos** y **pagos**, almacenando la información en archivos JSON. Desarrollada como práctica de Programación Orientada a Objetos aplicando arquitectura tipo **MVC**, validaciones, reutilización de código y persistencia de datos.

---

# 1. Estructura del proyecto (MVC)

```text
prestamos_app.v2.1/
├── main.py
├── README.md
│
├── controllers/                   # C — Lógica de negocio
│   ├── employee_controller.py
│   ├── loan_controller.py
│   ├── payment_controller.py
│   └── statistics_controller.py
│
├── models/                        # M — Entidades del sistema
│   ├── base.py
│   ├── empleado.py
│   ├── prestamo.py
│   └── pago.py
│
├── views/                         # V — Interfaz consola
│   └── menu.py
│
├── core/                          # Núcleo del sistema
│   ├── json_manager.py            # Lectura y escritura JSON
│   └── mixins.py                  # Mixins y reutilización
│
├── data/                          # Persistencia de datos
│   ├── empleados.json
│   ├── prestamos.json
│   └── pagos.json
│
├── utils/                         # Utilidades y validaciones
│   ├── helpers.py
│   ├── ui.py
│   └── validaciones.py
```

---

# 2. Arquitectura por capas (MVC)

El sistema sigue el patrón **Modelo–Vista–Controlador (MVC)**:

```text
┌──────────────────────────────────────────────┐
│  main.py → views/menu.py   (V — Interfaz)   │
└───────────────────────┬──────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────┐
│  controllers/       (C — Lógica negocio)    │
│  - employee_controller                       │
│  - loan_controller                           │
│  - payment_controller                        │
│  - statistics_controller                     │
└───────────────────────┬──────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────┐
│  models/             (M — Entidades)         │
│  - Empleado                                 │
│  - Prestamo                                 │
│  - Pago                                     │
└───────────────────────┬──────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────┐
│  core/json_manager.py  (Persistencia JSON)  │
└───────────────────────┬──────────────────────┘
                        │
                        ▼
        empleados.json / prestamos.json / pagos.json
```

---

# 3. Flujo general del sistema

## 3.1 Inicio

El archivo `main.py` ejecuta el sistema:

```python
from views.menu import menu

if __name__ == "__main__":
    menu()
```

---

## 3.2 Menú principal

El sistema permite:

```text
SISTEMA DE PRESTAMOS

1. Crear empleado
2. Crear préstamo
3. Registrar pago
4. Consultas
5. Eliminar
6. Estadísticas
7. Salir
```

---

## 3.3 Registro de empleado

- Se ingresan: nombre, cédula y sueldo.
- El sistema valida:
  - Texto correcto.
  - Cédula válida.
  - Sueldo positivo.
- Los datos se almacenan en `empleados.json`.

---

## 3.4 Registro de préstamo

Flujo:

1. Seleccionar empleado por ID.
2. Ingresar:
   - Fecha (`YYYY-MM-DD`)
   - Monto
   - Número de cuotas
3. El sistema calcula:
   - Cuota
   - Saldo inicial
4. Se almacena el préstamo en `prestamos.json`.

---

## 3.5 Registro de pago

Flujo:

1. Seleccionar préstamo.
2. Mostrar:
   - Empleado
   - Saldo actual
3. Ingresar valor del pago.
4. Validar que no supere el saldo.
5. Actualizar saldo pendiente.
6. Guardar el pago en `pagos.json`.

---

## 3.6 Estadísticas

El sistema calcula:

- Total de préstamos.
- Total de pagos.
- Monto total prestado.
- Promedio de préstamos.
- Máximo y mínimo.
- Préstamos pendientes.
- Préstamos pagados.
- Saldo total pendiente.

---

# 4. Persistencia de datos JSON

El sistema almacena la información en archivos JSON independientes:

```text
data/
├── empleados.json
├── prestamos.json
└── pagos.json
```

Esto permite mantener los datos guardados aunque el programa se cierre.

---

# 5. Conceptos de Programación Orientada a Objetos

| Concepto         | Aplicación                                      |
| ---------------- | ------------------------------------------------ |
| Encapsulamiento  | Cada clase administra sus propios datos          |
| Clases y objetos | Empleado, Prestamo y Pago                        |
| Abstracción      | Separación entre vista, lógica y modelos         |
| Modularidad      | Código organizado en carpetas                    |
| Reutilización    | Uso de mixins, helpers y funciones reutilizables |
| Persistencia     | Almacenamiento mediante archivos JSON            |

---

# 6. Ejecución del proyecto

Desde la carpeta raíz:

```bash
python main.py
```

✔ No requiere librerías externas.  
✔ Usa únicamente módulos estándar de Python (`json`, `os`, etc.).

---

# 7. Flujo resumido

```text
Usuario → Menú → Controllers
                     │
                     ▼
                 Models
                     │
                     ▼
          json_manager.py
                     │
                     ▼
        Archivos JSON (data/)
```

---

# 8. Notas finales

- El sistema utiliza persistencia en JSON.
- Mantiene los datos almacenados aunque se cierre el programa.
- Sigue una arquitectura MVC simplificada.
- Implementa Programación Orientada a Objetos.
- Usa modularidad y reutilización mediante mixins y utilidades.
- Aplicación completamente funcional en consola.