#  Alumno: Arnulfo Aranda Castro
#  Diplomado de TI -  Facultad de Telematica - Universidad de Colima
#  Escritura de tuplas
import pickle
 
t=("Domingo","Lunes","Martes","Miercoles","Jueves")
 
with open('tsemana.bin','wb') as fh:
        pickle.dump(t,fh)
 
print('LISTO.. ARCHIVO DE TUPLAS CREADO...')