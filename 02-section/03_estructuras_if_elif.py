'''
Sentencias Condicionales encadenadas, verifican la veracidad de condiciones en cadena
'''

numero = input('Introdusca un numero entero: ')
numero = int(numero)

if numero < 0:
    print (f'El numero {numero} es negativo')
elif numero == 0: 
    print (f'El numero {numero} es cero')
elif numero > 0 and numero < 10:
    print (f'El numero {numero} es positivo y menor a 10')
elif numero in range(10,21):
    print (f'El numero {numero} esta entre 10 y 20')
else:
    print (f'El numero {numero} es mayor a 20')
    