diccionarios = {
    "nombre": "chanchito feliz",
    "raza": "gato persa",
    "edad": 5
}

print (diccionarios)


#para eliminar

diccionarios.pop("nombre")
del diccionarios['raza']


#para copiar

diccionario=dict(diccionarios)

#profundizacion de diccionarios

gatitos = {
    "Flufly": {
        "nombre": "Flufly",
        "edad": 5
    },
    "Manba":{
        "nombre": "Black manba",
        "edad": 20
    }
}

chico={
    "nombre": "victor",
    "edad": 2
}
alto={
    "nombre": "ben",
    "edad": 5
}

perros ={
    "chico":chico,
    "alto":alto
}

print (perros)

conejos = dict(nombre="Pin", edad=3)
