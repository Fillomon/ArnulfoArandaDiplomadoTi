#  Alumno: Arnulfo Aranda Castro
#  Diplomado de TI -  Facultad de Telematica - Universidad de Colima
#  Distribución Numpy - calculando el valor medio de los valores que existen en el array
#  especificando que el calculo de realice a lo largo del eje 0.
import numpy as np
v=np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]])
print("Array: ",v)
print(v.shape)
#calculando el valor medio de los valores que existen en el array
#
cvm=np.mean(v,(0,2))
print("Valor Medio",cvm)
print(type(cvm))