'''
Sentencias iteradora for, iterara un rango de numeros, listas u objetos agrupados.
'''

print ('\n Rango 0-4 \n')
for i in range(5):
    print(i)

print ('\n Rango 5-9 \n')
for i in range(5, 10):
    print(i)

print ('\n Rango 0-9 en intevalos de 3 \n')
for i in range(0, 10, 3):
    print(i)
    
    
 
animales = ['elefante', 'caballo', 'zorillo', 'delfin', 'medusa', 'gato']

print ('\n conjunto de animales uando IN \n')   
for animal in animales:
    print(f'{animal} \t {len(animal)}')
    
print ('\n conjunto de animales uando RANGE \n')   
for i in range(len(animales)):
    animal = animales[i]
    print(f'{i} \t {animal} \t {len(animal)}')


print ('\n conjunto cuadrados \n')   
cuadrados = [x**2 for x in range(10)]
print(cuadrados)

print ('\n conjunto de decimales de pi \n')   
from math import pi
[str(round(pi, i)) for i in range(1, 6)]