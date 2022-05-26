
#Ignacio Martinez Goloboff
#Ejercicio 3

import math
from ej1 import serie_seno

def rbisec(fun, I, err, mit):
    a, b = I[0], I[1]
    u, v = fun(a), fun(b)
    e = abs(b-a)
    hx = []
    hf = []
    if math.copysign(1,u) == math.copysign(1,v): 
        return hx, hf
    for k in range(mit):
        e = e/2
        c = a+e
        w = fun(c)
        hx.append(c)
        hf.append(w)
        if abs(e)<err:
            break
        if math.copysign(1,u) != math.copysign(1,w):
            b = c
            v = w
        else:
            a = c
            u = w

    return hx, hf

hx1, hy1 = rbisec(serie_seno, [2, 4], 1e-5, 100)
hx2, hy2 = rbisec(serie_seno, [4, 5], 1e-5, 100)


print("Raiz 1:", hx1[len(hx1)-1])
print("Raiz 2:", hx2[len(hx2)-1])