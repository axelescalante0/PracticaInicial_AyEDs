#Escribir una función que permita calcular las raíces de una ecuación cuadrática.
import math
def raices(a,b,c):
    """Esta funcion encuentra las raices de una funcion cuadratica"""
    discriminante = b**2 - 4*a*c
    raiz1 = (-b + math.sqrt(discriminante)) // (2*a)
    raiz2 = (-b - math.sqrt(discriminante)) // (2*a)
    return raiz1, raiz2

a = 2
b = 0
c = -2

raiz = raices(a,b,c)
print(raiz)