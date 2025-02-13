class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre}, tengo {self.edad} y soy {self.profesion}.")

class Estudiante(Persona):
    def __init__(self, nombre, edad, profesion, curso):
         super().__init__(nombre, edad, profesion)
         self.curso = curso
    
    def presentarse(self):
        print(f"Hola, me llamo {self.nombre}, tengo {self.edad} y estudio {self.curso}.")

jose = Persona("José", 27, "camarero")
jose.presentarse()
lucia = Estudiante("Lucía", 22, "estudiante", "arqueología")
lucia.presentarse()