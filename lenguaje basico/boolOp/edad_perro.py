edad_humano = int(input("Edad del humano: "))

# 1=> 5 perro
# 2=> 10.5 perro
# 3=> 4.5 perro
edad_perro = 0
if edad_humano >= 0:
    if edad_humano == 1:
        edad_perro = 5

    if edad_humano == 2:
        edad_perro = 10.5

    if edad_humano > 2:
        edad_perro = ((edad_humano-2)*4.5)+10.5

    print(f"La edad del perro es: {edad_perro}.")
else:
    print("Los datos no son validos.")
