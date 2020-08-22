edad = int(input("Edad: "))

if edad>0 and edad<18:
    print("Tiene: Tarjeta de identidad")
else:
    if edad>=18:
        print("Tiene: Cédula de ciudadanía.")
    else: 
        print("Datos incorrectos.")
    