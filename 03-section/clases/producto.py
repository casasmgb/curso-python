import csv

class Producto:
    nombre = ''
    precio = 0
    descuento = 0
    iva = 0
    ruta = '/media/gcasas/1b6e2e25-7c0f-4fe1-ae7e-caa069016f8f/gcasas/Documents/gabo_projects/class_material/python/03-section/ventas.csv'

    def __init__ (self,nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.descuento = self.calcular_descuento()
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

    def leer_csv(self):
        resultado = []
        with open(self.ruta, 'r') as archivo:
            datos_csv = csv.DictReader(archivo)
            for fila in datos_csv:
                resultado.append(fila)
        return resultado

    def registrar_csv(self, fila):
        data = self.leer_csv()
        id = int(data[-1]['id'])+1
        fila['id'] = id
        with open(self.ruta, 'a', newline='') as f:
            escritura = csv.DictWriter(f, fieldnames=fila.keys())
            escritura.writerow(fila)