# 🧮 Código Python con Explicaciones en Markdown

## **1. Lista de Números Impares**
```python
impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(impares)
```
###  Índices de la Lista
<table style="font-size: 18px; border-collapse: collapse; width: 100%; margin: 20px auto;">
  <thead>
    <tr>
      <th style="border: 1px solid #000; padding: 8px;">Valor</th>
      <th style="border: 1px solid #000; padding: 8px; background-color:rgb(5, 92, 135);">1</th>
      <th style="border: 1px solid #000; padding: 8px; background-color:rgb(5, 92, 135);">3</th>
      <th style="border: 1px solid #000; padding: 8px; background-color:rgb(5, 92, 135);">5</th>
      <th style="border: 1px solid #000; padding: 8px; background-color:rgb(5, 92, 135);">7</th>
      <th style="border: 1px solid #000; padding: 8px; background-color:rgb(52, 110, 7);">9</th>
      <th style="border: 1px solid #000; padding: 8px; background-color:rgb(5, 92, 135);">11</th>
      <th style="border: 1px solid #000; padding: 8px; background-color:rgb(5, 92, 135);">13</th>
      <th style="border: 1px solid #000; padding: 8px; background-color:rgb(5, 92, 135);">15</th>
      <th style="border: 1px solid #000; padding: 8px; background-color:rgb(5, 92, 135);">17</th>
      <th style="border: 1px solid #000; padding: 8px; background-color:rgb(5, 92, 135);">19</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #000; padding: 8px;"><strong>Índice Positivo</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>0</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>1</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>2</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>3</strong></td>
      <td style="border: 1px solid #000; padding: 8px; background-color:rgb(176, 32, 10);"><strong>4</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>5</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>6</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>7</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>8</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>9</strong></td>
    </tr>
    <tr>
      <td style="border: 1px solid #000; padding: 8px;"><strong>Índice Negativo</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>-9</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>-8</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>-7</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>-6</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>-5</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>-4</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>-3</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>-2</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>-1</strong></td>
    </tr>
  </tbody>
</table>

---

### **Explicación:**
1. **Valor**: Representa los elementos de la lista `[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]`.
2. **Índice Positivo**: Muestra los índices positivos (de `0` a `9`) para acceder a los elementos desde el inicio de la lista.
3. **Índice Negativo**: Muestra los índices negativos (de `-1` a `-9`) para acceder a los elementos desde el final de la lista.

## **3. Acceso a Elementos de la Lista**

```Python
# Mostar valore
print(impares[4])  # Mpstrara el numero 9
print(impares[-6])
print(impares[:4])
print(impares[4:])
```
### **Explicación:**
1. Se accede a elementos específicos de la lista usando índices positivos y negativos.
2. Se utilizan rebanadas (`slicing`) para obtener subconjuntos de la lista.

## **4. Mostrar Rangos de la Lista**
```python
# Mostrar rango
print(impares[3:7])
print(impares[-7:-3])

# No devuelve nada por el orden
print(impares[-3:-7]) 
```
### **Explicación:**
1. Se pueden obtener rangos de la lista usando índices positivos y negativos.
2. Si el rango está en orden inverso, no se devuelve nada.

## **5. Unión de Listas**
```python
pares = [2, 4, 6, 8, 10]
union = impares + pares 
print (union)
```

## **6. Adicion de valor a la lista**
```python
pares.append(12)
print (pares)
```
## **7. Reemplazar Valores en la Lista**
```python
print (impares)
impares[4:7] = [21, 23, 25]
print (impares)
```
## **8. Métodos de Listas**
```python
# Métodos
alfa_numerico = [1, 'a', 3, 'b', 5, 'a', 7, 'a', 'b']
print(alfa_numerico)

print(alfa_numerico.index('a'))  # Muestra la posición de la primera ocurrencia de 'a'
print(alfa_numerico.count('a'))  # Cuenta cuántas veces aparece 'a' en la lista

# Eliminar el último valor
print(alfa_numerico)
alfa_numerico.pop(5)  # Elimina el valor en la posición 5
print(alfa_numerico)

# Eliminar el primer valor que se encuentre
print(alfa_numerico)
alfa_numerico.remove('b')  # Elimina la primera ocurrencia de 'b'
print(alfa_numerico)

# Eliminar un rango de posiciones
print(alfa_numerico)
del alfa_numerico[2:6]  # Elimina los valores desde la posición 2 hasta la 5
print(alfa_numerico)

# Invertir la lista
print(alfa_numerico)
alfa_numerico.reverse()  # Invierte el orden de la lista
print(alfa_numerico)

# Ordenar
desordenado = [2, 5, 6, 9, 8, 4, 5, 2]
desordenado.sort()  # Ordena la lista de menor a mayor
print(desordenado)
```
## **9. Manipulación de Cadenas**
<h3>Tabla de Índices y Caracteres</h3>

