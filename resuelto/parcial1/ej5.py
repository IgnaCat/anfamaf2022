
#Ignacio Martinez Goloboff
#Ejercicio 5

from ej1 import serie_seno
from ej4 import rsteffensen

hx1, hy1 = rsteffensen(serie_seno, 3, 1e-5, 100)
print("x0=3 converge a", hx1[len(hx1)-1]) #Raiz 1
print("requiere {} iteraciones".format(len(hx1)))

hx2, hy2 = rsteffensen(serie_seno, 6, 1e-5, 100)
print("x0=6 converge a", hx2[len(hx2)-1]) #Raiz 2
print("requiere {} iteraciones".format(len(hx2)))

hx3, hy3 = rsteffensen(serie_seno, 4.5, 1e-5, 100)
print("x0=4.5 diverge aprox a", hx3[len(hx3)-1]) #Problema de divergencia con la recta tangente que pasa por (4.5, f(4.5))
print("requiere {} iteraciones".format(len(hx3)))