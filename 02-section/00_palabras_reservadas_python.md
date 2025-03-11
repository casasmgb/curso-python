# Palabras Clave Esenciales de Python con Ejemplos

## 1. `print()`

- **Descripción:** Muestra texto o variables en la consola.
- **Ejemplo:**
```python
print("Hola, mundo!")  # Imprime "Hola, mundo!"
nombre = "Juan"
print("Hola,", nombre)  # Imprime "Hola, Juan"
print(2 + 2)  # Imprime 4
```
## 2. `input()`

- **Descripción:** Permite que el usuario ingrese datos a través del teclado. Siempre devuelve una cadena (string).
- **Ejemplo:**
```python
nombre = input("Ingresa tu nombre: ")
print("Hola,", nombre + "!")
edad = input("Ingresa tu edad: ")
edad = int(edad)  # Convierte la entrada a un entero
print("Tienes", edad, "años.")
```

## 3. `if, elif, else`

- **Descripción:** Sentencias condicionales que permiten ejecutar diferentes bloques de código basados en si una condición es verdadera o falsa.
- **Ejemplo:**
```python
edad = 18
if edad >= 18:
    print("Eres mayor de edad.")
elif edad >= 16:
    print("Puedes obtener un permiso de conducir.")
else:
    print("Eres menor de edad.")
```

## N. `for`

- **Descripción:** Bucle que itera sobre una secuencia (lista, tupla, cadena, rango, etc.).
- **Ejemplo:**
```python
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print("Me gusta la", fruta)
for i in range(5):  # Itera de 0 a 4
    print(i)
```

## 5. `while`

- **Descripción:**Bucle que se ejecuta mientras una condición sea verdadera. 
- **Ejemplo:**
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

## 6. `def`

- **Descripción:** Define una función.
- **Ejemplo:**
```python
def saludar(nombre):
    print("Hola,", nombre + "!")

# llamada de la funcion
saludar("Ana")
```

## 7. `return`

- **Descripción:** Devuelve un valor desde una función.
- **Ejemplo:**
```python
def sumar(a, b):
    return a + b

# llamada de la funcion
resultado = sumar(5, 3)
print(resultado)  # Imprime 8
```

## 8. `import`

- **Descripción:** Importa módulos para usar sus funciones y clases.
- **Ejemplo:**
```python
import math
radio = 5
area = math.pi * radio**2
print("El área del círculo es:", area)
```

## 9. `try, except`

- **Descripción:** Manejo de excepciones (errores). `try` intenta ejecutar un bloque de código, y `except` captura un error si ocurre.
- **Ejemplo:**
```python
try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print("Resultado:", resultado)
except ValueError:
    print("Debes ingresar un número entero válido.")
except ZeroDivisionError:
    print("No se puede dividir por cero.")
```

## 10. `and, or, not`

- **Descripción:** Operadores lógicos. and requiere que ambas condiciones sean verdaderas, or requiere que al menos una condición sea verdadera, not niega una condición.
- **Ejemplo:**
```python
edad = 20
tiene_licencia = True
if edad >= 18 and tiene_licencia:
    print("Puede conducir.")
if edad < 18 or not tiene_licencia:
    print("No puede conducir (aún).")
```
