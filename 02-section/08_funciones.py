''' 
    Definicion de funciones

    def          name         (n):    
     
  definicion    nombre     parametros

Las funciones pueden o no devolver un valor

'''

def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


limite = int(input('Introdusca el limite de la serie: '))
fibonacci(limite)


'''
    Las funciones que devuelven valores usan la palabra         return
'''


def fibonacci2(n):
    resultado = []
    a, b = 0, 1
    while a < n:
        resultado.append(a)
        a, b = b, a+b
    return resultado

limite = int(input('Introdusca el limite de la serie: '))
resultado_fibonacci = fibonacci2(limite)

print(resultado_fibonacci)


'''
Valores por defecto
'''

def fibonacci2(n=15):
    resultado = []
    a, b = 0, 1
    while a < n:
        resultado.append(a)
        a, b = b, a+b
    return resultado

resultado_fibonacci = fibonacci2()

print(resultado_fibonacci)


'''
Mandando funciones como argumentos
'''

def porcentaje(numero, porcentaje):
    return numero * porcentaje / 100

def aplicar_porcentaje(lista, funcion):
    lista_porcentajes = []
    for numero, porcentaje in lista.items():
        resultado_porcentaje = funcion(numero, porcentaje)
        lista_porcentajes.append(resultado_porcentaje)
    return lista_porcentajes


valores = { 
    100: 15, 
    250: 25,
    368: 22
}

print('Falculo de porcentajes: ', aplicar_porcentaje(valores, porcentaje))


'''
funciones lamda
'''

sumar = lambda a,b : a + b
impar = lambda n : n % 2 == 0 

print (sumar(5, 8))
print (impar(5))



'''
Ejercicio: dada una lista de productos y precios calcular el descuento Total y el IVA Total aplicable.

Descuento: precios Mayores a 100 descuento del 15%
Descuento: precios Menores o Iguales a 100 descuento del 5%

Tasa Iva aplicable: 13%

Ej.

{
    'cereal': 85,
    'carne': 268,
    'gaseosas': 125,
    'arroz': 28,
    'papel': 189,
    'maleta': 369,
    'pasta dental': 36
}
'''



def descuento(precio):
    desc = 0
    if precio > 100:
        desc = precio * 0.15
    else:
        desc = precio * 0.05
    return desc

def iva(precio):
    return precio * 0.13


def calcular(lista, funcion):
    total = 0
    for producto, pricio in lista.items():
        total += funcion(pricio)
    return total


productos = {
    'cereal': 85,
    'carne': 268,
    'gaseosas': 125,
    'arroz': 28,
    'papel': 199,
    'maleta': 319,
    'pasta dental': 36
}

print('Descuento Total: ', calcular(productos, descuento))
print('IVA Total: ', calcular(productos, iva))
