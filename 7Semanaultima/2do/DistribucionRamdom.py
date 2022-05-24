#  Alumno: Arnulfo Aranda Castro
#  Diplomado de TI -  Facultad de Telematica - Universidad de Colima
#  Distribución Random - 
import random
import matplotlib.pyplot as plt
alpha=2
r = random.weibullvariate(alpha, 2.5)
print('La distribucion de weibullvariate:', r)
plt.figure(figsize=(8, 4))
plt.hist([random.weibullvariate(alpha, 2.5) for i in range(1000)], bins = 50)
plt.grid()
plt.show()