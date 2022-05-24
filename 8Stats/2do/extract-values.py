#  Alumno: Arnulfo Aranda Castro
#  Diplomado de TI -  Facultad de Telematica - Universidad de Colima
#  Almacenamiento a tupla
#  Almacenamiento a Dicionario
#  Almacenamiento a lista
#https://www.w3schools.com/python/python_for_loops.asp
import pandas as pd

iris = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv')
print(iris.head())

#ALMACENAMIENTO DE DATOS EN DICCIONARIO columna(sepal width)***
print("Almacenamiento en Diccionario")
dicionario = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv',usecols = ['sepal width']).to_dict()
print("** Información almacenada en el Diccionario: ",dicionario)
print(type(dicionario))#verificamos que tipo de variable se convirtio con la informacion almacenada

#ALMACENAMIENTO EN TUPLA columna(sepal length)
print("Almacenamiento en Tupla")
#como primer paso extraemos la información de nuestra tupla, en el cual le indicamos que columna usar para este proceso
tiris = pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv',usecols = ['sepal length'])
vtupla=[] #declaración e inicialización en cero de nuestra tupla
for x in tiris.index:
    #almacenamos la información extraida del api en nuestra variable
    vtupla.append(tuple(tiris.values[x]))
atupla=tuple(vtupla)
print("** Información almacenada en la Tupla: ",atupla)
print(type(atupla))#verificamos que tipo de variable se convirtio con la informacion almacenada

#ALMACENAMIENTO DE DATOS EN LISTA columna(pw)***
print("Almacenamiento en Lista")
lista=pd.read_csv('https://raw.githubusercontent.com/jrgpulido/ai4edu/master/iris%2Bheaders.csv',names = ['sl','sw','pl','pw','class'])
alista = lista.pw.to_list()
print("** Información almacenada en la Lista: ",alista)
print(type(alista))#verificamos que tipo de variable se convirtio con la informacion almacenada
