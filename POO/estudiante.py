from persona import Persona
class Estudiante(Persona):

    def __init__(self,nombre, apellido, edad,codigo,promedio):
        super().__init__(nombre,apellido,edad)
        self.codigo = codigo
        self.promedio = promedio

    def estudiante_condicional(self):
        if self.promedio < 3.1:
            return "Es condicional"
        else:
            return "No es condicional"

e1 = Estudiante("Jimmy","Page","20","1151621",3.6)

print(e1.retornar_nombre())
print(e1.estudiante_condicional())