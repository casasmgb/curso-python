from producto import Producto
from cliente import Cliente
from venta import Venta

producto = Producto('pan', 100.6)
producto.mostrar()
producto.modificar_precio(25)
producto.mostrar()

# cliente = Cliente(15000, 'Aramando')
# cliente.mostrar()

cliente = Cliente()
cliente.crear(1000, 'pedro')
cliente.mostrar()

venta = Venta(cliente, producto)
diccionario_venta = venta.armar_diccionario()
venta.guardar_venta()
