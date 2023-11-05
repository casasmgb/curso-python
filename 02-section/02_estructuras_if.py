'''
Sentencias Condicionales simples, verifican la veracidad de una condicion
'''

numero = input('Introdusca un numero entero: ')
numero = int(numero)

if numero % 2 == 0:
    print (f'El numero {numero} es par')
else: 
    print (f'El numero {numero} es impar')
    