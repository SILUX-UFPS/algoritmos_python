
# Lista
"""
print("-----Lista:-----")
lista = ["amarillo", "azul", "rojo", "verde", "morado", "naranja"]
print("\nImpresion de lista:")
print("La lista es: {}".format(lista))
print("\nImpresion de lista con for:")
for x in lista:
    print(x)

#[x:n)
print(lista[1:5])

#[0:n)
print(lista[:5])

if "naranja" in lista:
    print("El color está en la lista.")
else:
    print("El color no está en la lista.")

lista.append("negro")
print("La lista es: {}".format(lista))
"""

print("-----Diccionarios:-----")
# Diccionarios
diccionario = {
    "nombre": "Chus",
    "correo": "chus@gmail.com",
    "edad": 17
}

"""
print("El diccionario es: {}".format(diccionario))
print("El valor de la clave {} es: {}".format("nombre",diccionario["nombre"]))
for x in diccionario:
    print("La clave es: {}".format(x))
for x in diccionario.values():
    print("El valor es: {}".format(x))

for x in diccionario:
    print("La clave es: {} y el valor es: {}".format(x, diccionario[x]))

if "correo" in diccionario:
    print("La clave está.")
else:
    print("La clave no está.")
    
diccionario["edad"] = 21
print("El diccionario es: {}".format(diccionario))
"""
