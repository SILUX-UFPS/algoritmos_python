#Calcula el máximo común divisor entre a y b mediante el algoritmo de Euclides

def gcd(a, b):
    if (b == 0):
        return a
    
    return gcd(b, a % b)

if __name__ == "__main__":
    gcd(18,8)
    