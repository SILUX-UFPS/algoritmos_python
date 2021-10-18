def prime_factors(n):
    num = n
    index = 0
    t = [2, 3, 5, 7]
    f = []
    while t[index] ** 2 <= n:
        if len(t) == (index + 1):
            t.append(t[-2] + 6)
        if n % t[index]:
            index += 1
        else:
            n = n // t[index]
            f.append(t[index]
    if n > 1:
        f.append(n)
    return num, f
