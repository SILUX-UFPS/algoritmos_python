#Dado un numero detecta si es perfecto (un numero perfecto es aquel que la suma de sus divisores es igual al propio numero)
def NumeroPerfecto(num):
  suma = 0
  for i in range(1,num):
    if (num % i == 0):
      suma += i
 
  if num == suma:
    return True
  else:
    return False
 
num = int(input("introduzca un numero:"))
 
if NumeroPerfecto(num):
  print("%s es un numero perfecto" % num)
else:
  print("%s NO es un numero perfecto" % num)
