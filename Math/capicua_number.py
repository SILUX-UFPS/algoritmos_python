def invertir_numero(n):
    numero = 0
    while n != 0:
        numero = 10*numero+n % 10
        n //= 10
    return numero


def capicua(numero):
    return numero == invertir_numero(numero)


# Probar
numeros = [11, 20, 123, 9889, 2811, 1801, 777, 12321, ]

for numero in numeros:
    es_capicua = capicua(numero)
    print(f"El número {numero} es capicúa? {es_capicua}")
