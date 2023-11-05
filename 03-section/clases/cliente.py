class Cliente:
    codigo = 0
    nombre = ''

    # def __init__ (self, codigo, nombre):
    #     self.codigo = codigo
    #     self.nombre = nombre

    def mostrar (self):
        print('Datos Cliente'.center(40, '='))
        print(f'Codigo Cliente:\t\t{self.codigo}')
        print(f'Nombre Cliente:\t\t{self.nombre}')

    def crear(self, codigo, nombre):
        self.nombre = nombre
        self.codigo = codigo

    def modificar_nombre(self, nombre):
        self.nombre = nombre

    