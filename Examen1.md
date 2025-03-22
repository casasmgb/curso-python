
## Ejercicio 1
Escribir un programa que pida al usuario un numero entero y calcule la suma de sus dígitos.
**Respuesta Esperada:**
```
Ingresa un número: 1234
La suma de los dígitos es: 10
```
## Ejercicio 2
Escribir un programa que identifique si un números es perfecto:
**Nota.-** Un **número perfecto** es un número entero positivo que es igual a la suma de sus **divisores propios** positivos (excluyendo al propio número)
ejemplo: 
para el **número 6**: generar sus divisores enteros
|indice|0|**1**|**2**|**3**|4|5|6|
|-|-|-|-|-|-|-|-|
|división|6/0|**6/1**|**6/2**|**6/3**|6/4|6/5|6/6|
|resto|X|**0**|**0**|**0**|0.5|1.2|X
Suma: 
1 + 2 + 3 = 6
Probar con los numeros: **6, 28, 496**
**Respuesta Esperada:**
```
Introduce un número:  28
El números 28 es perfecto
```
## Ejercicio 3
Escribir un programa que identifique si un números es **Un número Armstrong**
**Nota.-** Un **número de Armstrong** es un número que es igual a la suma de sus propios dígitos elevados a la potencia del número de dígitos.
ejemplo: 
el **número 153**: tiene 3 digitos, y se deben sumar sus digitos elevados al numero total de digitos.
$1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153$
el **número 1634**: tiene 4 digitos, y se deben sumar sus digitos elevados al numero total de digitos.
$1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634$
Probar con los numeros: **1, 153, 370, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084**
**Respuesta Esperada:**
```
Introduce un número:  153
El números 153 es un número Armstrong
```
