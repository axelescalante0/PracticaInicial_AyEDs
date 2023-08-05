#Escribir una función que reciba una cadena de caracteres y determine la cantidad de vocales que posee

def contador_vocal(cadena):
    """Esta funcion cuanta la cantidad de vocales que hay 
        en una cadena."""
    contador = 0
    for letra in cadena:
        if letra in 'aeiou':
            contador += 1
    return contador

cadena = 'abcdefghii'
vocales = contador_vocal(cadena)
print('El numero de vocales es de: ',vocales)