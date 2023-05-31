# from calculos import calcular, descuento, iva
import principal

productos = {
    'cereal': 85,
    'carne': 268,
    'gaseosas': 125,
    'arroz': 28,
    'papel': 199,
    'maleta': 319,
    'pasta dental': 36
}

print('Descuento Total: ', principal.calcular(productos, principal.descuento))
print('IVA Total: ', principal.calcular(productos, principal.iva))
