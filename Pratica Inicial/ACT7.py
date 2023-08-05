#  Escribir una función que pida dos palabras y determine si las mismas riman o no. Considere que las dos palabras riman si coinciden en sus tres últimas letras.



def rima(p1, p2):
    """Esta funcion determina si dos palabras riman."""
    if p1[-3:] == p2[-3:]:
        return True
    else:
        return False

p1 = 'di maria'
p2 = 'que diria'

h = rima(p1,p2)
print(h)