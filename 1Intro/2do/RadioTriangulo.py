#  Alumno: Arnulfo Aranda Castro
#  Diplomado de TI -  Facultad de Telematica - Universidad de Colima
# radious of circle inscribed in a tringle
#
# -> a=8,b=16,c=14
# <- r
import math
a=float(input("Igrese el valor del lado a: "))
b=float(input("Igrese el valor del lado b: "))
c=float(input("Igrese el valor del lado c: "))
 
#realizamos una suma para validar que el lado c del triangulo no sea mayor de la suma de los lados a+b
su=a+b
 
if (c < su):
    s=0.5*(a+b+c)
    r=math.sqrt(s*(s-a)*(s-b)*(s-c))/s
    r2 = round(r, 2)
    se = round(s, 2)
    print("Semiperimetro: ",se)
    print("Radio: ",r2)
   
else:
    print("Error, el lado c no puede ser mayor a la suma de los lados a y b")