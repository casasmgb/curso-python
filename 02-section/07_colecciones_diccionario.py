# Diccionarios Tipo de dato para almacenar datos en forma de clave: valor

telefonos = { 
    'liz': 65656565,
    'ariana': 63636363,
    'erick': 78787878,
    'carlo': 75757575,
}

print (telefonos)
print(sorted(telefonos))

print('guido' in telefonos)
print('marcos' not in telefonos)


# Creacion de diccionarios con iterador for

cuadrados = {x: x**2 for x in (2, 4, 6)}
print (cuadrados)

nombres = ('uno', 'dos', 'tres')
cuadrados = {nombres[i]: (i+1)**2 for i in range(len(nombres)) }
print (cuadrados)

''' 
Iterando diccionarios

    'liz':   65656565

    CALVE    VALOR
'''

telefonos = { 
    'liz': 65656565,
    'ariana': 63636363,
    'erick': 78787878,
    'carlo': 75757575,
}

for k, v in telefonos.items():
    print(f'CLAVE: \t{k} \tVALOR: \t{v}')

