#Calculo del mínimo común múltiplo usando el máximo común divisor. Agregar Greatest Common Divisor.
def gcd(a, b):
    if (b == 0):
        return a
    
    return gcd(b, a % b)

def lcm( a, b):
    return a * b / gcd(a, b)

if __name__ == "__main__":
    lcm(18,8)
    