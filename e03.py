class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre}, tengo {self.edad} y soy {self.profesion}.")
class Trabajador(Persona):
    def __init__(self, nombre, edad, profesion, trabajo):
        super().__init__(nombre, edad, profesion)
        self.trabajo = trabajo

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre}, tengo {self.edad}, soy {self.profesion} y trabajo en {self.trabajo}.")

jose = Persona("José", 27, "camarero")
jose.presentarse()
lucia = Trabajador("Lucía", 22, "obrera", "Contrucciones Jacobo S.L.")
lucia.presentarse()