# Caracteres de Escape en Python

Los caracteres de escape son secuencias especiales que representan caracteres que no se pueden escribir directamente en una cadena (string).

Se utilizan dentro de cadenas de texto (entre comillas simples `''` o dobles `"`) y comienzan con una barra invertida `\`.

En esta tabla se pueden ver los caracteres de escape más comunes en Python:

| Carácter de Escape | Descripción                       | Ejemplo                        | Resultado                              |
|--------------------|-----------------------------------|--------------------------------|----------------------------------------|
| `\n`              | Nueva línea (salto de línea)      | `print("Hola\nMundo")`         | Hola<br>Mundo                          |
| `\t`              | Tabulación horizontal             | `print("Nombre:\tValor")`      | Nombre: Valor (con un espacio de tabulación entre Nombre y Valor) |
| `\\`              | Barra invertida literal           | `print("La ruta es C:\\Archivos\\Ejemplo")` | La ruta es C:\Archivos\Ejemplo |
| `\'`              | Comilla simple literal            | `print('It\'s a beautiful day')` | It's a beautiful day         |
| `\"`              | Comilla doble literal             | `print("Ella dijo: \"Hola\"")` | Ella dijo: "Hola"              |
| `\r`              | Retorno de carro (mueve el cursor al principio de la línea actual) | `print("Hola\rMundo")` | Mundo (reemplaza "Hola" con "Mundo" en la misma línea) |
| `\b`              | Retroceso (borra el carácter anterior) | `print("Hola\bMundo")`     | HolaMundo (elimina el espacio entre "Hola" y "Mundo") |
| `\f`              | Salto de página                   | `print("Página 1\fPágina 2")`  | (Depende del intérprete/entorno; puede no mostrarse como un salto de página) |
| `\v`              | Tabulación vertical               | `print("Columna 1\vColumna 2")` | (Depende del intérprete/entorno; puede no mostrarse como tabulación vertical) |

---

| Carácter de Escape | Descripción                       | Ejemplo                        | Resultado                              |
|--------------------|-----------------------------------|--------------------------------|----------------------------------------|
| `\ooo`            | Carácter con valor octal ooo (donde ooo son tres dígitos octales) | `print("\101")` (101 en octal es 65 en decimal, que corresponde a 'A') | A |
| `\xhh`            | Carácter con valor hexadecimal hh (donde hh son dos dígitos hexadecimales) | `print("\x41")` (41 en hexadecimal es 65 en decimal, que es 'A') | A |
| `\uhhhh`          | Carácter Unicode con valor hexadecimal hhhh (4 dígitos) | `print("\u0394")`          | Δ (Letra griega Delta mayúscula)       |
| `\Uhhhhhhhh`      | Carácter Unicode con valor hexadecimal hhhhhhhh (8 dígitos) | `print("\U0001F600")`      | 😀 (Emoji "Grinning Face")             |

## Ejemplos Adicionales:

- **Usando `\n` para crear párrafos:**
```python
texto = "Este es el primer párrafo.\nEste es el segundo párrafo."
print(texto)