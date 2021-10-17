
class Persona:

    def __init__(self,nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def retornar_nombre(self):
        return self.nombre + " " + self.apellido
    
    def cumplir_anios(self):
        self.edad = self.edad + 1
    
p1 =  Persona("Michael","Scott",40)
print(p1.retornar_nombre())
p1.cumplir_anios()
print(p1.edad)