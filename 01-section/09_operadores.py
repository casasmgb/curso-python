'''
Operadores 
%  Modulo (resto) 
** Exponente
// Division (parte entera)
'''
print(17 % 3)
print(3**2)
print(24//9)

'''
Asignacion
=    Asignacion de valor
+=   El primer elemento es igual a la suma del primer elemento con el segundo
-=   El primer elemento es igual a la resta del primer elemento con el segundo
*=   El primer elemento es igual a la multiplicación del primer elemento con el segundo
/=   El primer elemento es igual a la división del primer elemento con el segundo.
%=   El primer elemento es igual a el Módulo: resto de la división del primer elemento con el segundo.
**=  El primer elemento es igual a el resultado de la exponente del primer elemento con el segundo
'''
a = 5
b = 8
resultado = a + b
print(resultado)

a = 5
a += 8
print(a)

'''
    TRUE        FALSE
    SI          NO
    VERDADERO   FALSE
'''
'''
Comparacion
==  Exactamente iguales
!=  Difetente
>   Mayor que
<   Menor que
>=  Mayor o igual que
>=  Menor o igual que
'''
print( 5 == 5 )
print( 5 != 5 )
print( 5 > 8 )
print( 5 < 8 )
print( 3 <= 10)
print( 3 >= 10)


'''
    TRUE        FALSE
    SI          NO
    VERDADERO   FALSE
'''

verdad = True
falso = False

'''
Logicos
and     operador "y"
or      operador "o"
not     operador "negado"
'''
print('OPERADORES LOGICOS......')
print (True and False)
print (False and False)
print (True and True)
print (False and False)
print(not False)
print(not True)
print(not (5 == 5))

'''
Especiales
in   	 El operador In (en) devuelve True si un elemento se encuentra dentro de otro.
not in   El operador Not In (en) devuelve True si un elemento no se encuentra dentro de otro.
'''

lista = [1, 2, 3, 4]

print( 8 in lista)
print( 3 in lista)
print( 18 not in lista)
