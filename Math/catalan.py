# Guarda en el array Catalan Numbers los numeros de Catalan hasta MAX.

MAX = 30

catalan = [0 for i in range(MAX+1)]


def catalanNumbers():
    catalan[0] = 1
    for i in range(1, MAX+1):
        catalan[i] = catalan[i-1]*((float)(2*((2 * i) - 1))/(i + 1))


if __name__ == "__main__":
    catalanNumbers()
    print(catalan)
