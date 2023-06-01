from producto import Producto
from cliente import Cliente

producto = Producto('pan', 100.6)
producto.mostrar()
producto.modificar_precio(25)
producto.mostrar()

# cliente = Cliente(15000, 'Aramando')
# cliente.mostrar()

cliente2 = Cliente()
cliente2.crear(1000, 'pedro')
cliente2.mostrar()