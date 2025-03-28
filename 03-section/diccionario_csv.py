import csv

ruta = './ventas.csv'

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
        
        
datos_csv = leer_csv(ruta)

un_producto = datos_csv[0]
print(un_producto)

for clave, valor in un_producto.items():
    print(f'CLAVE: {clave} \t\tVALOR: \t{valor}')
    
for venta in datos_csv:
    print('==============================================')
    for clave, valor in venta.items():
        print(f'CLAVE: {clave} \t\tVALOR: \t{valor}')


nueva_venta = {
    'id': 0,
    'codigo_cliente': 100007, 
    'cliente': 'Saturnina del León', 
    'producto': 'crema', 
    'precio': 116.5, 
    'descuento': '', 
    'iva': ''
}

registrar_csv(nueva_venta, ruta)

# lectura = True

# while lectura:
#     nombre = input('Producto: ')
#     nuevo_producto = { 'id': 0 }
#     if (nombre != 'terminar'): 
#         codigo_cliente = input('Codigo Cliente: ')
#         cliente = input('Nombre Cliente: ')
#         producto = input('Codigo Cliente: ')
#         precio = float(input('Precio: '))
        
#         nuevo_producto['codigo_cliente'] = codigo_cliente
#         nuevo_producto['cliente'] = cliente
#         nuevo_producto['producto'] = nombre
#         nuevo_producto['precio'] = precio
#         nuevo_producto['descuento'] = 0
#         nuevo_producto['iva'] = 0

#         registrar_csv(nuevo_producto, ruta)
#     else:
#         lectura = False
    

