#El algoritmo de Euclides extendido retorna el gcd(a, b) y calcula los coeficientes enteros X y Y que satisfacen la ecuación: a*X + b*Y = gcd(a, b).

x = 0
y = 0

# O(log(max(a, b)))
def euclid( a, b):
    if b == 0:
        x = 1
        y = 0
        return a

    d = euclid(b, a % b)
    aux = x
    x = y
    y = aux - ((a/b)*y)
    return d
