#  Alumno: Arnulfo Aranda Castro
#  Diplomado de TI -  Facultad de Telematica - Universidad de Colima
#  Integracion numerica Utilizando 2 metodos (Rectangulo / Simpson)- semana 3
#
from math import sin, sqrt
 
def f(x):
    return 2*(sin(sqrt(x))-x)
a = 0
b = 1.9724
m = (a+b)/2
 
r1 = f(a)*(b-a)
print("\n")
print("Metodo por la Regla del Rectángulo: ",r1)
 
r2 = ((b-a)/6)*(f(a)+4*f(m)+f(b))
print("Metodo por la Regla de Simpson: ",r2)
print("\n")
