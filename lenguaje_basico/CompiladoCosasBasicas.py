print("Ejemplo pedir por consola y comparar 2 numeros")
print("Introduzca 2 numeros")
n = int(input("n: ")) #Ejemplo pedir por consola
m = int(input("m: "))

if n==m: #PONER LOS ":" DE LO CONTRARIO NO FUNCIONA
	print("oli son iguales") #Ejemplo imprimir 
else:
	print("No son iguales")
	
print()
	
n=10

print("Ejemplo while")
while n>0:
	if (n%2) == 0:
		print("el " , n , "es par sapo") #Concatena con la "," 
	else:	
		print("el " , n , "es impar sapo") 
	n-=1 #El -- y ++ no son validos
	
	
print()

print("Ejemplo recorrer lista con while")

m = [1,2,3,4,5] #Ejemplo lista
n=0
while n< len(m): #Ejemplo .length en python
	print(m[n])
	n+=1
	
	
print()

print("Ejemplo recorrer lista con for")

m= list(range(2,20,3))#Con el range se obtiene un rango de numeros. con un solo
										 #valor hasta ese numero -1, 2 valores en ese intervalo y 
											#el tercer valor para decir de cuanto en cuanto
#m = [1,2,3,4,5]
for it in m:
	print(it)
 
print()
 
print("Ejemplo funcion")
def saludar():
	print("Ola pa k vea k sirve")
 
saludar()
print()

print("TUPLAS")
#TUPLAS
tupla = (100, "ola", [1,2,3], -50, "ola" )
print(tupla.index("ola")) #Obtener el index de un elemento
print(tupla.count("ola")) #Contar cuantas veces aparece el elemento
tuplaALista = list(tupla) #Pasar una tupla a lista
print()

print("Conjuntos")
conjunto = set()
conjunto = {1,2,3}
conjunto.add(5) #Son desordenadas ya que se almacena desordenadamente, se pueden 
conjunto.add("h") #varios tipos de valores tmb, no premite repetidos
conjunto
conjunto2 = {2,3,4}
print("Interseccion")
print(conjunto.intersection(conjunto2))
print("Union")
print(conjunto.union(conjunto2))
print("Interseccion")
print(conjunto.difference(conjunto2))
print()

print("Diccionarios") #es equivalente a json basicamente 
colores = {"amarillo":"yelou", "azul":"blu", "rojo":"red"} #Se define clave:valor
colores.items() #Ver items
del(colores["amarillo"])
colores.items()
print()

print("pilas")
pila=[3,4,5]
pila.append(6) #agregar
print(pila)
pila.pop() #eliminar
print(pila)
print()

print("colas")
from collections import deque
cola=deque(["manuel","maria"])
print(cola)
cola.append("pedro") #Agregar
print(cola)
cola.pop()#Eliminar ultimo
print(cola)
cola.popleft()#Eliminar primero
print(cola)
