"""
    Muy deficiente [0, 3)
    Deficiente [3, 3.5)
    Aceptable [3.5, 4)
    Bueno [4,4.5)
    Excelente [4.5, 5]
"""
nota = float(input("Ingrese la nota: "))

# nota => [0,5]
valida = nota >= 0 and nota <= 5
muy_deficiente = nota >= 0 and nota < 3
deficiente = nota >= 3 and nota < 3.5
aceptable = nota >= 3.5 and nota < 4
buena = nota >= 4 and nota < 4.5
excelente = nota >= 4.5 and nota <= 5

print(f"Nota valida: {valida}")
print(f"Nota muy deficiente: {muy_deficiente}")
print(f"Nota deficiente: {deficiente}")
print(f"Nota aceptable: {aceptable}")
print(f"Nota buena: {buena}")
print(f"Nota excelente: {excelente}")
