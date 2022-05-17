#  Alumno: Arnulfo Aranda Castro
#  Diplomado de TI -  Facultad de Telematica - Universidad de Colima
#  ESCRITURA DE LISTA
 
import pickle
 
aList = ["Naranja", "Sandia", ["Sin semilla", "Con semilla"], "exportacion"]
 
with open('listaDiplomado.bin','wb') as fh:
        pickle.dump(aList,fh)
 
print('Lista Creada... \n')