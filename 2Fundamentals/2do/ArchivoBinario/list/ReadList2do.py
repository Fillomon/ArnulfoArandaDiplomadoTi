#  Alumno: Arnulfo Aranda Castro
#  Diplomado de TI -  Facultad de Telematica - Universidad de Colima
#   LECTURA DE LISTA
# 
import pickle
 
with open('listaDiplomado.bin','rb') as fh:
        olista= pickle.load(fh)
 
print(type(olista))
print(olista)
 
print('\n Listo... \n')