class Animal:
    def hablar(self):
        print("Sonido de anima")

class Perro(Animal):
    def hablar(self):
        print("Guau!")

class Gato(Animal):
    def hablar(self):
        print("Miau!")


for animal in Perro(), Gato():
    animal.hablar()
