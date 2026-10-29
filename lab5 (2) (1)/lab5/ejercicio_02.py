"""
EJERCICIO 02: Validación de contraseña segura

Implementa una función que reciba una contraseña y verifique: 
    1. Que tenga al menos 8 caracteres de longitud.
    2. Que contenga al menos un número (puedes usar un bucle o una verificación con dígitos).
    3. Que contenga al menos una letra mayúscula.

La función debe retornar True si cumple todas las condiciones, y False en caso contrario. 
(Ayuda: puedes crear funciones auxiliares pequeñas para cada validación, fomentando la modularidad de tu programa).

Ejemplos de casos de prueba:
    - es_contrasena_segura("Python123") -> True
    - es_contrasena_segura("clave") -> False
    - es_contrasena_segura("12345678") -> False
"""
def contraseña_segura(contraseña):
    contador= 0  
    for i in contraseña: 
        contador=contador + 1
    longitud= contador 
    if longitud<8:
        return False 
   
    Es_mayuscula= False 
    Es_numero= False
    for i in contraseña:
        if i.isupper():
            Es_mayuscula= True
        if i.isdigit():
            Es_numero= True 
    if  Es_mayuscula and Es_numero:
        return True 
    else:
        return False

print(contraseña_segura("Python123"))