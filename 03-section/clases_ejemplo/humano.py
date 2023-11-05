class Humano():                         # Creamos la clase Humano
    def __init__(self, edad, nombre, ojos, estatura, genero, ocupacion):   # Definimos el atributo por defecto
        self.edad = edad 
        self.nombre = nombre 
        self.ojos = ojos
        self.estatura = estatura
        self.genero = genero
        self.ocupacion = ocupacion



    def hablar (self):
        print (f'Hola soy {self.nombre}.') 
        print (f'\t\tmi edad es {self.edad} y mi ocupación es {self.ocupacion}.\n')

    def correr (self):
        print (f'Ahora {self.nombre} empieza a correr.\n') 

    def renombrar (self, nombre):
        self.nombre = nombre 
        print (f'Nombe modificado a {nombre}') 

    def contratar (self, puesto):
        self.ocupacion = puesto 
        print (f'Felicidades {self.nombre} estas ocupando un nuevo puesto como: {self.ocupacion}.\n') 