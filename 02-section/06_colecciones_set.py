# SET define una coleccion de datos con valores unicos.

frutas = {'manzana', 'naranja', 'manzana', 'uva', 'naranja', 'sandia'}
print(frutas)

# Operaciones sobre colecciones SET

grupo_uno = set('abracadabra')
grupo_dos = set('alacazam')

print(grupo_uno)
print(grupo_dos)

# letras en grupo_uno pero no en grupo_dos
print(grupo_uno - grupo_dos)
# letras en grupo_uno o grupo_dos o en ambos
print(grupo_uno | grupo_dos)
# letras grupo_uno y en grupo_dos
print(grupo_uno & grupo_dos)
# letras en grupo_uno o en grupo_dos pero no en ambos
print(grupo_uno ^ grupo_dos)

# Llenado de datos en una sola linea
cuadrados = [x**2 for x in range(10)]
print(cuadrados)

