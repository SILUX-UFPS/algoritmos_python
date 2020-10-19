def es_feliz(num):
    r = num
    suma_cuadrados = []
    while True:
        if r == 1:
            return True

        r = sum(int(x) ** 2 for x in str(r))
        if r in suma_cuadrados:
            return False

        suma_cuadrados.append(r)

for i in range(15):
    if es_feliz(i):
        print(f"{i} es feliz!")
    else:
        print(f"{i} no es feliz!")
