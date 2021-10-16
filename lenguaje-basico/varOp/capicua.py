numero = int(input("Ingrese el numero: "))

# 1234
primer = numero % 10
# 1234/10 = 123%10 = 3
segundo = int((numero/10) % 10)
# 1234/100 = 12%10 = 2
tercer = int((numero/100) % 10)
# 1234/1000 = 1%10 = 1
cuarto = int((numero/1000) % 10)

# 1234 -> 4321
primer_nuevo = primer*1000
segundo_nuevo = primer_nuevo+(segundo*100)
tercer_nuevo = segundo_nuevo+(tercer*10)
cuarto_nuevo = tercer_nuevo+cuarto

invertido = cuarto_nuevo

es_capicua = invertido == numero

print(f"Es capicua: {es_capicua}")

"""print(f"El numero es: {primer_nuevo}")
print(f"El numero es: {segundo_nuevo}")
print(f"El numero es: {tercer_nuevo}")
print(f"El numero es: {cuarto_nuevo}")"""
"""print(f"El primer digito del numero es: {primer}")
print(f"El segundo digito del numero es: {segundo}")
print(f"El tercer digito del numero es: {tercer}")
print(f"El tercer digito del numero es: {cuarto}")"""
