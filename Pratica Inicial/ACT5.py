# Escribir una función que tome una lista de palabras y devuelva la más larga de ellas.

def palabra_mas_larga(lista):
    """Esta funcion devuelve la palabra mas larga de la lista"""
    largo = 0
    for palabra in lista:
        if len(palabra) > largo:
            largo = len(palabra)
            str_palabra = palabra
    return str_palabra

lista = ['hola','comos','va']
valor = palabra_mas_larga(lista)
print(valor)