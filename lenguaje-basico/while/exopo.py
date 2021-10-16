base = int(input("Número base: "))
exponente = int(input("Número exponente: "))
aux = exponente

rta = 1
#base = 2
#exponente = 3
while aux > 0:
    rta = rta*base
    aux -= 1
# ciclo
#exponente = 0
#rta = 8
print(f"La potencia de la base {base} con exponente {exponente}: {rta}")
