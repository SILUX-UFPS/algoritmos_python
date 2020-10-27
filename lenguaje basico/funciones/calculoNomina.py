
# Funcion para el calculo de nomina,devuelve la cantidad a pagar al trabajador
# recibe como parametros sueldoBase -> Sueldo basico del empleado
# dineroVentas -> Dinero que genero el trabajador a la empresa

def totalNomina(sueldoBase, dineroVentas):
    sueldoBase = float(sueldoBase)
    comisionVentas = (float(dineroVentas))*10/100
    totalNomina = sueldoBase + comisionVentas
    print('El total de nomina a pagar es: ' + str(totalNomina))

# Menu de opciones del sistema de calculo de nomina mientras el administrador no cancele la operacion


opcion = 1
while opcion != 0:
    menu = """
Bienvenido al sistema de calculo de nomina.
0. Cancelar
1. Calcular Nomina
Elige una opción: """
    opcion = int(input(menu))

    if opcion == 1:
        """ Calcular nomina de un trabajador"""
        totalNomina(input("Ingrese el sueldo base del empleado "), input(
            "Ingrese la cantidad de dinero generado por las ventas "))
