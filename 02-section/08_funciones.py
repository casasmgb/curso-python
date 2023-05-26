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