nombre = input('Ingrese es su nombre:\t ')
edad = input('Ingrese es su edad:\t ')
hobbie = input('Ingrese es su hobbie:\t ')

print ('SALIDA\n\n')

print (f'Hola {nombre}!')
print (f'Tu edad es: {edad}.')
print (f'Y tu pasatiempo es: {hobbie}.')


print(f"""
    Hola {nombre}
    Tu edad es: {edad}

    Tambien acabas de indicarme que tu pasatiempo es {hobbie}.
""")

nombre_centrado = nombre.center(15, '*')
print(nombre_centrado)