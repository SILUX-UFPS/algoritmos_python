
#Ejemplo de uso de funciones con un conversor de dolar a diferentes monedas

menu="""
Bienvenido al conversor de monedas 👛💲💰
1- Peso Colombiano
2- Peso Mexicano
3- Peso Chileno
Elige una opción: """

def convertir_peso(valor_dolar):
    dolar= input("Cantidad de Dolares a convertir \n")
    dolar=float(dolar)
    pesoConvertido=dolar*valor_dolar
    pesoConvertido=round(pesoConvertido,2)
    pesoConvertido=str(pesoConvertido)
    print("Tienes "+pesoConvertido+" Pesos")


opcion=int(input(menu))
if opcion==1:
    convertir_peso(3715.01)
elif opcion==2:
    convertir_peso(21.54)
elif opcion==3:
    convertir_peso(771.60)
else:
    print("Ingresa una opcion correcta porfavor")
