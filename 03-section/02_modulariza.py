# from calculos import calcular, descuento, iva
import calculos
import math

productos = { }
lectura = True

while lectura:
    nombre = input('Producto: ')
    if (nombre != 'terminar'): 
        precio = float(input('Precio: '))
        productos[nombre] = precio
    else:
        lectura = False
    

print('\n\nCalculando valores... \n\n')

total_descuento = calculos.calcular(productos, calculos.descuento)
total_iva = calculos.calcular(productos, calculos.iva)

total_descuento = round(total_descuento, 2)
total_iva = round(total_iva, 2)

print('Descuento Total: ', total_descuento)
print('IVA Total: ', total_iva)