<table style="font-size: 18px; border-collapse: collapse; width: 100%;">
  <thead>
    <tr>
      <th style="border: 1px solid #000; padding: 8px;">Carácter</th>
      <th style="border: 1px solid #000; padding: 8px; background-color:rgb(52, 110, 7);">H</th>
      <th style="border: 1px solid #000; padding: 8px; background-color:rgb(52, 110, 7);">e</th>
      <th style="border: 1px solid #000; padding: 8px; background-color:rgb(52, 110, 7);">l</th>
      <th style="border: 1px solid #000; padding: 8px; background-color:rgb(52, 110, 7);">l</th>
      <th style="border: 1px solid #000; padding: 8px; background-color:rgb(52, 110, 7);">o</th>
      <th style="border: 1px solid #000; padding: 8px; background-color:rgb(5, 92, 135);">_</th>
      <th style="border: 1px solid #000; padding: 8px; background-color:rgb(52, 110, 7);">f</th>
      <th style="border: 1px solid #000; padding: 8px; background-color:rgb(52, 110, 7);">r</th>
      <th style="border: 1px solid #000; padding: 8px; background-color:rgb(52, 110, 7);">o</th>
      <th style="border: 1px solid #000; padding: 8px; background-color:rgb(52, 110, 7);">m</th>
      <th style="border: 1px solid #000; padding: 8px; background-color:rgb(5, 92, 135);">_</th>
      <th style="border: 1px solid #000; padding: 8px; background-color:rgb(5, 92, 135);">p</th>
      <th style="border: 1px solid #000; padding: 8px; background-color:rgb(5, 92, 135);">y</th>
      <th style="border: 1px solid #000; padding: 8px; background-color:rgb(5, 92, 135);">t</th>
      <th style="border: 1px solid #000; padding: 8px; background-color:rgb(5, 92, 135);">h</th>
      <th style="border: 1px solid #000; padding: 8px; background-color:rgb(5, 92, 135);">o</th>
      <th style="border: 1px solid #000; padding: 8px; background-color:rgb(5, 92, 135);">n</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #000; padding: 8px;"><strong>word[:5]</strong></td>
      <td style="border: 1px solid #000; padding: 8px; background-color:rgb(176, 32, 10);"><strong>0</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>1</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>2</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>3</strong></td>
      <td style="border: 1px solid #000; padding: 8px; background-color:rgb(176, 96, 10);"><strong>4</strong></td>
      <td style="border: 1px solid #000; padding: 8px; background-color:rgb(176, 32, 10);"><strong>5</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>6</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>7</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>8</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>9</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>10</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>11</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>12</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>13</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>14</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>15</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>16</strong></td>
    </tr>
    <tr>
      <td style="border: 1px solid #000; padding: 8px;"><strong>word[6:10]</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>0</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>1</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>2</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>3</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>4</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>5</strong></td>
      <td style="border: 1px solid #000; padding: 8px; background-color:rgb(176, 32, 10);"><strong>6</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>7</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>8</strong></td>
      <td style="border: 1px solid #000; padding: 8px; background-color:rgb(176, 96, 10);"><strong>9</strong></td>
      <td style="border: 1px solid #000; padding: 8px; background-color:rgb(176, 32, 10);"><strong>10</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>11</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>12</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>13</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>14</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>15</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>16</strong></td>
    </tr>
    <tr>
      <td style="border: 1px solid #000; padding: 8px;"><strong>Índice Negativo</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>-16</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>-15</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>-14</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>-13</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>-12</strong></td>
      <td style="border: 1px solid #000; padding: 8px; background-color:rgb(176, 32, 10);"><strong>-11</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>-10</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>-9</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>-8</strong></td>
      <td style="border: 1px solid #000; padding: 8px; background-color:rgb(176, 32, 10);"><strong>-7</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>-6</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>-5</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>-4</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>-3</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>-2</strong></td>
      <td style="border: 1px solid #000; padding: 8px;"><strong>-1</strong></td>
    </tr>
  </tbody>
</table>

```python
word = 'Hello_from_python'
print(word)

print(word[:5])   # primeros 5 caracteres (Hello)
print(word[6:10]) # caracteres desde la posición 6 hasta la 9 (from)
print(word[-11:-7]) # caracteres desde la posición -7 hasta la -11 (from)
```

## **10. Matrices**


<h2 style="text-align: center;">Matriz</h2>

<table style="font-size: 18px; border-collapse: collapse; width: 100%;">
    <tr>
        <th></th>
        <th>0</th>
        <th>1</th>
        <th style=" background-color:rgb(176, 32, 10);">2</th>
        <th>3</th>
        <th>4</th>
    </tr>
    <tr>
        <th>0</th>
        <td style="border: 1px solid #000; padding: 8px; background-color:rgb(5, 92, 135);">10</td>
        <td style="border: 1px solid #000; padding: 8px; background-color:rgb(5, 92, 135);">12</td>
        <td style="border: 1px solid #000; padding: 8px; background-color:rgb(5, 92, 135);">14</td>
        <td style="border: 1px solid #000; padding: 8px; background-color:rgb(5, 92, 135);">16</td>
        <td style="border: 1px solid #000; padding: 8px; background-color:rgb(5, 92, 135);">18</td>
    </tr>
    <tr>
        <th style=" background-color:rgb(176, 32, 10);" >1</th>
        <td style="border: 1px solid #000; padding: 8px; background-color:rgb(5, 92, 135);">20</td>
        <td style="border: 1px solid #000; padding: 8px; background-color:rgb(5, 92, 135);">22</td>
        <td style="border: 1px solid #000; padding: 8px; background-color:rgb(52, 110, 7);">24</td>
        <td style="border: 1px solid #000; padding: 8px; background-color:rgb(5, 92, 135);">26</td>
        <td style="border: 1px solid #000; padding: 8px; background-color:rgb(5, 92, 135);">28</td>
    </tr>
</table>


```python
matriz = [ 
    [10, 12, 14, 16, 18], 
    [20, 22, 24, 26, 28] 
]

print(matriz[1][2])  # Muestra el valor 24 (fila 1, columna 2)
```
