#  Alumno: Arnulfo Aranda Castro
#  Diplomado de TI -  Facultad de Telematica - Universidad de Colima
#  INTERPOLACION - LARANGE
p1 = (-2, 4)
p2 = (-1, -2)
p3 = (3, 5)
p4 = (4.3, 11)
x = 7.7
#DECLARACION DE LA FUNCION
def fun(x, p1, p2, p3, p4):
    a = ((x - p2[0]) / (p1[0] - p2[0]))
    b = ((x - p3[0]) / (p1[0] - p3[0]))
    c = ((x - p4[0]) / (p1[0] - p4[0]))
    d = a * b * c * p1[1]
 
    a0 = ((x - p1[0]) / (p2[0] - p1[0]))
    b0 = ((x - p3[0]) / (p2[0] - p3[0]))
    c0 = ((x - p4[0]) / (p2[0] - p4[0]))
    d0 = a0 * b0 * c0 * p2[1]
 
    a1 = ((x - p1[0]) / (p3[0] - p1[0]))
    b1 = ((x - p2[0]) / (p3[0] - p2[0]))
    c1 = ((x - p4[0]) / (p3[0] - p4[0]))
    d1 = a1 * b1 * c1 * p3[1]
 
    a2 = ((x - p1[0]) / (p4[0] - p1[0]))
    b2 = ((x - p2[0]) / (p4[0] - p2[0]))
    c2 = ((x - p3[0]) / (p4[0] - p3[0]))
    d2 = a2 * b2 * c2 * p4[1]
 
    return d + d0 + d1 + d2

print("\n") 
print("Siendo X equivalente a: ", x, " se tiene que Y equivale a: ", fun(x, p1, p2, p3, p4))
print("\n")

