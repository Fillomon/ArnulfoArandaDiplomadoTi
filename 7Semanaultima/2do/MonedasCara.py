#  Alumno: Arnulfo Aranda Castro
#  Diplomado de TI -  Facultad de Telematica - Universidad de Colima
#  Funcion para juego de Sellos o Aguilas
#
from random import choice
print("\n TIRO DE MONEDAS")
def caras():
    return choice(['Aguila', 'Sello'])

def tiro(times):
    values = {}
    for iteration in range(times):
        m = caras()
        values[m] = values.get(m, 0) + 1
    return values

print("\n")
print(tiro(10))
print(tiro(20))