class Producto:
    nombre = ''
    precio = 0
    descuento = 0
    iva = 0

    def __init__ (self,nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.precio = self.calcular_descuento()
        self.iva = self.calcular_iva()

    def calcular_descuento(self):
        desc = 0
        if self.precio > 100:
            desc = self.precio * 0.15
        else:
            desc = self.precio * 0.05
        return round(desc, 2)

    def calcular_iva(self):
        return round((self.precio * 0.13), 2)

    def modificar_precio (self, precio):
        self.precio = precio
        self.precio = self.calcular_descuento()
        self.iva = self.calcular_iva()

    def mostrar (self):
        print('Datos del Producto'.center(50, '='))
        print(f'Producto:\t\t{self.nombre}')
        print(f'Precio  :\t\t{self.precio}')
        print(f'Descuento:\t\t{self.descuento}')
        print(f'Impuesto:\t\t{self.iva}')