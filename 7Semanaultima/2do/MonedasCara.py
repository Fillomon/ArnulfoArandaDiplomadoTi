from random import choice
#from re import M
#import random

print("\n TIO DE MONEDAS")

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