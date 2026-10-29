"""
EJERCICIO 03: Día del año.

1. Haga una función que dado un mes (en número), retorne la cantidad de días que tiene el mes (considere febrero con 28 días)
2. Haga otra función que dado un mes y el día actual del mes (ambos en número), calcule la cantidad de días que van del año
3. Pídale al usuario que ingrese el mes actual (en número). Debe validar el dato ingresado.
4. Pídale al usuario que ingrese el día actual (en número). Debe validar el dato ingresado y debe tener coherencia con el mes
   indicado en el paso anterior. Por ejemplo, abril no puede tener 31 días.
5. Calcule el día presente del año según los datos ingresados por el usuario, utilizando las funciones que acaba de implementar
6. Muestre en pantalla el resultado

"""
def Dias_mes(mes):
    if mes in [4,6,9,10]:
        return 30
    elif mes in [1,3,5,7,8,10,12]:
        return 31
    elif mes==2:
        return 28
    return 0

def calcular_dias_año(mes,dia):
    dias_total=0 
    for i in range(1,mes): 
      dias_total += Dias_mes(i)
    return dias_total + dia

mes_actual=0
dia_actual=0

mes_actual= int(input('ingrese mes actual:'))
while 1< mes_actual > Dias_mes:
    print('El mes no existe')
    mes= int(input('ingrese mes del 1 al 12:'))
dia_actual= int (input('ingrese dia actual:'))
while 1< dia_actual > mes:
   print('El dia no existe')
   dia= int (input('ingrese dia del mes:'))

resultado= calcular_dias_año(mes,dia)
print(f'los dias que han pasado son{resultado}')