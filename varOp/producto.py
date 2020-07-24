#Leer los datos // Entradas
cantidad_inicial = float(input("Cantidad Inicial: "))
cantidad_comprada = float(input("Cantidad Comprada: "))
cantidad_vendida = float(input("Cantidad Vendida: "))
precio_compra = float(input("Precio de Compra: "))

#Realiza operaciones // Procesamiento
precio_venta = (precio_compra*0.29) + precio_compra
ingresos = precio_venta*cantidad_vendida
egresos = cantidad_comprada*precio_compra
ganancias_brutas = ingresos-egresos
impuesto = ingresos*0.19
ganancias_netas = ganancias_brutas-impuesto

#Mostrar datos // Salidas
#print(f"La cantidad inicial es: {cantidad_inicial}")
print("Las salidas son:")
print(f"Precio de Venta: {precio_venta}")
print(f"Ingresos: {ingresos}")
print(f"Egresos: {egresos}")
print(f"Ganancias Brutas: {ganancias_brutas}")
print(f"Impuestos: {impuesto}")
print(f"Ganancias Netas: {ganancias_netas}")