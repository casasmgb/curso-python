class Venta:
    nueva_venta = {}
    def __init__(self, cliente, producto):
        self.cliente = cliente
        self.producto = producto

    def armar_diccionario (self):
        self.nueva_venta = {
            'id': 0,
            'codigo_cliente': self.cliente.codigo, 
            'cliente': self.cliente.nombre, 
            'producto': self.producto.nombre, 
            'precio': self.producto.precio, 
            'descuento': self.producto.descuento, 
            'iva': self.producto.iva, 
        }

        return self.nueva_venta

    def guardar_venta (self):
        self.producto.registrar_csv(self.nueva_venta)