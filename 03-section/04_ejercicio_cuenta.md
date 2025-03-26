# Ejercicio: 
# Sistema de Registro de Transacciones Financieras

### Objetivo:
1. Registrar transacciones (depósitos y retiros).

2. Calcular el saldo actual.

3. Generar un resumen de movimientos.

### Que se debe crear
* Clase `CuentaBancaria` con:

  * Atributos: 
    * `titular`
    * `saldo_inicial`
    * `movimientos` (debe ser una lista).

  * Métodos:

    * `depositar(monto)`: Añade el monto al saldo y registra la transacción.

    * `retirar(monto)`: Resta el monto (si hay saldo suficiente) y registra la transacción.

    * `mostrar_saldo()`: Imprime el saldo actual.

    * `mostrar_movimientos()`: Muestra todas las transacciones.



Seguir la siguiente estructura de codigo:

**Nota.-** en los metodos de la clase completar la logica segun los comentarios, y quitar la sentencia ```pass```

Archivo `ClaseCuentaBancaria.py`
```python
import datetime

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        self.movimientos = []  # Lista de tuplas: (fecha, tipo, monto, saldo)

    def depositar(self, monto):
        # Completar lo siguiente: 
        # 1. actualizar saldo 
        # 2. añadir movimiento de deposito (fecha, tipo, monto, saldo) 
        # 3. Mostrar mensaje de depósito exitoso
        pass

    def retirar(self, monto):
        # Completar lo siguiente: 
        # 1. Validar saldo, y si es insuficiente mostrar mensaje
        # 2. Actualizar saldo
        # 3. Añadir movimiento de retiro (fecha, tipo, monto, saldo) 
        # 4. Mostrar mensaje de retiro exitoso
        pass

    def mostrar_saldo(self):
        # Completar lo siguiente: 
        # 1. mostrar mensaje con nombre de titular y su saldo.
        pass

    def mostrar_movimientos(self):
        print(f"\n--- Historial de {self.titular} ---")
        # Completar lo siguiente: 
        # 1. iterar la lista de movimientos y mostar la fecha, tipo el monto y el saldo.
        pass

```

Para verificar la logica ejecutar el archivo `main.py` 

Archivo `main.py`
```python 
from ClaseCuentaBancaria import CuentaBancaria

# ------ Ejemplo de uso ------  
cuenta = CuentaBancaria("Carlos López", 1000)
cuenta.depositar(300)
cuenta.retirar(200)
cuenta.retirar(1500)  # Fallará por saldo insuficiente.
cuenta.mostrar_saldo()
cuenta.mostrar_movimientos()
```
