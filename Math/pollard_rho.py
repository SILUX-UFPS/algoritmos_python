#La función Rho de Pollard calcula un divisor no trivial de n. 
from fractions import gcd

def pollard_rho(n):
    x = 2; y = 2; d = 1
    f = lambda x: (x**2 + 1) % n
    while d == 1:
        x = f(x); y = f(f(y))
        d = gcd(abs(x-y), n)
    if d != n: return d

