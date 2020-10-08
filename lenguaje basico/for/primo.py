numero = int(input("Ingrese un número: "))

mitad = int(numero/2)
respuesta = "Es un número primo."
rango = range(2,mitad)
#10/2=5
#10/5 = 2
#10%5 = 0
if numero%mitad==0 and mitad!=1:
    respuesta = "No es un número primo."
else:
    for aux in rango:
        if numero%aux==0:
            respuesta = "No es un número primo."

print(respuesta)