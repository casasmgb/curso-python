'''
Dado un numero verificar si este es:
negativo
cero
si es positivo 
si entre 10 y 20
si es mayor a 20
'''
numero = int(input('mumero: '))
if (numero > 0):
    print('numero es positivo')
    if (numero >= 10 and numero <=20):
        print('el numero esta entre 10 y 20')
    elif (numero >20):
        print('el numero es mayor a 20')
    else:
        print('el numero esta entre 1 y 9') 
elif (numero == 0):
    print('el numero es 0')
else:
    print('es negativo')	
