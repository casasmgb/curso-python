from humano import Humano

print('Instancia Uno'.center(50, '='))
mujer = Humano(nombre='Elisa', ocupacion='Estudiante', edad=25, ojos='cafes', estatura='1.68', genero='Femenino')
mujer.hablar()
mujer.correr()
mujer.contratar('Gerente')
mujer.hablar()

print('Instancia Dos'.center(50, '='))

hombre = Humano(nombre='Marcos', ocupacion='Artesano', edad=45, ojos='cafes', estatura='1.75', genero='Masculino')
hombre.hablar()
hombre.contratar('Empresario')
hombre.hablar()