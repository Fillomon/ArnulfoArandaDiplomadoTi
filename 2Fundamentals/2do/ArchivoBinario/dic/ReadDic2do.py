#  Alumno: Arnulfo Aranda Castro
#  Diplomado de TI -  Facultad de Telematica - Universidad de Colima
#   LECTURA DICCIONARIO
# 
import pickle

with open('diplomadoDic.bin','rb') as fh:
        odic = pickle.load(fh) 

print(type(odic))
print("Sin pprint:\n",odic)

