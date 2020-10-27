def multiplicacion(a, b):
    multiplicar = a*b
    return f"El resultado de la multiplicación es: {multiplicar}"


def dividir(a, b):
    division = a/b
    return f"El resultado de la división es: {division}"


def sumar(a, b):
    suma = a+b
    return f"El resultado de la suma es: {suma}"


def resta(a, b):
    resta = a-b
    return f"El resultado de la resta es: {resta}"


if __name__ == "__main__":
    cumple = True
    while cumple:
        numero_a = int(input("Ingrese el primer número: "))
        numero_b = int(input("Ingrese el segundo número: "))

        lista = [multiplicacion(numero_a, numero_b), dividir(
            numero_a, numero_b), sumar(numero_a, numero_b), resta(numero_a, numero_b)]

        pregunta = int(input(
            "0. Multiplicación.\n1. División.\n2. Sumar.\n3. Restar.\n¿Qué operación desea realizar?: "))

        print(lista[pregunta])

        continuar = input("¿Quiere realizar otra operación? s/n: ")

        if continuar == "n":
            cumple = False
