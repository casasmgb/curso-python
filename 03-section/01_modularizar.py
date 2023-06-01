# from operaciones import calcular, descuento, iva
import operaciones

productos = {
    'cereal': 85,
    'carne': 268,
    'gaseosas': 125,
    'arroz': 28,
    'papel': 199,
    'maleta': 319,
    'pasta dental': 36
}

print('Descuento Total: ', operaciones.calcular(productos, operaciones.descuento))
print('IVA Total: ', operaciones.calcular(productos, operaciones.iva))
