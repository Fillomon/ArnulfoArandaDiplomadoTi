#  Alumno: Arnulfo Aranda Castro
#  Diplomado de TI -  Facultad de Telematica - Universidad de Colima
#  ESCRITURA DE DICCIONARIO
# 
import pickle

d={'123456':'TRABAJADOR 1', '654321':'TRABAJADOR 2', '987654':'TRABAJADOR 3'}

with open('diplomadoDic.bin','wb') as fh:
        pickle.dump(d,fh)

print('\n LISTO...\n')