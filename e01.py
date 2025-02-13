class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre}, tengo {self.edad} y soy {self.profesion}.")

jose = Persona("José", 27, "camarero")
jose.presentarse()