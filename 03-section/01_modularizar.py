# from calculos import calcular, descuento, iva
import calculos

productos = {
    'cereal': 85,
    'carne': 268,
    'gaseosas': 125,
    'arroz': 28,
    'papel': 199,
    'maleta': 319,
    'pasta dental': 36
}

print('Descuento Total: ', calculos.calcular(productos, calculos.descuento))
print('IVA Total: ', calculos.calcular(productos, calculos.iva))
