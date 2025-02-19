import math

class Rectangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def Calcular_area(self):
        return(f"El area de un rectangulo de base {self.base} y altura {self.altura} es igual a {self.base * self.altura}")
class Circulo():
    def __init__(self, radio):
        self.radio = radio

    def Calcular_area(self):
        return(f"El area de un cirulo con radio {self.radio} es igual a {math.pi * self.radio ** 2}")
c = Circulo(5)
r = Rectangulo(4, 6)
print(c.Calcular_area())
print(r.Calcular_area())