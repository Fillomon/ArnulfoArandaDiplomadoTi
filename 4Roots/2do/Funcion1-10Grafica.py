#  Alumno: Arnulfo Aranda Castro
#  Diplomado de TI -  Facultad de Telematica - Universidad de Colima
#  Funcion para Graficar del 1 al 10 con incremento de 0.10
#
import matplotlib.pyplot as plt
import numpy as npy

X=npy.arange(1,10, .10)
Y=X*2

print("Cordenada X:",X)
print("Cordenada Y:",Y)

plt.plot(X,Y)
plt.show()