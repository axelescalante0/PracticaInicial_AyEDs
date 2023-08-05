#Definir una función que calcule la longitud de una lista o una cadena dada.

def longitud_cadena(lista):
    """Esta funcion determina la longitud de una lista o cadena"""
    longitud = len(lista)
    return longitud

cadena = [1,26,4,3,5,7,8]

long_cadena = longitud_cadena(cadena)
print('Su longitud es de: ',long_cadena)