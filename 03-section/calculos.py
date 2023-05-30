
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
