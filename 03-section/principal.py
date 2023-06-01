# from calculos import calcular, descuento, iva
import operaciones

ruta = '/media/gcasas/1b6e2e25-7c0f-4fe1-ae7e-caa069016f8f/gcasas/Documents/gabo_projects/class_material/python/03-section/ventas.csv'

# datos = operaciones.leer_csv(ruta)
# for fila in datos:
#     print(fila)


nueva_venta = {
    'id': 0,
    'codigo_cliente': 100007, 
    'cliente': 'Saturnina del León', 
    'producto': 'crema', 
    'precio': 116.5, 
    'descuento': '', 
    'iva': ''
}

operaciones.registrar_csv(nueva_venta, ruta)



lectura = True

while lectura:
    nombre = input('Producto: ')
    nuevo_producto = { 'id': 0 }
    if (nombre != 'terminar'): 
        codigo_cliente = input('Codigo Cliente: ')
        cliente = input('Nombre Cliente: ')
        producto = input('Codigo Cliente: ')
        precio = float(input('Precio: '))
        
        nuevo_producto['codigo_cliente'] = codigo_cliente
        nuevo_producto['cliente'] = cliente
        nuevo_producto['producto'] = nombre
        nuevo_producto['precio'] = precio
        nuevo_producto['descuento'] = operaciones.descuento(precio)
        nuevo_producto['iva'] = operaciones.iva(precio)

        operaciones.registrar_csv(nuevo_producto, ruta)
    else:
        lectura = False
    





# total_descuento = operaciones.calcular(nuevo_producto, operaciones.descuento)
# total_iva = operaciones.calcular(nuevo_producto, operaciones.iva)

# total_descuento = round(total_descuento, 2)
# total_iva = round(total_iva, 2)

# print('Descuento Total: ', total_descuento)
# print('IVA Total: ', total_iva)
