'''
Sentencias iteradora while, iterara y se detiene cuando se cumpla una condicion.
'''

print ('\n Itera hasta que el numero llegue a 10 \n')
limite = 10
numero = 1

while numero <= limite:
    print (numero) 
    numero += 1



animales = ['elefante', 'caballo', 'zorillo', 'delfin', 'medusa', 'gato']

print ('\n itera el conjunto de animales \n')   

i = 0
while i < len(animales):
    animal = animales[i]
    print(f'{i} \t {animal} \t {len(animal)}')
    i += 1
    
print ('\n Serie Fibonacci \n')   
'''
    0 1 1 2 3 5 8 13 21
'''

limite = int(input('Introdusca el limite de la serie: '))

a, b = 0, 1

while a < limite:
    print(a)
    a, b = b, a+b