#495204495216
numero = int(input("Número: "))

horas2 = int(numero%100)
#4952044952
minutos2 = int( (numero/100)%100 )
#49520449
segundos2 = int( (numero/10000)%100 )

#495204 495216
numero_aux = int((numero/1000000))
hora1 = int(numero_aux%100)
minutos1 = int((numero_aux/100)%100)
segundos1 = int((numero_aux/10000)%100)

diferencia = horas2 - hora1

cant_dias = diferencia/24

#print(f"Numero1: {numero_aux}")
print(f"Hora1: {hora1}, Minutos1: {minutos1}, Segundos1: {segundos1}")
print(f"Hora2: {horas2}, Minutos2: {minutos2}, Segundos2: {segundos2}")
print(f"El tiempo trasncurrido en días es: {cant_dias}")