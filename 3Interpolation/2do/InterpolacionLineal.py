#  Alumno: Arnulfo Aranda Castro
#  Diplomado de TI -  Facultad de Telematica - Universidad de Colima
#  INTERPOLACIÓN LINEAL 
p1=(-4,-2)
p2=(1,5)
y=3.7
 
 
def fun(y,p1,p2):
    a=(y-p1[1])*(p2[0]-p1[0])
    b=(p2[1]-p1[1])
    return p1[0]+(a/b)

print("\n")
print("Cuando Y vale: ",y," X equivale a: ",fun(y,p1,p2))
print("\n")
