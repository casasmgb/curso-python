impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(impares)

# |  1 |  3 |  5 |  7 |  9 |  11 |  13 |  15 |  17 |  19 |
# |  0 |  1 |  2 |  3 |  4 |   5 |   6 |   7 |   8 |   9 |
# |    | -9 | -8 | -7 | -6 |  -5 |  -4 |  -3 |  -2 |  -1 | 

# Mostar valore
print(impares[4])
print(impares[-6])
print(impares[:4])
print(impares[4:])

# Mostar Rango
print(impares[3:7])
print(impares[-7:-3])

# no devuelve nada por el orden
print(impares[-3:-7])

# Union de listas
pares = [2, 4, 6, 8, 10]
union = impares + pares 
print (union)

# Adicion de valor a la lista
pares.append(12)
print (pares)

# Reemplazar valore
print (impares)
impares[4:7] = [21, 23, 25]
print (impares)


# Metodos
alfa_numerico = [1, 'a', 3, 'b', 5, 'a', 7, 'a', 'b']
print(alfa_numerico)

print(alfa_numerico.index('a'))
print(alfa_numerico.count('a'))

# Eliminar el ultimo un valor
print(alfa_numerico)
alfa_numerico.pop(5)
print(alfa_numerico)

# Eliminar el primer valor que se encuentre
print(alfa_numerico)
alfa_numerico.remove('b')
print(alfa_numerico)

# Eliminar un rango de posiciones
print(alfa_numerico)
del alfa_numerico[2:6]
print(alfa_numerico)



# Invertir la lista
print(alfa_numerico)
alfa_numerico.reverse()
print(alfa_numerico)

# Ordenar
desordenado = [2,5,6,9,8,4,5,2]
desordenado.sort()
print(desordenado)


word = 'Hello_from_python'
print(word)

# |  H | e  | l  | l  |  o |  _ |  f |  r |  o |  m  | _  | p  | y  | t  | h  | o  | n  | 
# |  0 | 1  | 2  | 3  |  4 |  5 |  6 |  7 |  8 |  9  | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 
# |    |-16 |-15 |-14 |-13 |-12 |-11 |-10 | -9 | -8  | -7 | -6 | -5 | -4 | -3 | -2 | -1 | 

print (word[:5])
print (word[6:10])


'''
matriz

    0   1   2   3   4
0  10  12  14  16  18
1  20  22  24  26  28

24 = matriz [1]   [2]

            Fila  Columna
'''
matriz = [ 
    [10, 12, 14, 16, 18], 
    [20, 22, 24, 26, 28] 
]

print(matriz[1][2])