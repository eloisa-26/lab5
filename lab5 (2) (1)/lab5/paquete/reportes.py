from paquete.operaciones import calcular_promedio, encontrar_maximo

def generar_resumen(lista_notas):
    promedio = calcular_promedio(lista_notas)
    maximo = encontrar_maximo(lista_notas)
    
    print(" Reporte de notas")
    print(f"Notas evaluadas: {lista_notas}")
    print(f"Promedio final: {round(promedio, 2)}")
    print(f"Nota más alta:  {maximo}")
    