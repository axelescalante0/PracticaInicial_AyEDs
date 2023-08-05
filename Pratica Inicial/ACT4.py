# Escribir dos funciones que realicen operaciones matemáticas básicas: 
# una debe realizar la suma de todos los elementos de una lista y la otra multiplicarlos.
# Por ejemplo: para la lista [1,2,3,4] la primera función debería devolver 10 y la segunda debería devolver 24.

def suma(lista):
    """Esta funcion realiza la suma de la lista ingresada"""
    resultado = sum(lista)
    return resultado

def multiplicacion(lista):
    """Esta funcion realiza la multiplicacion de la lista ingresada"""
    numero = 1
    for num in lista:
        numero *= num
    return numero

lista = [1,2,3,4]
sumar = suma(lista)
print('La suma de la lista es',sumar)

multiplicar = multiplicacion(lista)
print('La multiplicacion de la lista es',multiplicar)