# Definir una función que tome como argumento una lista y devuelva el mayor de sus elementos.

def mayor_lista(lista):
    """Esta funcion determina el elmenento mayor de una lista,
       se lista un parametro de la funcion."""
    mayor = max(lista)
   
    return mayor

lista = [1,6,76,34,36]
mayor_list = mayor_lista(lista)
print('El numero mayor de la lista es: ',mayor_list)
