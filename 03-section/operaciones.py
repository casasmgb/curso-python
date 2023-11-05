import csv

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

def leer_csv(ruta):
    resultado = []
    with open(ruta, 'r') as archivo:
        datos_csv = csv.DictReader(archivo)
        # return datos_csv
        for fila in datos_csv:
            resultado.append(fila)
    return resultado

def registrar_csv(fila, ruta):
    data = leer_csv(ruta)
    id = int(data[-1]['id'])+1
    fila['id'] = id
    with open(ruta, 'a', newline='') as f:
        escritura = csv.DictWriter(f, fieldnames=fila.keys())
        escritura.writerow(fila)