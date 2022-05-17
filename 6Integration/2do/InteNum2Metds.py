#  Alumno: Arnulfo Aranda Castro
#  Diplomado de TI -  Facultad de Telematica - Universidad de Colima
#  Integracion numerica Utilizando 2 metodos (Punto Medio / Simpson)- semana 3
#
from math import sin, sqrt

def f(x):
    return (7**-x)+3

a = -1
b = 2
m = (a+b)/2

r1 = f(m)*(b-a)
print("\n")
print("Resultado por el Punto medio: ",r1)

r1 = ((b-a)/6)*(f(a)+4*f(m)+f(b))
print("Resultado por la regla de Simpson: ",r1)
print("\n")
