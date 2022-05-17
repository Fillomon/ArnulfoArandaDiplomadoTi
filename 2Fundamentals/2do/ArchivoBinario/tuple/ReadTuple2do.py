#  Alumno: Arnulfo Aranda Castro
#  Diplomado de TI -  Facultad de Telematica - Universidad de Colima
#  Lectura de tuplas
import pickle
 
with open('tsemana.bin','rb') as fh:
        otuple = pickle.load(fh)
 
print(type(otuple))
 
print(otuple)